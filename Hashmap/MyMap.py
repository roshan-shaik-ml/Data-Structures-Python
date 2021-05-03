'''
    Author: Shaik Faizan Roshan Ali
    Date: May 4 2021
    About: A Simple Multimap implementation
'''

class Hashmap:

    
    def __init__(self, threshold = 10):

        self.mod = 26
        self.hashmap = {}
        self.threshold = threshold # threshold is the limit for chaining
        self.limit = 1  # limit for letter in hash function

    def __getHashcode(self, key):

        # sum the first n (self.limit) characters
        # find the remainder of sum after mod 
        # return the hashcode
        hashcode = 0
        for i in key[:self.limit]:

            hashcode += ord(i)
        
        hashcode = hashcode % self.mod
        return hashcode
    
    def __rehash(self):

        self.mod = self.mod * 2
        self.limit += 1
        temp = self.hashmap.copy()
        self.hashmap.clear()

        for lists in temp.values():

            for pair in lists:

                self.put(pair[0], pair[1])

    def put(self, key, value):
        
        hashcode = self.__getHashcode(key)
        if self.hashmap.get(hashcode) == None:

            self.hashmap[hashcode] = [(key, value)]
        else:

            if len(self.hashmap[hashcode]) < self.threshold:

                self.hashmap[hashcode].append((key, value))
            else:

                self.hashmap[hashcode].append((key, value))
                self.__rehash()

    def get(self, key):

        hashcode = self.__getHashcode(key)
        linkedlist = self.hashmap[hashcode]

        for index in range(0, len(linkedlist)):

            if key == linkedlist[index][0]:

                return linkedlist[index]
        return "Key not found"