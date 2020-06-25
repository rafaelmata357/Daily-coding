''' Function to plot the logistic map function for different lambda values
"f(x+1) = lamda*x*(1-x) Lambda: 0<lambda < 4
x : Valor inicial
maxNum : Cantidad max de generaciones, en tiempo
'''


import matplotlib.pyplot as plt

import numpy as np
import matplotlib.ticker as ticker


import os
import argparse


# 
def get_args():
    '''
    Retrieves and parses two command line arguments provided by the user from 
    command line. argparse module is used. 
    If some arguments is missing default value is used. 
    Command Line Arguments:
    
    Args:
        1. Initial x value                           --initial_x
        2. Iterations for each lambda value          --iter
        3. Steps for lambda range 0 <= lambda <= 4   --steps
   
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    '''
    
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser('logistic_map_function.py',description='Graph logistic map function', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
       
    # Argument 1: Initial x value for the function 
    parser.add_argument('--initial_x', type = float, default= 0.1,
                    help = 'Inital x value')  
    
    # Argument 2: Y axis scale to use
    parser.add_argument('--iter', type = int, default = 200 ,
                    help = 'Iteration for each lambda value')   

    # Argument 3: Number of steps to divide the lambda value from  0 to 4
    parser.add_argument('--steps', type = int, default = 400 ,
                    help = 'Iteration for each lambda value')  
    
   

    return parser.parse_args()


def log_function(lamb,x,maxNum): 
    result = [] 

    for i in range(1,maxNum+1): 
        fnP1 = lamb*x*(1-x) 
        result.append(fnP1) 
        x = fnP1 
  
    return result 

def compute_results(initial_x, steps, iterations):
    '''Fuction to compute the logistic function results
    
    Parameters:
            lamb: start value for the logistic function
    
    Returns:
           x: array for each lambda value used
           y: array with the output values for each lambda evaluated

    '''

    x = np.linspace(0, 4, steps) 
    y = [log_function(l, initial_x, iterations) for l in x] 
    y2 = [lamb[-50:] for lamb in y]
    z = [[i]*50 for i in x] 

    return z, y2

                    


def graph(x,y):
    ''' Function to graph the log_function
    Params:
          x: list with the lambda values for each iteration
          y: the log_function output

    returns:
           None
    '''

    plt.figure(figsize=(10,6))
    plt.scatter(x, y,s=0.1)
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

    in_arg = get_args()               #Get variables from command line
    initial_x = in_arg.initial_x      #Initial value to feed the logistica map function
    iterations = in_arg.iter          #Number of iterations for each lambda value
    steps = in_arg.steps              #Lambda steps evaluation 0 <= lambda <= 4
      
    x, y = compute_results(initial_x, steps, iterations)
    graph(x, y)
