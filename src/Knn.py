import pandas as pd
from fuzzywuzzy import fuzz
from gensim.parsing.preprocessing import remove_stopwords
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
#import utils
#import graph

class KnnRecommender:
    def __init__(self):
        self.path_books = '../data/BX-Books.csv'
        self.path_ratings = '../data/BX-Book-Ratings.csv'
        self.book_rating_lim = 10
        self.user_rating_lim = 10
        self.model = NearestNeighbors()
        self.model.set_params(**{
            'n_neighbors': 20,
            'algorithm': 'auto',
            'metric': 'cosine',
        })

    @property
    def _prep_data(self):
        """
        prepare data for recommender
        join dataframes
        """
        # read data
        #headers = pd.read_csv(self.path_books, encoding='unicode_escape', nrows=0, sep=';').columns.tolist()
        #print(headers)
        #columns = ['title']
        #pd.read_csv(self.path_books, encoding='unicode_escape', usecols=columns, sep=';').to_csv('Books.csv', index=False)

        df_books = pd.read_csv(
            self.path_books,
            encoding="ISO-8859-1",
            sep=";",
            header=0,
            names=['isbn', 'title', 'author'],
            usecols=['isbn', 'title', 'author'],
            dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

        df_ratings = pd.read_csv(
            self.path_ratings,
            encoding="ISO-8859-1",
            sep=";",
            header=0,
            names=['user', 'isbn', 'rating'],
            usecols=['user', 'isbn', 'rating'],
            dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

        #df_books_ratings = pd.merge(df_ratings, df_books, on='isbn')
        #print(df_ratings)
        #print(df_books)
        # filter users who rated less than 50 books and books with less than 50 rates
        df_books_cnt = pd.DataFrame(df_ratings.groupby('isbn').size(), columns=['count'])
        popular_books = list(df_books_cnt.query('count >= @self.book_rating_lim').index)
        books_filter = df_ratings.isbn.isin(popular_books).values

        df_users_cnt = pd.DataFrame(df_ratings.groupby('user').size(), columns=['count'])
        active_users = list(df_users_cnt.query('count >= @self.user_rating_lim').index)
        users_filter = df_ratings.user.isin(active_users).values

        df_ratings_filtered = df_ratings[books_filter & users_filter]
        # create book user matrix
        df_books_ratings = pd.merge(df_ratings_filtered, df_books, on='isbn')
        #print(df_books_ratings)
        book_user_mat = df_books_ratings.pivot(index='isbn', columns='user', values='rating').fillna(0)

        # hashmap from book title to index
        hashmap = {
            book: i for i, book in
            enumerate(list(df_books.set_index('isbn').loc[book_user_mat.index].title))
        }
        book_user_mat_sparse = csr_matrix(book_user_mat.values)

        return book_user_mat_sparse, hashmap

    def _fuzzy_matching(self, hashmap, fav_book):
        """
        return the closest match via fuzzy ratio.
        If no match found, return None

        params:

        hashmap: dict, map book title name to index of the book in data

        fav_book: str, name of user input book

        return:

        index of the closest match
        """
        match_tuple = []
        # get match
        for title, idx in hashmap.items():
            ratio = fuzz.ratio(remove_stopwords(title.lower().replace(",", " ")),
                               remove_stopwords(fav_book.lower().replace(",", " ")))
            if ratio >= 60:
                match_tuple.append((title, idx, ratio))
        # sort
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            print('No results found')
        else:
            print('Found results: \n' + str([x[0] for x in match_tuple]))
            return match_tuple[0][1]

    def _inference(self, model, data, hashmap,
                   fav_book, n_recommendations):
        """
        return top n similar book recommendations based on user's input book

        params:

        model: sklearn model, knn model

        data: book-user matrix

        hashmap: dict, map book title name to index of the book in data

        fav_book: str, name of user input book

        n_recommendations: int, top n recommendations

        return:

        list of top n similar book recommendations
        """
        # fit
        model.fit(data)
        # get input book index
        print('Your book is:', fav_book)
        try:
            idx = self._fuzzy_matching(hashmap, fav_book)
            # inference
            #print('qui')
            #print(idx)
            distances, indices = model.kneighbors(
                data[idx],
                n_neighbors=n_recommendations + 1)
        except IndexError:
            exit(0)
        # get list of raw idx of recommendations
        raw_recommends = \
            sorted(
                list(
                    zip(
                        indices.squeeze().tolist(),
                        distances.squeeze().tolist()
                    )
                ),
                key=lambda x: x[1]
            )[1:n_recommendations + 1]

        # return recommendation (isbn, distance)
        return raw_recommends

    def make_recommendations(self, fav_book, n_recommendations):
        """
        make top n books recommendations

        params:

        fav_book: str, name of user input book

        n_recommendations: int, top n recommendations
        """
        # get data
        book_user_mat_sparse, hashmap = self._prep_data
        # get recommendations
        raw_recommends = self._inference(
            self.model, book_user_mat_sparse, hashmap,
            fav_book, n_recommendations)
        # print results
        book_list = []
        reverse_hashmap = {v: k for k, v in hashmap.items()}
        #print(reverse_hashmap)
        #print(raw_recommends)
        print('Recommendations for : ' + fav_book)
        for i, (idx, dist) in enumerate(raw_recommends):
            if idx in hashmap.values():
                print('{0}: {1}, with distance of {2}'.format(i + 1, reverse_hashmap[idx], dist))
                book_list.append(reverse_hashmap[idx])
            else:
                print(str(i+1) + ": Not found")
        return book_list


if __name__ == '__main__':
    #input("Press [enter] to show planimetry of the shop")
    #utils.show_planimetry()
    book_name = input('Insert favourite book name:\n')
    top_n = 10
    recommender = KnnRecommender()
    recommendation = recommender.make_recommendations(book_name, top_n)
    if recommendation is None:
        print("Not found")
    else:
        print("Found")
    '''
    if recommendation is not None:
        graph.research(recommendation)
    else:
        print("Not found")
    '''
