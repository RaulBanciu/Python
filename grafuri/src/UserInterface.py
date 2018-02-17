'''
Created on Mar 15, 2017

@author: Raul
'''

class UI:
    '''
    classdocs
    '''


    def __init__(self, ctrl):
        '''
        Constructor
        '''
        self._ctrl=ctrl
        
    def numberVertices(self):
        
        x=self._ctrl.numberOfVertices()
        if(x==0):
            print("There are no vertices!")
        else:
            print("the number of vertices is ",repr(x))
            
    def edgeBetween(self):
        x=int(input("Please enter the first vertex: "))
        y=int(input("Please enter the second vertex: "))
        z=self._ctrl.isEdge(x,y)
        if z==-1:
            print("There is no edge between " +repr(x)+" and "+ repr(y))
        else:
            print("There is an edge between " +repr(x)+" and "+ repr(y))
    
    def inAndOut(self):
        x=int(input("Please enter the vertex "))
        y=self._ctrl.vertOutDegree(x)
        z=self._ctrl.vertInDegree(x)
        if y==-1:
            print("The vertex does not exist")
        elif(y==0):
            print("No outbound edges")
        else:
            print("The outdegree is ",repr(y))
        if z==0:
            print("No inbound edges")
        else:
            print("The indegree is ",repr(z))
    
    def iterateOut(self):
        x=int(input("Please enter the vertex "))
        z=self._ctrl.iterateOutDegree(x)
        if z==-1:
            print("The vertex does not exist")
        elif(z==0):
            print("No outbound edges")
        else:
            for i in range(0,len(z)):
                print("Edge "+repr(x)+" "+repr(z[i][0])+" with cost "+repr(z[i][1]))
    
    #problem 3
    
    def addEdge(self):
        x=int(input("Please enter the 1st vertex "))
        y=int(input("Please enter the 2nd vertex "))
        z=int(input("Please enter the cost  "))
        self._ctrl.addEdge(x,y,z)
    
    def addVert(self):
        x=int(input("Please enter the vertex "))
        self._ctrl.addVertex(x)
    
    def iterateIn(self):
        x=int(input("Please enter the vertex "))
        z=self._ctrl.iterateInDegree(x)
        if z==-1:
            print("The vertex does not exist")
        elif(z==0):
            print("No inbound edges")
        else:
            for i in range(0,len(z)):
                print("Edge "+repr(z[i][0])+" "+repr(x)+" with cost "+repr(z[i][1]))
                
    def menu(self):
        while True:
            cmds={"1":self.numberVertices,"2":self.edgeBetween,"3":self.inAndOut,"4":self.iterateOut,"5":self.iterateIn,"6":self.addVert,"7":self.addEdge}
            com=["1","2","3","4","5","6","7"]
            print("1-Number of vertices\n","2-Is edge between\n","3-In and out degree\n","4-Iterate out\n","5-Iterate in\n")
            cmd=input("Enter command: ")
            if cmd in com:
                if cmd=="0":
                    print("Thanks for using my app!")
                    return
                else:
                    cmds[cmd]()
            else:
                print("Invalid command!\n")