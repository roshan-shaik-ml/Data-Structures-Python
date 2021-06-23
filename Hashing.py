def linearProbing(value, i):

    # key = (value mod m + i ) mod m 
    # m is the table size
    key = (( value % 11 ) + i) % 11

    return key

def doubleHashing(value, i):
    
    hash1 = value
    hash2 = 1 + value % (i - 1)
    key = hash1 + i*hash2

    return key

def quadraticProbing(value, i):

    # key = ( (value mod m) + i x c1 + i^2 x c2 ) mod m
    # c1 and c2 can take any values
    # m is the table size
    c1 = 1
    c2 = 3
    key = ( (value % 11) + (i * c1) + (i**2 * (c2)) ) % 11
    return key

if __name__ == "__main__":

    hashmap1, hashmap2, hashmap3 = {}, {}, {}
    arr = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    for value in arr:

        for i in range(0, 11):

            key = quadraticProbing(int(value), i)
            if hashmap1.get(key) == None:

                hashmap1[key] = int(value)
                break
        
        for i in range(0, 11):

            key = linearProbing(int(value), i)
            if hashmap2.get(key) == None:

                hashmap2[key] = int(value)
                break

        for i in range(0, 11):

            key = doubleHashing(int(value), i)
            if hashmap3.get(key) == None:

                hashmap3[key] = int(value)
                break
    
    print("Quadratic probing hashmap")
    print(hashmap1)

    print("Linear Probing Hashmap")
    print(hashmap2)

    print("double Hashing Hashmap")
    print(hashmap3)
