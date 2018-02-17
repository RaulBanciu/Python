'''
Created on Mar 15, 2017

@author: Raul
'''
from define import DoubleDictGraph

class defineFile(DoubleDictGraph):
    '''
    classdocs
    '''

    def __init__(self, fileName="D:\\projects\\grafuri\\src\\test.txt"):
        f=open(fileName,"r")
        line = f.readline().strip()
        attrs = line.split(" ")
        n=int(attrs[0])
        f.close()
        DoubleDictGraph.__init__(self,n)
        self.__fName = fileName
        self.__loadFromFile()
        
    def __loadFromFile(self):
        f = open(self.__fName, "r")
        line = f.readline().strip()
        line = f.readline().strip()
        while line != "":
            attrs = line.split(" ")
            DoubleDictGraph.addEdge(self, int(attrs[0]),int(attrs[1]),int(attrs[2]))
            line = f.readline().strip()
        f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        l=DoubleDictGraph.parseNout(self,DoubleDictGraph.parseX(self))
        for i in l:
            for j in DoubleDictGraph.parseNout(self, l):
                if(j!=[-1]):
                    strf =str(repr(i) + " " + repr(j +  " " + repr(DoubleDictGraph.isEdge(self, i, j))))
                    f.write(strf)
        f.close()
    
    def addVertex(self, x):
        DoubleDictGraph.addVertex(self, x)
        'self.__storeToFile()'
        
    def addEdge(self, x, y, cost):
        DoubleDictGraph.addEdge(self, x, y, cost)
        self.__storeToFile()
    '''
    def remove(self, bookid):
        BookRepository.remove(self, bookid)
        self.__storeToFile()        
    
    def update(self, bookid,booktitle,bookdesc,bookgen):
        BookRepository.update(self, bookid, booktitle, bookdesc, bookgen)
        self.__storeToFile()
    '''
    