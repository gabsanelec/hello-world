'''
Created on Aug 14, 2019

@author: gabriel.santamaria
'''
from builtins import *
from _ast import If

class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    def arrancar(self):
        #pass
        self.enmarcha = True
        
    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
   
    
miCoche = Coche() #INstanciar, ejemplarizar una clase

print("El largo de mi coche es:",miCoche.largoChasis)
print("Mi coche tiene:",miCoche.ruedas,"ruedas")

miCoche.arrancar()

#print(miCoche.estado())