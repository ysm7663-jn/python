uniqe_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

N = input()

for i in uniqe_list :
    N = N.replace(i, '*')
    
"""
ddz=z=

ddz=z=
ddz=z=
d*z=  
d*z=  
d*z=  
d*z=  
d*z=  
d**
"""
print(len(N)) 