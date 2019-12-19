
from collections import defaultdict 

class Graph:

    def __init__(self): 

        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        
        ans=[]
        temp=[s]
     

        
        while len(temp)>0 :
            
            out=temp.pop(0)
            ans.append(out)
            
            
            for i in self.graph[out]:
                if i not in ans:
                    temp.append(i)

                    
        return ans
                
                
                
    def DFS(self, s):
        
        ans=[]
        temp=[s]
      

        
        while len(temp)>0 :
            
            out=temp.pop(-1)
            ans.append(out)
            
            
            for i in self.graph[out]:
                if i not in ans:
                    temp.append(i)

                    
        return ans
                
        
