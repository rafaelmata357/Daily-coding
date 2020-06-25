''' Function to plot the logistic map function for different lambda values
"f(x+1) = lamda*x*(1-x) Lambda: 0<lambda < 4
x : Valor inicial
maxNum : Cantidad max de generaciones, en tiempo
'''


import matplotlib.pyplot as plt

import numpy as np
import matplotlib.ticker as ticker


def log_function(lamb,x,maxNum): 
    result = [] 

    for i in range(1,maxNum+1): 
        fnP1 = lamb*x*(1-x) 
        result.append(fnP1) 
        x = fnP1 
  
    return result 

def graph(x,y):
    ''' Function to graph the log_function
    Params:
          x: list with the lambda values for each iteration
          y: the log_function output

    returns:
           None
    '''

    plt.figure(figsize=(10,6))
    plt.scatter(x[:400], y[:400],s=0.1)
    tick_major = 0.2
    tick_minor = 0.1
    plt.xlim(0,4.1)
    plt.grid(True,ls=':',color='k')
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(tick_major)) 
    plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(tick_minor))
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.1)) 
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
    #plt.xticks(np.arange(0,4.2,0.2))
    plt.title('Logistic Map Function: ' + r'$X_{n+1}  =  \lambda   X_n (1-X_n)$', fontsize=18,c='b')
    plt.xlabel(r'$\lambda$',fontsize=30,c='b')
    plt.show()


if __name__ == '__main__':  

    x = np.linspace(0,4,400) 
    y = [log_function(l,0.5,200) for l in x] 
    x2 = [lamb[-150:] for lamb in y]
    z = [[i]*150 for i in x] 
    graph(z, x2)
