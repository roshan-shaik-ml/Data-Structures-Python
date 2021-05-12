
from DoubleLinkedList import DoubleLinkedList

class Mymap:


    def __init__(self, cacheLimit = 5, threshold = 2):

        self.cacheLimit = cacheLimit
        self.mod = 26
        self.hashmap = {}
        self.threshold = threshold # threshold is the limit for chaining of hashcode collision
        self.limit = 1  # limit for letter in hash function
        self.dll = DoubleLinkedList()
        self.currentCache = 0


    def rehash(self):

        self.mod = self.mod * 2
        self.limit += 1
        temp = self.hashmap.copy()
        self.hashmap.clear()

        for lists in temp.values():

            for pair in lists:

                self.put(pair[0], pair[1])
        

    def getHashcode(self, key):

        hashcode = 0
        for i in key[:self.limit]:

            hashcode += ord(i)
        
        hashcode = hashcode % self.mod
        return hashcode
        

    def put(self, key, value):

        hashcode = self.getHashcode(key)

        # checking cache limit before adding
        if self.currentCache + 1 > self.cacheLimit:

            toDelete = self.dll.delete()
            toDelteHashcode = self.getHashcode(toDelete)
            for index in range(0, len(self.hashmap[toDelteHashcode])):

                if self.hashmap[toDelteHashcode][index][0] == key:

                    self.hashmap[toDelteHashcode].pop(index)

        self.currentCache += 1 # increment current cache limit

        # if hashcode doesn't exist in dictionary, add it
        if self.hashmap.get(hashcode) == None:

            node = self.dll.insert(key, value, self.cacheLimit)
            self.hashmap[hashcode] = [[key, node]]
        
        # if exists add it to their exisiting list
        else: 

            for pair in self.hashmap[hashcode]:

                if pair[0] == key:
                    
                    # override the value if key exists with the new value
                    pair[1].value = value
                    return
            
            # check the limit of chaining 
            if len(self.hashmap[hashcode]) < self.threshold:

                self.hashmap[hashcode].append((key, value))
            # if more than necessary rehash the hashmap
            else:

                self.hashmap[hashcode].append((key, value))
                self.rehash()

    def get(self, key):

        # get the hashcode using key
        hashcode = self.getHashcode(key)

        if hashcode != None:
            for pair in self.hashmap[hashcode]:

                if pair[0] == key:

                    print(pair[0], ": ", pair[1].value)
                    self.dll.repositionNode(pair[1])
                    return
        else:

            print("key not found") 
        
    def leastRecentlyUsed(self):

        print(self.dll)