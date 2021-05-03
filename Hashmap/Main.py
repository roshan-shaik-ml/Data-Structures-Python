from MyMap import Hashmap

if __name__ == "__main__":

    hashmap = Hashmap(2)

    # put method
    hashmap.put("roshan", "20")
    hashmap.put("rishi", "12")
    hashmap.put("rima", "10")
    hashmap.put("riya", '32')
    hashmap.put("Ana", "21")

    # put method test
    pair = hashmap.get("roshan")
    print(pair)
    notFound = hashmap.get("roshi")
    print(notFound)
    
    # print the hashmap
    print(hashmap.hashmap)
