from bst import BST
from graph import Graph
from hash_set import HashSet
from hash_table import HashTable
from min_heap import MinHeap
from linked_list import LinkedList
from linked_queue import Queue
from linked_stack import Stack


def main():
    print("=======================================")
    print("         METRO CITY NAV                 ")
    print("=======================================\n")

    directory = BST()
    fares = HashTable()
    metro_map = Graph(directed=False)

    stations = ["Airport", "Beach", "Campus", "Downtown", "Eastside", "Factory", "Garden"]
    for s in stations:
        directory.insert(s, f"Station Info for {s}")
        metro_map.add_vertex(s)

    while True:
        print("\nMenu Options:")
        print("1. View Station Directory")
        print("2. Search for Station")
        print("3. Check Fare Zone")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            print("\nStations:", directory.inorder())
        elif choice == "2":
            name = input("Enter station name: ").strip()
            if directory.contains(name):
                print(f"Found: {directory.get(name)}")
            else:
                print("Station not found.")
        elif choice == "3":
            station = input("Enter station name: ").strip()
            zone = fares.get(station, default="Unknown Zone")
            print(f"Fare Zone for {station}: {zone}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()