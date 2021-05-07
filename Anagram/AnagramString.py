from MyMultimap import Multimap

if __name__ == "__main__":

    strings = ['abc', 'acb', 'bca', 'ghi', 'igh', 'jkl']
    sortedStrings = [''.join(sorted(string)) for string in strings]

    multimap = Multimap()
    for index in range(0, len(strings)):

        multimap.put(sortedStrings[index], strings[index])
    
    multimap.entrySet()


    