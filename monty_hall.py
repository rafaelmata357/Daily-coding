#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# PROGRAMMER   : Rafael Mata M.
# DATE CREATED :  20 June 2020                                 
# REVISED DATE :  1 july   2020
# PURPOSE: Test the probabilities using simulation of n cases for the monty hall game and demostrate that change the choice is the better option
#          
# 
# Command Line Arguments:
# 


# Imports python modules


import numpy as np
import collections

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
    juegos = int(input('Cantidad de juegos:'))
    espacio = choices(juegos)
    
    cambia_y_gana, no_cambia_y_gana, no_cambia = calculate_win(espacio)

    print('Cambia y gana: {} no hace caso y gana: {}'.format(cambia_y_gana,no_cambia_y_gana))
    print('No Hace caso:', no_cambia)
  



        

