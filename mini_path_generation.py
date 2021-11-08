import random
import numpy as np
import generation_mod as gm
import selection_mod as sm
from crossover_mod import is_path
import test
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
c_prob=float(input("Enter number of cross-over probability"))
m_prob=float(input("Enter mutation probability"))
lent=np.size(mat)
vc=gm.Obj(random.randrange(1,lent+1))
l=vc.minipath(mat,lent,gen_size)
print(mat)
print(vc.pos)
print(vc.nbour(mat))
L=sm.Batch(l)
i=1
val=sm.Fit(L.fit_enough(mat)).fit_cof(mat)
print(val)
while val<2*np.size(mat):
    col=[]
    print(i)
    for pairs in L.generation(mat,L.list,c_prob,m_prob):
        x,y=pairs
        col.append(x)
        col.append(y)
    test.timSort(col,mat)
    col=col[:gen_size]
    L=sm.Batch(col)
    val=sm.Fit(L.fit_enough(mat)).fit_cof(mat)
    print(val)
    i+=1
print(L.fit_enough(mat))
print(sm.Fit(L.fit_enough(mat)).fit_cof(mat))
