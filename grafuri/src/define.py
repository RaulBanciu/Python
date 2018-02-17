'''
Created on Mar 1, 2017

@author: Raul
'''

class DoubleDictGraph:
    """A directed graph, represented as two maps,
    one from each vertex to the set of outbound neighbours,
    the other from each vertex to the set of inbound neighbours"""

    def __init__(self,n):
        """Creates a graph with n vertices
        and no edges"""
        self._dictOut={}
        self._dictIn = {}
        self._cost={}
        for i in range(1,n):
            self._dictOut[i]=[0]
            self._dictIn[i] = [0]
         
    def validateOut(self,x):
        if x in range(len((self._dictOut))):
            if(-1 ==self._dictOut[x][0]):
                return False
        else:
            return False
        
        return True
        
    def validateIn(self,x):  
        if(x in self._dictIn):
            if(-1 ==self._dictIn[x][0]):
                return False
        else:
            return False
        
        return True
           
         
    def numberOfVertices(self):
        nr=0
        for i in range(1,len(self._dictOut)+1):
            print(len(self._dictOut))
            if(-1!= self._dictOut[i][0]):
                nr+=1
        return nr
    
    def addVertex(self,x):
        if(x in self._dictOut):
            if(self._dictOut[x][0]==-1):
                self._dictOut[x][0]=0
                return 1
            else:
                return -1
        else:
            if(x>0):
                for j in range(len(self._dictOut)+1,x):
                    self._dictOut.update({j:[-1]})
                    self._dictIn.update({j:[-1]})
                self._dictOut.update({x:[0]})
                self._dictIn.update({x:[0]})
                print(self._dictOut)
                return 1
            else:
                return -1
            
            
    def removeVertex(self,x):
        if(x in self._dictOut):
            self._dictOut[x]=-1
            
        
            
                            
    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self._dictOut.keys()

    def parseNout(self,x):
        """Returns an iterable containing the outbound neighbours of x"""
        if(self.validateOut(x)):
            return self._dictOut[x]
        return -1

    def parseNin(self,x):
        """Returns an iterable containing the inbound neighbours of x"""
        if(self.validateIn(x)):
            return self._dictIn[x]
        return -1  

    def isEdge(self,x,y):
        '''returns True if there is edge between x and y
        checks if x and y are vertices, if they aren't return -1'''
        if(self.validateOut(x)==False and self.validateOut(x)==False):
            return -1
        
        z=(x,y)
        if z in self._cost:
            return self._cost[z]
        
        return -1
        
        
    def addEdge(self,x,y,cost):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""
        if(self.validateOut(x)==False and self.validateOut(y)==False):
            return -1
        
        if(y in self._dictOut[x]):
            return -1
        
        if(self._dictOut[x][0]==0 or self._dictOut[x][0]==-1):
            self._dictOut[x][0]=y
        else:
            self._dictOut[x].append(y)
            
        if(self._dictIn[y][0]==0 or self._dictIn[y][0]==-1):
            self._dictIn[y][0]=x
        else:
            self._dictIn[y].append(x)
            
        self._cost[x,y]=cost
        print(x,y,cost)
        return 1
        
    def vertOutDegree(self,x):
        '''returns the out degree of vertex x
            if there is no such vertex, returns -1
            if it is isolated, returns 0'''
        if(self.validateOut(x)==False):
            return -1
        
        if self._dictOut[x][0]==0:
            return 0
        
        return len(self._dictOut[x])
    
    def vertInDegree(self,x):
        '''returns the in degree of vertex x
            if there is no such vertex, returns -1
            if it is isolated, returns 0'''
        if(self.validateIn(x)==False):
            return -1
        
        if self._dictOut[x][0]==0:
            return 0
        
        return len(self._dictIn[x])
    
    def iterateOutDegree(self,x):
        '''return -1 if the vertices does not exist
           return 0 if the vertice is isolated
           else return every out vertex with their cost
        '''
        
        if(self.validateOut(x)==False):
            return -1
        
        if self._dictOut[x][0]==0:
            return 0;
        
        l=[]
        
        for i in range(0,len(self._dictOut[x])):
            z=(x,self._dictOut[x][i])
            l.append([self._dictOut[x][i],self._cost[z]])
            
        return l
    
    def iterateInDegree(self,x):
        '''return -1 if the vertices does not exist
           return 0 if the vertice is isolated
           else return every out vertex with their cost
        '''
        if(self.validateIn(x)==False):
            return -1
        
        if self._dictIn[x][0]==0:
            return 0
        
        
        l=[]
        
        for i in range(0,len(self._dictIn[x])):
            z=(self._dictIn[x][i],x)
            l.append([self._dictIn[x][i],self._cost[z]])
            
        return l

    #def modify(self,x):
        
