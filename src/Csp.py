from constraint import *  # including csp constraint library
import bisect

import GraphSearch


def checkDay(day):
    """
    function that check if the day chosen by the user it's actually a
    workday or no (based on library's timetable)
    :param day: week day, specified by the user
    :return: a boolean value: False if day isn't a work day, True otherwise
    """
    if 0 < int(day) < 7:
        return True
    else:
        return False


def checkTime(time, date):
    """
     function that check if the input parameter "time" is consistent to library's timetable
    :param time:time expressed in the format HH.MM (hours.minutes)
    :param date: date chosen
    :return: a string that match with the input

    """

    hour = time.split('.')  # splitting the input string in 2 substring
    mins = int(hour[1])
    # print(mins)
    hour = int(hour[0])
    # print(hour)
    day = int(date)
    # print(day)

    if (not (0 < hour < 24)) or (not (0 <= mins < 60)):
        print("Invalid time.")
        exit(0)
    elif (not (9 <= hour <= 19)) or (hour == 19 and mins > 0):
        print("We're sorry, but the library is currently closed.")
        exit(0)
    else:
        if (day == 6) and (12 <= hour <= 19):
            print("We're sorry, but the library is currently closed.")
            exit(0)
        else:
            print("We're open")
            return str(hour)


def nameToId(name):
    """
    function that return the id of a book
    :param name: book name
    :return:  book id
    """
    if name.lower() == '1984':
        return '1'
    elif name.lower() == 'animal farm':
        return '2'
    elif name.lower() == 'harry potter':
        return '3'
    elif name.lower() == 'hamlet':
        return '4'
    elif name.lower() == 'history':
        return '5'
    elif name.lower() == 'if this is a man':
        return '6'
    elif name.lower() == 'one, no one and one hundred thousand':
        return '7'
    elif name.lower() == 'the betrothed':
        return '8'
    elif name.lower() == 'the castle':
        return '9'
    elif name.lower() == 'the divine comedy':
        return '10'
    elif name.lower() == 'the idiot':
        return '11'
    elif name.lower() == 'the lord of rings':
        return '12'
    elif name.lower() == 'the name of the rose':
        return '13'
    elif name.lower() == 'the metamorphosis':
        return '14'
    elif name.lower() == 'the possessed':
        return '15'
    elif name.lower() == 'the trial':
        return '16'
    elif name.lower() == "zeno's Conscience":
        return '17'
    elif name.lower() == "wuthering heights":
        return '18'
    elif name.lower() == 'the ultimate finance book':
        return '19'
    elif name.lower() == 'learning java':
        return '20'
    elif name.lower() == 'principles of mathematical analysis':
        return '21'
    elif name.lower() == 'human body anatomy':
        return '22'
    elif name.lower() == 'it':
        return '23'
    elif name.lower() == 'fairy tales and folklore':
        return '24'
    elif name.lower() == 'fables':
        return '25'
    elif name.lower() == 'this book is funny':
        return '26'
    elif name.lower() == 'greek mythology':
        return '27'
    elif name.lower() == 'mindhunter':
        return '28'
    else:
        return 'id not found'


def idToName(id):
    """
    function that return the name of a book, starting from its id
    :param id:  book id
    :return: book name string
    """
    if id == 1:
        return '1984'
    elif id == 2:
        return 'Animal farm'
    elif id == 3:
        return 'Harry Potter'
    elif id == 4:
        return 'Hamlet'
    elif id == 5:
        return 'History'
    elif id == 6:
        return 'If this is a man'
    elif id == 7:
        return 'One, no one and one hundred thousand'
    elif id == 8:
        return 'The betrothed'
    elif id == 9:
        return 'The castle'
    elif id == 10:
        return 'The divine comedy'
    elif id == 11:
        return 'The idiot'
    elif id == 12:
        return 'The lord of rings'
    elif id == 13:
        return 'The name of the rose'
    elif id == 14:
        return 'The metamorphosis'
    elif id == 15:
        return 'The possessed'
    elif id == 16:
        return 'The trial'
    elif id == 17:
        return "Zeno's Conscience"
    elif id == 18:
        return 'Wuthering heights'
    elif id == 19:
        return 'The ultimate finance book'
    elif id == 20:
        return 'Learning Java'
    elif id == 21:
        return 'Principles of mathematical analysis'
    elif id == 22:
        return 'Human body anatomy'
    elif id == 23:
        return 'It'
    elif id == 24:
        return 'Fairy tales and folklore'
    elif id == 25:
        return 'Fables'
    elif id == 26:
        return 'This book is funny'
    elif id == 27:
        return 'Greek mythology'
    elif id == 28:
        return 'Mindhunter'
    else:
        return 'name not found'


def borrowABook(list1, list2):
    """
    function that allow users to borrow a book. after printing the list of available book, users can choose
    the one that they want to borrow
    :param list1: list of available books
    :param list2: list of unavailable books
    :return: id of the borrowed book
    """
    print("List of unavailable book")
    for book in list2:
        print("\n\t", idToName(book))
    print("Otherwise, you can chose a book to borrow from the below list :")
    list3 = difference(list1, list2)
    for book in list3:
        print("\n\t", idToName(book))

    name = input("Write the name of the book chosen \n")
    idbook = int(nameToId(name))

    return idbook


