import random
import generation_mod as gm
def cross_over(par_tup):
    ran=len(par_tup[0])
    c_point=random.randint(0, ran-1)
    p1=par_tup[0]
    p2=par_tup[1]
    d1=p1[:c_point]+p2[c_point:]
    d2=p2[:c_point]+p1[c_point:]
    return (d1,d2)
def is_path(l,mat):
    for j in range(len(l)-1):
        test_obj=gm.Obj(l[j])
        if l[j+1] in test_obj.nbour(mat):
            return True
        else:
            return False

