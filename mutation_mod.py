import random
import generation_mod as gm
def mutate(l,mat):
    b_point=random.randint(0, len(l)-1)
    t_obj1=gm.Obj(l[b_point-1])
    if b_point!=len(l)-1:
        t_obj2=gm.Obj(l[b_point+1])
    else:
        t_obj2=t_obj1
    nl1=t_obj1.nbour(mat)
    nl2=t_obj2.nbour(mat)
    pmut=[i for i in nl1 if ((i in nl2) and i!=l[b_point])]
    if pmut==[]:
        return l
    l[b_point]=random.choice(pmut)
    return l