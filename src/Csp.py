from constraint import *
import bisect


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
    :return:
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
            print("we're open")
            return str(hour)


def nameToId(name):
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


# funzione per prenotare il libro
def borrowABook(list1, list2):
    if list1 == []:
        print("Rightnow all books are unavailable, there's nothing to borrow")
        return
    print("list of unavailable book")
    for book in list2:
        print("\n\t", idToName(book))
    print("otherwise, you can chose a book to borrow from the below list :")
    list3 = difference(list1, list2)
    for book in list3:
        print("\n\t", idToName(book))

    name = input("Write the name of the book chosen \n")
    idbook = int(nameToId(name))

    return idbook


def difference(list1, list2):
    list3 = []
    for element in list1:
        if element not in list2:
            list3.append(element)
    return list3


def returnABook(list2):
    if list2 == []:
        print("Rightnow all books are available, there's nothing to return")
        return

    print("here there's the list of unavailable book")
    for book in list2:
        print("\n\t", idToName(book))
    name = input("which book are you returning?")
    bookreturned = int(nameToId(name))

    return bookreturned


def checkConstraint(day, time, book, list, op):

    if op == 1:
        # formato tupla : {{'Day': 6, 'Time': 19, 'idBookUn': 11}
        day += ','
        time += ','
        id = str(book)
        id += '}'
        for element in list:

            strings = str(element)
            strings = strings.split(' ')
            # print(strings)
            if (day == strings[1]) and (time == strings[3]) and (id == strings[5]):
                print("sono qua")
                return True

        return False

    elif op == 2:
        # formato tupla: {'Day': 6, 'idBookUn': 11, 'Time': 19}
        day += ','
        id = str(book)
        id += ','
        time += '}'

        for element in list:
            strings = str(element)
            strings = strings.split(' ')
            # print(strings)

            #            print(day)
            #            print(id)
            #            print(time)
            if (day == strings[1]) and (id == strings[3]) and (time == strings[5]):
                print("sono qui")
                return True

        return False


def constraint(list):
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
    print(objectProblem)
    return objectProblem


"""
def returnConstraint(list2):
    problem = Problem()
    problem.addVariable("Day", [1, 2, 3, 4, 5, 6])
    problem.addVariable("Time", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    problem.addVariable("idBookUn", list2)
    problem.addConstraint(lambda Day, Time, idBookUn:
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
"""

if __name__ == "__main__":
    book = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28]
    bookBorrowed = [1, 7, 11, 18, 20, 25]

    keepOn = 0

    while keepOn != 2:
        """
        problem = Problem()
        problem2 = Problem()
        problem.addVariable("Day", [1, 2, 3, 4, 5, 6])
        problem2.addVariable("Day", [1, 2, 3, 4, 5, 6])
        problem.addVariable("Time", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        problem2.addVariable("Time", [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

        actualBook = difference(book, bookBorrowed)

        problem.addVariable("idBookA", actualBook)
        problem2.addVariable("idBookUn", bookBorrowed)

        problem.addConstraint(lambda Day, Time, idBookA:
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

        # ogni volta che riparte il ciclo questo mi sminchia tutto
        problem2.addConstraint(lambda Day, Time, idBookUn:
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
        # print(objectProblem)
        objectProblem2 = problem2.getSolutions()
        # non ho capito perché  anziche l'ordine day-time-id mi fa le tuple come day-id-time
        print(objectProblem2)
        """
        actualBook = difference(book, bookBorrowed)

        print("insert day as integer: \n1:Monday\n2:Tuesday\n3:Wednesday\n4:Thursday\n5:Friday\n6:Saturday\n")
        day = input("day: \n")
        if checkDay(day) is False:
            print("Wrong day format")
            exit(0)
        print("insert time in the following format: [HH].[MM] (example 10.20)\n")
        time = input("time: \n")
        hour = checkTime(time, day)
        choice = input("are you going to borrow or return a book? write 1 to borrow or 2 to return\n")
        if choice == '1':
            bookChoice = borrowABook(book, bookBorrowed)
            if checkConstraint(day, hour, bookChoice, constraint(actualBook), int(choice)):
                print("You can take this book")
                # update list
                actualBook.remove(bookChoice)
                bisect.insort(bookBorrowed, bookChoice)
                print("Operation Done ... Thank you for borrowing a book")
                print(actualBook)  # lo elimina correttamente
                print(bookBorrowed)
            else:
                print("We are sorry, but for some reason you can't take this book (constraints problems occurred)")

        elif choice == '2':
            bookChoice = returnABook(bookBorrowed)
            if checkConstraint(day, hour, bookChoice, constraint(bookBorrowed), int(choice)):
                print("Thank you for returning this book")
                # update list
                bookBorrowed.remove(bookChoice)
                bisect.insort(actualBook, bookChoice)
                print(actualBook)
                print(bookBorrowed)
                print("Operation done successfully!")
            else:
                print("We are sorry, but for some reason you can't return this book (constraints problems occurred)")

        keepOn = int(input("\nDo you need something more? press 1 to continue or 2 to leave:\n"))
        if keepOn == 2:
            print("Goodbye and thank you!")
            exit(0)
