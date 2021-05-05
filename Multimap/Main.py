from MyMultimap import Multimap

if __name__ == "__main__":

    multimap = Multimap(2)

    # put method
    multimap.put("roshan", "20")
    multimap.put("rishi", "12")
    multimap.put("rima", "10")
    multimap.put("riya", '32')
    multimap.put("Ana", "21")
    multimap.put("roshan", "25")
    # put method test
    pair = multimap.get("roshan")
    print(pair)
    notFound = multimap.get("roshi")
    print(notFound)
    
    # print the multimap
    print(multimap.multimap)
