# from MyTreemap import BST
from MyTreemap import Treemap

if __name__ == "__main__":

    treemap = Treemap()
    treemap.put(1010, 'Roshan')
    treemap.put(1004, 'Alex')
    treemap.put(1003, 'Jasper')
    treemap.put(1007, 'Alan')
    treemap.put(1015, 'Juliet')
    treemap.put(1013, 'Romeo')
    treemap.put(1020, 'Gandhi')

    # Search for existent keys
    treemap.get(1015)

    # Search for non-existent keys
    treemap.get(1111)

    # update key check
    treemap.get(1004)
    treemap.put(1004, 'Robert')
    treemap.get(1004)

    # Display the tree
    treemap.entrySet()
