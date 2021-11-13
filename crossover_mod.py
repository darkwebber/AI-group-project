import random
import generation_mod as gm
def cross_over(par_tup):
    ran1=len(par_tup[0])
    c_point1=random.randint(1, ran1-1)
    ran2=len(par_tup[1])
    c_point2=random.randint(1, ran2-1)
    p1=par_tup[0]
    p2=par_tup[1]
    d1=p1[:c_point1]+p2[c_point2:]
    d2=p2[:c_point2]+p1[c_point1:]
    return (d1,d2)
def is_path(l,mat):
    for j in range(len(l)-1):
        test_obj=gm.Obj(l[j])
        if l[j+1] not in test_obj.nbour(mat):
            return False
    return True