def difference(list1, list2):
    """
    the function return a new list of element, that corresponds to list1 - list2
    :param list1: first list
    :param list2: second list
    :return: third list of element (list1 - list2)
    """
    list3 = []
    for element in list1:
        if element not in list2:
            list3.append(element)
    return list3


def returnABook(list2):
    """
    function that allows user to return a book, which was unavailable in the library
    :param list2: list of books that are currently unavailable (that have to be return)
    :return: id of book returned
    """
    print("Here's the list of unavailable book")
    for book in list2:
        print("\n\t", idToName(book))
    name = input("Which book are you returning?")
    bookreturned = int(nameToId(name))

    return bookreturned


def checkConstraint(day, time, book, list, op):
    """
    function that check if the parameters observ the constraint, before borrowing or returning a book.
    :param day:string =  day of the week
    :param time:string =  hour
    :param book: int = id of the book returned/borrowed
    :param list: list of constraint
    :param op: int that correspond to the operation that the user's doing ( 1 = borrow a book, 2 = return a book)
    :return: boolean value (true if the operation op is possible, false otherwise)
    """
    # for borrowing a book
    if op == 1:

        day += ','
        time += ','
        id = str(book)
        id += '}'
        # element : {{'Day': 6, 'Time': 19, 'idBookUn': 11}
        for element in list:

            strings = str(element)
            strings = strings.split(' ')
            if (day == strings[1]) and (time == strings[3]) and (id == strings[5]):
                return True

        return False

    # for returning a book
    elif op == 2:

        day += ','
        id = str(book)
        id += ','
        time += '}'

        # element: {'Day': 6, 'idBookUn': 11, 'Time': 19}
        for element in list:
            strings = str(element)
            strings = strings.split(' ')

            if ((day == strings[1]) and (id == strings[3]) and (time == strings[5])) or \
                    ((id == strings[1]) and (day == strings[3]) and (time == strings[5])):
                return True

        return False


def constraint(list):
    """
    function that create a list of constraint
    :param list: list of books (available or unavailable)
    :return: objectProblem = constraint in list form
    """
    problem = Problem()
    problem.addVariable("Day", [1, 2, 3, 4, 5, 6])
    problem.addVariable("Time", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    problem.addVariable("idBook", list)
    problem.addConstraint(lambda Day, Time, idBook:
                          (Day == 1 and 9 <= Time < 12) or
                          (Day == 1 and 16 <= Time < 19) or
                          (Day == 2 and 9 <= Time < 12) or
                          (Day == 2 and 16 <= Time < 19) or
                          (Day == 3 and 9 <= Time < 12) or
                          (Day == 3 and 16 <= Time < 19) or
                          (Day == 4 and 9 <= Time < 12) or
                          (Day == 4 and 16 <= Time < 19) or
                          (Day == 5 and 9 <= Time < 12) or
                          (Day == 5 and 16 <= Time < 19) or
                          (Day == 6 and 9 <= Time < 12)
                          )
    objectProblem = problem.getSolutions()
    return objectProblem


# if __name__ == "__main__":
def doCSP():
    # total books
    book = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28]
    # list of unavailable books, at the beginning
    bookBorrowed = [1, 7, 11, 18, 20, 25]

    # list of available book
    actualBook = difference(book, bookBorrowed)

    keepOn = 0

    while keepOn != 2:

        # choosing the day
        print("Insert day as integer: \n1:Monday\n2:Tuesday\n3:Wednesday\n4:Thursday\n5:Friday\n6:Saturday\n")
        day = input("Day: \n")
        if checkDay(day) is False:
            print("Wrong day format")
            exit(0)
        # choosing the time
        print("Insert time in the following format: [HH].[MM] (example 10.20)\n")
        time = input("Time: \n")
        hour = checkTime(time, day)
        # choosing the operation
        choice = input("Do you want to borrow or return a book? write 1 to borrow or 2 to return\n")

        if choice == '1' and bool(actualBook):
            # borrowing a book
            bookChoice = borrowABook(book, bookBorrowed)
            if checkConstraint(day, hour, bookChoice, constraint(actualBook), int(choice)):
                print("You can take this book")
                # update list
                actualBook.remove(bookChoice)
                bisect.insort(bookBorrowed, bookChoice)
                print("Operation Done ... Thank you for borrowing a book\n")
                searchChoice = int(input("Do you want to search the book? write 1 to search it or 2 to only borrow it\n"))
                if searchChoice == 1:
                    GraphSearch.research(bookChoice)
            else:
                print("We are sorry, but for some reason you can't take this book (constraints problems occurred)")

        elif choice == '2' and bool(bookBorrowed):
            # returning a book
            bookChoice = returnABook(bookBorrowed)
            if checkConstraint(day, hour, bookChoice, constraint(bookBorrowed), int(choice)):
                print("Thank you for returning this book")
                # update list
                bookBorrowed.remove(bookChoice)
                bisect.insort(actualBook, bookChoice)
                print("Operation done successfully!")
            else:
                print("We are sorry, but for some reason you can't return this book (constraints problems occurred)")
        """
        if bool(bookBorrowed):
            print("Rightnow all books are available, there's nothing to return")
        elif bool(actualBook):
            print("Rightnow all books are unavailable, there's nothing to borrow")
        """

        keepOn = int(input("\nDo you need something more? press 1 to continue or 2 to leave:\n"))
