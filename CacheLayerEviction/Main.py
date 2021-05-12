'''
    Author: Shaik Faizan Roshan Ali
    Email: alsahercoder@gmail.com
    Date: 12 May 2021
    Program: Immplementation of Cache eviction policy (LRU)
'''

from MyMap import Mymap

if __name__ == "__main__":

    # my map takes two argument cahce limit and threshold of chaining in case of hashcode collisions
    mymap = Mymap(4)
    mymap.put('roshan', 12)
    mymap.put('Jasper', 14)
    mymap.put('Rishi', 15)
    mymap.put('Tom', 21)
    mymap.dll.display()

    # Evicted Tom once Anna is added
    mymap.put('Anna', 19)

    mymap.dll.display()

    # Observe the change in the list order
    mymap.get('Rishi')
    mymap.dll.display()
    mymap.get('roshan')
    mymap.dll.display()
