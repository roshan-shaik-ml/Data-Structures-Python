class Hashmap:

    def __init__(self):

        self.hashmap = {}
        
    def build(self, start, end):

        for year in range(start, end+1):

            self.hashmap[year] = 0
    
    def put(self, birth, death):

        for year in range(birth, death+1):

            self.hashmap[year] = self.hashmap[year] + 1
        
    def maxPopulated(self):

        pop = 0
        popYear = 0
        for key in self.hashmap.keys():

            if self.hashmap[key] >= pop:
                
                pop = self.hashmap[key]
                popYear = key
                maxPop = pop
        
        print("Max population in year " + str(popYear) + " with population " + str(pop))

if __name__ == "__main__":

    # birth = list(map(int, input().split()))
    # death = list(map(int, input().split()))

    birth = [1990, 1995, 1992, 1990]
    death = [1992, 1999, 2000, 1996]

    minBirthYear = min(birth)
    maxDeathYear = max(death)

    hashmap = Hashmap()
    hashmap.build(minBirthYear, maxDeathYear)
    
    for index in range(0, len(birth)):

        hashmap.put(birth[index], death[index])
    
    hashmap.maxPopulated()