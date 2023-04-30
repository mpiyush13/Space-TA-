from collections import defaultdict
 
class Graph():
    def __init__(self,lis):
        self.g = defaultdict(list)
        self.s={}
        self.s=set()
        for t in lis:
            self.s.add(t[0])
        self.V = len(self.s)
 
    def addEdge(self,lis):
        for t in lis:
            self.g[t[0]].append(t[1])
    def checkcycle(self):
        v=[]
        s=[]
        for i in range(self.V):
            v.append(False)
            s.append(False)
        for i in range(self.V):
            if v[i] == False:
                if self.helpcheckcycle(i,v,s) == True:
                    return True
        return False
    
    def helpcheckcycle(self, v, vlist, rstack):
        vlist[v] = True
        rstack[v] = True
        for n in self.g[v]:
            if vlist[n] == False:
                if self.helpcheckcycle(n, vlist, rstack) == True:
                    return True
            elif rstack[n] == True:
                return True
        rstack[v] = False
        return False
listt=[(0, 1),(0, 2),(1, 2),(2, 0),(2, 3),(3, 3)]
g = Graph(listt)
g.addEdge(listt)
if g.checkcycle() == 1:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")
