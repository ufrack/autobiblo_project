import Csp
import Knn
import Ontology

if __name__ == "__main__":

    choice: int = 0
    knnChoice: int = 0

    print("_____________________")
    print("Welcome in AutoBiblo!")
    while choice != 4:
        print("_____________________________________________________________________________________________________\n")

        print("Choose operation: ")
        print("1) Borrow or Return a Book")
        print("2) Book Recommender")
        print("3) Ontology Visualizer")
        print("4) Exit\n")

        catch = 2
        while catch == 2:
            try:
                choice = int(input("Insert choice number: "))
            except ValueError:
                print("Invalid choice, try again...\n")
            else:
                catch = 1

        match choice:
            case 1:
                Csp.doCSP()
            case 2:
                while knnChoice == 0:
                    Knn.doKNN()
                    knnChoice = int(input("Do you want other recommendations? 0 to redo, 1 to exit\n"))
            case 3:
                Ontology.doOntology()

    print("See you soon!")


