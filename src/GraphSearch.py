import cairo
from igraph import *  # including graph library

import Csp

# graph vertex setup
vertex_values = []
for x in range(0, 36):
    vertex_values.append(str(x))


def get_shelf(book_id):
    """
    returns the corrispective shelf of the book
    :param book_id: book id
    :return: shelf number
    """
    if book_id == 2 or book_id == 14 or book_id == 16:
        n_shelf = 1
    if book_id == 1 or book_id == 3 or book_id == 5 or book_id == 6 or book_id == 7 or book_id == 12:
        n_shelf = 2
    if book_id == 10:
        n_shelf = 3
    if book_id == 4:
        n_shelf = 4
    if book_id == 27:
        n_shelf = 5
    if book_id == 8:
        n_shelf = 6
    if book_id == 22:
        n_shelf = 7
    if book_id == 21:
        n_shelf = 8
    if book_id == 28:
        n_shelf = 9
    if book_id == 20:
        n_shelf = 10
    if book_id == 9 or book_id == 11 or book_id == 13 or book_id == 15 or book_id == 17 or book_id == 18:
        n_shelf = 11
    if book_id == 19:
        n_shelf = 12
    if book_id == 26:
        n_shelf = 13
    if book_id == 23:
        n_shelf = 14
    if book_id == 25:
        n_shelf = 15
    if book_id == 24:
        n_shelf = 16
    if book_id == 10:
        n_shelf = 17
    return n_shelf


def get_nodes(shelf):
    """
    returns the corrispective node of the shelf
    :param shelf: shelf to search node for
    :return: node number
    """
    if shelf == 1:
        return 2
    if shelf == 2:
        return 3
    if shelf == 3:
        return 4
    if shelf == 4:
        return 5
    if shelf == 5:
        return 8
    if shelf == 6:
        return 9
    if shelf == 7:
        return 23
    if shelf == 8:
        return 22
    if shelf == 9:
        return 21
    if shelf == 10:
        return 19
    if shelf == 11:
        return 20
    if shelf == 12:
        return 18
    if shelf == 13:
        return 17
    if shelf == 14:
        return 16
    if shelf == 15:
        return 15
    if shelf == 16:
        return 13
    if shelf == 17:
        return 14
    if shelf == 18:
        return 11
    if shelf == 19 or shelf == 20:
        return 12


def bfs(graph, start, end):
    """
    breath first search algorithm
    :param graph: graph to search for
    :param start: start node
    :param end: end node
    :return: cost of the path
    """
    # maintain a queue of paths
    queue = [[start]]
    # push the first path into the queue
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph.neighbors(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def path_cost(path):
    """
    returns cost of a path
    :param path: path to find cost of
    :return: cost of the path
    """
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]


def add_cost(graph, start, neighbours):
    """
    adds cost to neighbour list
    :param graph:
    :param start:
    :param neighbours:
    :return weighted_list: list of neighbours with costs added
    """
    weighted_list = []

    for node2 in neighbours:
        weighted_list.append([node2, graph.es.select(_source=start, _target=node2)['weight'][0]])

    return weighted_list


def lowest_cost_first(graph, start, end):
    """
    returns path to end node, starting from start node, using Lowest Cost First Search
    :param graph:
    :param start:
    :param end:
    :return path: path to end node
    """
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        visited.append(node)
        if node == end:
            return path

        else:
            adjacent_nodes = add_cost(graph, node, graph.neighbors(node))
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


def setup_graph():
    """
    Creates weighted graph
    :return graph: graph
    :return edges: list of edges of the graph
    :return weights: list of weights of the graph edges
    """
    a = [('0', '1', 5), ('1', '2', 3), ('2', '3', 4), ('3', '4', 4), ('4', '5', 2), ('5', '6', 5), ('5', '7', 4),
         ('6', '7', 3), ('8', 9, 1), ('9', '10', 4), ('1', '11', 3), ('11', '12', 5), ('11', '29', 5), ('1', '29', 5),
         ('29', '13', 3), ('13', '14', 3), ('29', '30', 1), ('30', '31', 3), ('30', '15', 3), ('31', '16', 3),
         ('16', '17', 2),
         ('31', '32', 5), ('32', '18', 2), ('32', '19', 4), ('19', '20', 3), ('32', '22', 4), ('32', '21', 6),
         ('21', '23', 2),
         ('22', '19', 6), ('22', '21', 6), ('19', '21', 8), ('1', '28', 1), ('28', '24', 2), ('28', '8', 2),
         ('28', '27', 3), ('28', '26', 4), ('28', '25', 4), ('27', '25', 3), ('25', '26', 2), ('26', '27', 3)]

    edge = []
    weights = []
    for i in range(40):

        for j in range(2):
            k = 2
            edge.append(a[i][j])

        weights.append(a[i][k])

    edges = [(i, j) for i, j in zip(edge[::2], edge[1::2])]
    list1 = []
    for i in range(len(edges)):
        list1.append((int(edges[i][0]), int(edges[i][1])))

    graph = Graph()
    for i in range(0, 33):
        graph.add_vertex(i)

    graph.add_edges(list1)
    graph.es['weight'] = weights
    graph.es['label'] = weights
    edges = graph.get_edgelist()
    return graph, edges, weights


def find_solution(graph, start, goal):
    """
    executes a search on the graph and returns the path in form of a list of nodes
    :param start: starting node
    :param graph: graph to search into
    :param goal: goal of the search
    :return solution: list of nodes representing the solution
    """

    search_method = -1
    while search_method != 1 and search_method != 2:

        # search_method = int(input("Insert the search method: \n1:Breadth-first-search\n2:Lowest-cost-first-search\n"))
        search_method = 1

        if search_method == 1:
            solution = bfs(graph, start, goal)
            print("Path:\n" + str(solution))
        elif search_method == 2:
            solution = lowest_cost_first(graph, 0, goal)
            print("Solution is:\n")
            print([x[0] for x in solution])
            print("Cost of solution is: ", path_cost(solution)[0])
        else:
            print("Incorrect answer")

    return solution


def print_solution(graph, solution, weights, color):
    """
    displays an image of the solution of the search on the graph
    :param color: color of the printed solution
    :param weights: list of graph weights
    :param graph: graph to print
    :param solution: solution to highlight on the image
    :return:
    """

    edges = graph.get_edgelist()
    g = Graph(edges)
    vertex_set = set(solution)
    g.vs["color"] = "yellow"
    g.vs["size"] = 22
    g.es["label"] = weights
    try:
        sol_edges = g.vs.select(vertex_set)
    except TypeError:
        vertex_set = (x[0] for x in vertex_set)
        sol_edges = g.vs.select(vertex_set)

    sol_edges["color"] = color
    g.layout(layout='auto')
    plot(g, "grafico.png", vertex_label=vertex_values)


def research(book):
    """
    prints paths based on breath-cost-first to find all books in the shelves

    :param book: book to search for
    :return:
    """
    print("Thank you for borrowing the book: ", Csp.idToName(book))
    start_node = 0
    shelfNode = get_nodes(get_shelf(book))
    print("Your book is on the shelf number:", get_shelf(book))
    print("That's identified by the node:", shelfNode)
    # setup and print graph
    graph, edges, weights = setup_graph()

    # print solutions on graph
    print_solution(graph, find_solution(graph, start_node, shelfNode), weights, "purple")

    print("Check 'grafico.png' for visualizing the path")
