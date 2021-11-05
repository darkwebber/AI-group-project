import random
import numpy as np
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
def mpath(obj,mat,lent,mini=[],i=0):
        if i==0:
            mini.append(obj.pos)
            #print(f'func {mini} ini')
        if obj.cord(mat)[0]==0 or obj.cord(mat)[1] == 0 or obj.cord(mat)[1]==np.shape(mat)[1]-1 or obj.cord(mat)[0]==np.shape(mat)[0]-1:
            if i<lent:
                k=random.choice(obj.nbour(mat))
                obj=Obj(k)
                mini.append(k)
                return mpath(obj, mat,lent , mini,i+1)
            if i==lent:
                obj=Obj(mini[0])
                return mini
            if i>lent:
                obj=Obj(mini[0])
                return None
        #print(f'func {mini} fini')
        mini.append(random.choice(obj.nbour(mat)))
        #print(f'func {mini} inipini')
        obj=Obj(mini[len(mini)-1])
        return mpath(obj,mat,lent,mini,i+1)
def minipath(obj,mat,lent,gen_size):
    minipaths=[]
    open('minipaths_gen1.txt','w').close()
    f=open('minipaths_gen1.txt','a')
    i=0
    while i<gen_size:
        p=mpath(obj,mat,lent,[])
        if p!=None:
            i+=1
            minipaths.append(p)
            f.write(str(p)+"\n")
    f.close()
    return minipaths

file=open('mat.txt', 'r')
lines=file.readlines()
elms=[]
for line in lines:
    elms.append(list(map(int,line.split())))
mat=np.array(elms)
file.close()
#if mat[x][y] is our location then
    #mat[X=x+-1][Y=y+-1] for all X,Y>=0 and X<l and Y<b
gen_size=int(input("Enter the gen size"))
lent=int(input("Length of path"))
vc=Obj(random.randrange(1,51))
l=minipath(vc,mat,lent,gen_size)
print(mat)
print(vc.pos)
print(vc.nbour(mat))