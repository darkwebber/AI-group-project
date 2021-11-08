import numpy as np
import random
class Obj:
    def __init__(self,pos):
        self.pos=pos
    def nbour(self,mat):
        tup = np.where(mat == self.pos)
        nlist=[]
        for i in range(2):
            nlist.append(list(tup[i]))
        nil=[]
        for i in range(2):
            nil.append(int(nlist[i][0]))
        nlist=[]
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                X=nil[0]+i
                Y=nil[1]+j
                if X>=0 and Y>=0 and X<np.shape(mat)[0] and Y<np.shape(mat)[1] and [X,Y]!=nil :
                    nlist.append(mat[X][Y])
        return nlist
    def cord(self,mat):
        tup = np.where(mat == self.pos)
        nlist=[]
        for i in range(2):
            nlist.append(list(tup[i]))
        nil=[]
        for i in range(2):
            nil.append(int(nlist[i][0]))
        return nil
    def mpath(self,mat,lent,mini=[],i=0):
            if i==0:
                mini.append(self.pos)
                #print(f'func {mini} ini')
            if self.cord(mat)[0]==0 or self.cord(mat)[1] == 0 or self.cord(mat)[1]==np.shape(mat)[1]-1 or self.cord(mat)[0]==np.shape(mat)[0]-1:
                if i<lent:
                    k=random.choice(self.nbour(mat))
                    self=Obj(k)
                    mini.append(k)
                    return self.mpath(mat,lent , mini,i+1)
                if i==lent:
                    self=Obj(mini[0])
                    return mini
                if i>lent:
                    self=Obj(mini[0])
                    return mini
            #print(f'func {mini} fini')
            mini.append(random.choice(self.nbour(mat)))
            #print(f'func {mini} inipini')
            self=Obj(mini[len(mini)-1])
            return self.mpath(mat,lent,mini,i+1)
    def minipath(self,mat,lent,gen_size):
        minipaths=[]
        open('minipaths_gen1.txt','w').close()
        f=open('minipaths_gen1.txt','a')
        i=0
        while i<gen_size:
            p=self.mpath(mat,lent,[])
            if p!=None and minipaths.count(p)==0:
                i+=1
                minipaths.append(p)
                f.write(str(p)+"\n")
        f.close()
        return minipaths

