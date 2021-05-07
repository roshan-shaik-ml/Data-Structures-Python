class Multimap:

    def __init__(self):

        self.multimap = {}

    def put(self, string):

        sortedString = ''.join(sorted(string))
        if self.multimap.get(sortedString) == None:

            self.multimap[sortedString] = [string]
        else:

            self.multimap[sortedString].append(string)

    def entrySet(self):

        for i in self.multimap.values():

            print(i)
    
if __name__ == "__main__":

    strings = ['abc', 'acb', 'bca', 'ghi', 'igh', 'jkl']

    multimap = Multimap()
    for string in strings:

        multimap.put(string)
    
    multimap.entrySet()
