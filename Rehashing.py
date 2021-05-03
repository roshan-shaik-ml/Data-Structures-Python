# This hashmap is from the first letter of their names 
# to their complete name with threshold of three values

if __name__ == "__main__":

    names = ['Liam','Noah','Oliver','William','Elijah',
        'James','Benjamin','Lucas','Mason','Ethan',
        'Alexander','Henry','Jacob','Michael','Daniel'
        ,'Logan','Jackson','Sebastian','Jack','Aiden','Owen',
        'Samuel','Matthew','Joseph','Levi','Mateo','David',
        'John','Wyatt','Carter','Julian','Luke','Grayson',
        'Isaac','Jayden','Theodore','Gabriel','Anthony','Dylan',
        'Leo','Lincoln','Jaxon','Asher','Christopher','Josiah',
        'Andrew','Thomas','Joshua','Ezra','Hudson'
        ]
    completed = False

    for letter in range(0, 10):

        hashmap = {}
        for name in names:

            if hashmap.get(name[:letter+1]) == None:

                hashmap[name[:letter+1]] = []
                hashmap[name[:letter+1]].append(name)    
            else:

                if len(hashmap[name[:letter+1]]) < 3:

                    hashmap[name[:letter+1]].append(name)
                else:
                    break
            
            # To check if the whole set of names are completed
            if name == names[-1]:
                completed = True
        
        # Print the hashmap to verify before rehashing
        print(hashmap)
        if completed == True:
            break
