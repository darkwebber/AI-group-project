import selection_mod as sm
import numpy as np
from generation_mod import Obj 
import test as t
file=open('mat.txt', 'r')
lines=file.readlines()
elms=[]
for line in lines:
    elms.append(list(map(int,line.split())))
mat=np.array(elms)
file.close()
vc=Obj(1)
lent=np.size(mat)
l=vc.minipath(mat,lent,30)
t.timSort(l, mat)
for i in l:
    print(i)