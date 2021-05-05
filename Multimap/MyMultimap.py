'''
    Author: Shaik Faizan Roshan Ali
    Date: May 4 2021
    About: A Simple Multimap implementation
'''

class Multimap:

    
    def __init__(self, threshold = 10):

        self.mod = 26
        self.multimap = {}
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
        temp = self.multimap.copy()
        self.multimap.clear()

        for lists in temp.values():

            for pair in lists:

                self.put(pair[0], pair[1])

    def put(self, key, value):
        
        hashcode = self.__getHashcode(key)
        if self.multimap.get(hashcode) == None:

            self.multimap[hashcode] = [[key, value]]
        else:
            
            # check if the key already exist
            for i in range(0, len(self.multimap[hashcode])):

                if self.multimap[hashcode][i][0] == key:
                    self.multimap[hashcode][i].append(value)
                    print("updated the key value pair")
                    return None
                

            if len(self.multimap[hashcode]) < self.threshold:

                self.multimap[hashcode].append((key, value))
            else:

                self.multimap[hashcode].append((key, value))
                self.__rehash()

    def get(self, key):

        hashcode = self.__getHashcode(key)
        linkedlist = self.multimap[hashcode]

        for index in range(0, len(linkedlist)):

            if key == linkedlist[index][0]:

                return linkedlist[index]
        return "Key not found"