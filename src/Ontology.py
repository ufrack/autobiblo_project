# -*- coding: utf-8 -*-
from owlready2 import *

print("__________________________________________________________________________________________________________________\n")
print("_______________________________")
print("AutoBiblo Ontology Visualizer |")
print("_______________________________\n")
onto = get_ontology("library.owl").load()

#print the classes
print("Class list in ontology:\n")
print(list(onto.classes()), "\n")

#print the object properties
print("Object property in ontology:\n")
print(list(onto.object_properties()), "\n")

#print the data properties
print("Data property in ontology:\n")
print(list(onto.data_properties()), "\n")

#print the individual entities
print("Books list in ontology:\n")
books = onto.search(is_a = onto.Book)
print(books, "\n")

print("Authors list in ontology:\n")
authors = onto.search(is_a = onto.Author)
print(authors, "\n")

print("Genres list in ontology:\n")
genres = onto.search(is_a = onto.Genre)
print(genres, "\n")

print("Publishers list in ontology:\n")
publishers = onto.search(is_a = onto.Publisher)
print(publishers, "\n")

print("Rooms list in ontology:\n")
rooms = onto.search(is_a = onto.Room)
print(rooms, "\n")

print("Shelves list in ontology:\n")
shelves = onto.search(is_a = onto.Shelf)
print(shelves, "\n")

print("Students list in ontology:\n")
students = onto.search(is_a = onto.Student)
print(students, "\n")

print("__________________________________________________________________________________________________________________\n")

print("___________________________")
print("AutoBiblo Example Queries |")
print("___________________________\n")

#example query_1: List of books available in a specific shelf
print("List of books available in Shelf_1:\n")
book = onto.search(is_a = onto.Book, isAvailable = onto.search(is_a =onto.Shelf_1))
print(book, "\n")

#example query_2: List of books of a specific genre
print("List of narrative books:\n")
book = onto.search(is_a = onto.Book, hasGenre = onto.search(is_a = onto.Narrative))
print(book, "\n")







