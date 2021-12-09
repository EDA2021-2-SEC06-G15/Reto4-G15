"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


airportsfile = 'airports-utf8-small.csv'
routesfile = 'routes-utf8-small.csv'
citiesfile = 'worldcities.csv'
initialStation = None

def printMenu():
    print("Bienvenido")
    print("1- Iniciar Analizador")
    print("2- Cargar información de la red de Transporte aéreo")
    print("3- Encontrar puntos de interconexión aérea")
    print("4- Encontrar clústeres de tráfico aéreo")
    print("5- Encontrar la ruta más corta entre ciudades")
    print("6- Utilizar las millas de viajero")
    print("7- Cuantificar el efecto de un aeropuerto cerrado")
    print("8- Comparar con servicio WEB externo")


def optionTwo(cont):
    print("\nCargando información de transporte aéreo ....")
    
    controller.loadRoutes(cont, airportsfile, routesfile)
    controller.loadAirports(cont, airportsfile)
    controller.loadCities(cont, citiesfile)
    controller.loadNames(cont, airportsfile)
    
def optionThree(analyzer):
    controller.puntosInterconexion(analyzer)

def optionFour(cont, verta, vertb):
    controller.clusteres(cont, verta, vertb)

def optionFive(cont, verta,vertb):
    controller.caminoMasCorto(cont, verta,vertb)

    


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        optionTwo(cont)

    elif int(inputs[0]) == 3:
        print("Encontrando puntos de interconexión aérea ....")
        optionThree(cont)

    elif int(inputs[0]) == 4:
        verta = input("Ingrese el codigo IATA 1: ")
        vertb = input("Ingrese el codigo IATA 2: ")
        optionFour(cont, verta, vertb)

    elif int(inputs[0]) == 5:
        verta = input("Ingrese la ciudad de origen: ")
        vertb = input("Ingrese la ciudad de destino: ")
        optionFive(cont, verta,vertb)

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    elif int(inputs[0]) == 8:
        pass

    else:
        sys.exit(0)
sys.exit(0)
