#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# PROGRAMMER   : Rafael Mata M.
# DATE CREATED :  20 June 2020                                 
# REVISED DATE :  5 july   2020
# PURPOSE: Test the probabilities using simulation of n cases for the monty hall game and demostrate that change the choice is the better option
#          
# 
# Command Line Arguments:
# 


# Imports python modules


import numpy as np
import collections
import matplotlib.pyplot as plt
import argparse

def get_args():
    '''
    Retrieves and parses two command line arguments provided by the user from 
    command line. argparse module is used. 
    If some arguments is missing default value is used. 
    Command Line Arguments:
    
    Args:
        1. Games to simulate                           --games
    
   
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    '''
    
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser('monty_hall.py',description='Monty hall game simulations', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
       
    # Argument 1: Initial x value for the function 
    parser.add_argument('--games', type = int, default= 100,
                    help = 'Number of games')  
    
    return parser.parse_args()


def choices(nsimulaciones):
    premios = np.array([['a','v','v'],['v','a','v'],['v','v','a']])
    espacio = []
    for i in range(nsimulaciones):
        p = premios[np.random.randint(0,3),:]
        espacio.append(p)
    return espacio


def calculate_win(espacio):
    
    
    no_cambia_y_gana = 0
    pierde = 0
    cambia_y_gana = 0
    no_cambia = dict()
    cambia = dict()
    elegido = []
  
    
    for opciones in espacio:
        puertas = [0,1,2]
        eleccion = np.random.randint(0,3)
        premio_elegido = opciones[eleccion]
        puertas.pop(eleccion)
        if opciones[puertas[0]] == 'v':      #Eliminar una puerta sin premio
            premio_restante = opciones[puertas[1]]
        else:
            premio_restante = opciones[puertas[0]]
        
        cambiar = np.random.randint(0,2)
        elegido.append(premio_elegido)
     

        #print('Premio elegido: {} Premio restante: {}  Cambia: {}'.format(premio_elegido, premio_restante, cambiar))
         
        if cambiar and premio_restante == 'a':
            cambia_y_gana += 1
        elif (premio_elegido == 'a') and (cambiar == 0):
            no_cambia_y_gana += 1
        
        no_cambia = collections.Counter(elegido)
       
  
    return cambia_y_gana, no_cambia_y_gana, no_cambia


if __name__ == '__main__':
  

    in_arg = get_args()               #Get variables from command line
    juegos = in_arg.games           #Number of games to simulate
    espacio = choices(juegos)
    
    cambia_y_gana, no_cambia_y_gana, no_cambia = calculate_win(espacio)
    
    opacity = 0.5
    bar_width = 0.6
    bar_chart = plt.bar(['Change & Win','Stay & Lost'],[no_cambia['v'],no_cambia['a']],align='center', width=bar_width, alpha=opacity, color='g')
    plt.title('Monty hall results for {} games'.format(juegos),fontsize=15)
    plt.ylabel('Number of games')
   
    prob_win = no_cambia['v']/juegos*100

    for rect in bar_chart:    # To add the probabilty for each bar
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height//2, '{:.2f}%'.format(height/juegos*100), ha='center', va='bottom')

    #plt.text(0,no_cambia['v']//2,'{:.2f}%'.format(prob_win))
    #plt.text(1,no_cambia['a']//2,'{:.2f}%'.format(100-prob_win))

    plt.tight_layout()

   
    plt.show()



        

