class Graph:
    
    def __init__(self):
        
        self.graph = {}
        
    
    def addEdge(self, vertex1, vertex2):
        
        if self.graph.get(vertex1) == None:
            
            self.graph[vertex1] = {vertex2}
        else:
            
            self.graph[vertex1].add(vertex2)
        
        if self.graph.get(vertex2) == None:
            
            self.graph[vertex2] = {vertex1}
        else:
            
            self.graph[vertex2].add(vertex1)
        
    
    def printVisited(self, vertex, visited):
        
        visited.add(vertex)
        print(vertex)
 
        for neighbour in self.graph[vertex]:
            
            if neighbour not in visited:
        
                self.printVisited(neighbour, visited)
        return
    
    
    def dfs(self, vertex):
        
        visited = set()
        for vertex in self.graph.keys():
            
            if vertex not in visited:
                
                self.printVisited(vertex, visited)
           
        return

if __name__ == "__main__":
    
    graph = Graph()
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 1)
    graph.addEdge(2, 5)
    print(graph.graph)
    graph.dfs(1)