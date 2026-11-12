# metro-navigator

# Name:
    Deva Mahesh

# Class period:
    1A-B

-------------------------------------------------------

# How to run main.py:
    python main.py in root folder
    python -m unittest discover -s tests -t .

    or just click the play btn (its rlly easy)' - a MUST have 3rd option

    
    # Metro City Navigator - Class Descriptions (README)

## LinkedList
This class keeps a list of items in order and is used to track the rider trip log in the demo. It's built from scratch using custom 'Node' objects that hold a value and point to the next node, with 'head' and 'tail' pointers tracking the ends. One smart choice here was keeping a 'tail' pointer and a size counter so adding to the end ('append') happens right away without having to walk through the whole list.

## HashTable
This class gives fast key-value lookups so we can match station names to their fare zones. It uses a list of buckets (starting at 8) and handles collisions by chaining custom 'HashNode' objects together. We built a custom rolling hash function with 'ord()' and made the table double its size whenever it gets more than 75% full so lookups stay quick.

## BST
This class keeps an alphabetical directory of stations so we can search for stops or grab a range of them easily. It's built with custom 'BSTNode' objects that hold a key, a value, and left/right child pointers. Instead of using recursion, we wrote all the methods using loops with stacks and queues so the program won't crash even if the tree gets really lopsided.

## MinHaep
This class works like a priority to-do list that sorts metro maintenance jobs by urgency (smaller numbers go first). It's backed by a regular Python list ('_data') storing '(priority, item)' pairs and uses simple index math to find parents and children. We made sure it only compares the priority numbers during swaps so that weird or unorderable task items (like dictionaries) don't crash the program on a tie.

## Graph
This class represents the actual Metro City map with stations and the tracks connecting them. It's built using our 'HashTable', where each station name points to a 'LinkedList' of simple 'Edge' objects. We kept the 'Edge' objects super basic with no weights or distances, and for two-way connections we just store the link in both directions while only counting it as one edge.

## Stack
This class acts like a browser "Back" button (Last-In, First-Out) to track a rider's recent stops and check for balanced brackets. It's built completely on top of our 'LinkedList' stored inside 'self._list'. By treating the 'head' of the linked list as the top of the stack, both 'push' and 'pop' happen instantly without scanning any nodes.

## Queue
This class works like a normal waiting line (First-In, First-Out) for ticket booths and boarding passengers. Just like the stack, it uses a 'LinkedList' stored in 'self._list' as its only storage. Putting the front of the line at 'head' and the back of the line at 'tail' lets us add new people and serve the front person right away in constant time.

## HashSet
This class holds a collection of unique station names and lets us do set math like union and intersection to compare neighbors. It's built on top of our 'HashTable' stored in 'self._map' (or '_table'). By saving each item as a key in the hash table with a dummy 'True' value, we get fast duplicate checks and set operations without having to build a whole new storage system from scratch.