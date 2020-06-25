''' Function to plot the logistic map function for different lambda values
"f(x+1) = lamda*x*(1-x) Lambda: 0<lambda < 4
x : Valor inicial
maxNum : Cantidad max de generaciones, en tiempo
'''


import matplotlib.pyplot as plt

import numpy as np


def f(lamb,x,maxNum): 
    result = [] 

    for i in range(1,maxNum+1): 
        fnP1 = lamb*x*(1-x) 
        result.append(fnP1) 
        x = fnP1 
  
    return result 

x = np.linspace(0,3.9,400) 
y = [f(l,0.5,200) for l in x] 
x2 = [lamb[-150:] for lamb in y]
z = [[i]*150 for i in x] 
plt.figure(figsize=(10,6))
plt.scatter(z[:400],x2[:400],s=0.5)

plt.xlim(0,4)
plt.grid(True,ls=':',color='k')
plt.title(r'$X_{n+1}  =  \lambda   X_n (1-X_n)$', fontsize=20)


plt.xlabel(r'$\lambda$',fontsize=30)
plt.show()
