import numpy as np
import math
import mutation_mod as mp
from crossover_mod import cross_over
from crossover_mod import is_path
'''class Path_col:
    def __init__(self,L):
        self.list=L
    def fspread(self,a):
        return ((a**2)/(a-1))
    def stupidity(self,l):
        non_unique=list(set([i for i in l if l.count(i)!=1]))
        no_nonun=len(non_unique)
        spread_reps=list(map(self.fspread,list(map(l.count,non_unique))))
        return sum(spread_reps)+no_nonun
    def tot_mass(self):
        stu_inds=list(map(self.stupidity, self.list))
        return sum(stu_inds)
    def flex(self,l):
        flexi=self.stupidity(l)/self.tot_mass()
        return flexi
    def good_enough(self,part):
        prog=[]
        for i in self.list:
            if self.flex(i)<=part:
                prog.append(i)
        return prog'''
class Fit:
    def __init__(self,l):
        self.path=l
    def dist(self,mat,pos1,pos2):
        x1,y1=np.where(mat==pos1)
        x2,y2=np.where(mat==pos2)
        delx= x2[0]-x1[0]
        dely= y2[0]-y1[0]
        dis = (delx**2 + dely**2)**0.5
        return dis
    def span(self,mat):
        pos=self.path[0]
        test=[i for i in self.path if i!=pos]
        x= lambda posi : self.dist(mat,pos,posi)
        res=list(map(x,test))
        return sum(res)
    def leng(self,mat):
        temp=[]
        for i in range(len(self.path)-1):
            pos1=self.path[i]
            pos2=self.path[i+1]
            temp.append(self.dist(mat, pos1, pos2))
        return sum(temp)
    def fspread(self,a):
        return ((a**2)/(a-1))
    def stupidity(self):
        non_unique=list(set([i for i in self.path if self.path.count(i)!=1]))
        no_nonun=len(non_unique)
        spread_reps=list(map(self.fspread,list(map(self.path.count,non_unique))))
        return 5*(sum(spread_reps))+3*(no_nonun)
    def completeness(self,mat):
        tot= list(range(1,np.size(mat)+1))
        scr=0
        for i in tot:
            if i in self.path:
                scr+=1
        if scr==np.size(mat):
            return scr+int(scr/3)
        else:
            return scr
    def fit_cof(self,mat):
        fit_coeff=self.span(mat)/(self.leng(mat) * self.stupidity())
        return fit_coeff+(np.size(mat)*is_path(self.path, mat))+self.completeness(mat)
class Batch:
    def __init__(self,l):
        self.list=l
    def fit_enough(self,mat):
        lst=self.list
        tops=[]
        maxim=Fit(lst[0]).fit_cof(mat)
        maxl=Fit(lst[0])
        for i in lst:
            i=Fit(i)
            if i.fit_cof(mat)>maxim:
                maxim=i.fit_cof(mat)
                maxl=i
        return(maxl.path)
    def parents(self,mat):
        com=self.fit_enough(mat)
        fun= lambda l: (com,l)
        par=list(map(fun,self.list))
        return par
    def generation(self,mat,pars):
        dauts=list(map(cross_over,pars))
        i=0
        for tup in dauts:
            x,y=tup
            tup=(mp.mutate(x, mat),mp.mutate(y, mat))
            dauts[i]=tup
            i+=1
        return dauts

        
    