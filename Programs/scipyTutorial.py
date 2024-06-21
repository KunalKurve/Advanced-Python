from scipy.special import cbrt,comb,perm
x=cbrt([27,64])
print(type(x))
print(x)
print()
print(perm(6,2))
print(comb(6,2))


import numpy as np
from scipy import linalg
m=np.array([[10,20],[30,40]])
print(linalg.det(m))

eig_val,eig_vect=linalg.eig(m)
print(eig_val,eig_vect)
print(eig_vect.dtype)


from scipy import stats
m=np.array([[22,23,14,22,56],[22,46,23,14,14]])
modeval=stats.mode(m,axis=1)
print(modeval)

