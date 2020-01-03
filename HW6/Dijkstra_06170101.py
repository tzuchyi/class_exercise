
from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
        self.dict=defaultdict(list)
        
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
     

    def Dijkstra(self, s): 
        long=len(self.graph)
        nodes = [i for i in range(long)]  
        visited=[]  
        
        if s in nodes:
            nodes.remove(s)
            visited.append(s)
            
        else:
            return None
        
        dictionary = {str(s):0}
        distance={s:0}  
        
        for i in nodes:
            distance[i]=self.graph[s][i]  

        k=pre=s
        while nodes:
            mid_distance=float('inf')
            for v in visited:
                for d in nodes:
                    new_distance = self.graph[s][v]+self.graph[v][d]
                    if new_distance < mid_distance and self.graph[v][d]!=0:
                        mid_distance=new_distance
                        self.graph[s][d]=new_distance 
                        k=d
                        pre=v
            distance[k]=mid_distance  
            nodes.remove(k) 
            visited.append(k)
             
            for i in range (self.V):
                dictionary[str(i)] = distance[i]
        return dictionary
    
    def Kruskal(self):
        
        result = {}
        val = sorted(self.dict)
        checked = [column for column in range(self.V)]  
        
        for i in val:
            for u,v in self.dict[i]:
                if checked[u] == checked[v]:
                    pass
                else:
                    checked = [checked[u]if x==checked[v] else x for x in checked]
                    result[str(u)+'-'+str(v)] = i
        return result
    

