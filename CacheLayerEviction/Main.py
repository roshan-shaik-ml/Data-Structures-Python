from MyMap import Mymap

if __name__ == "__main__":


    mymap = Mymap(4) # my map takes two argument cahce limit and threshold of chaining
    mymap.put('roshan', 12)
    mymap.put('Jasper', 14)
    mymap.put('Rishi', 15)
    mymap.put("Tom", 21)
    mymap.dll.display()

    # evicted Tom once Anna is added
    mymap.put('Anna', 19)

    mymap.dll.display()

    # Obsere the change in the list order
    mymap.get('Rishi')
    mymap.dll.display()
    mymap.get('roshan')
    mymap.dll.display()