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
from DISClib.ADT import orderedmap as om
from DISClib.ADT import map as m


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
citiesfile = 'worldcities-utf8.csv'
initialStation = None

def printMenu():
    print("\n//////////")
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
    
    controller.loadRoutes(cont, airportsfile, routesfile) #Grafo
    controller.loadAirports(cont, airportsfile) #Árbol Codigo IATA
    controller.loadCities(cont, citiesfile) #Árbol Tipos de Ciudades
    controller.loadNames(cont, airportsfile) #Árbol Nombre de la Ciudad

    grafo = cont['airports']
    llavesgrafo = om.keySet(grafo)
    first = om.get(grafo, lt.firstElement(llavesgrafo))
    last = om.get(grafo, lt.lastElement(llavesgrafo))
    
    aiatai = first["key"]
    nombrei = first["value"]["Name"]
    ciudadi = first["value"]["City"]
    paisi = first["value"]["Country"]
    latitudi = first["value"]["Latitude"]
    longitudi = first["value"]["Longitude"]

    aiataf = last["key"]
    nombref = last["value"]["Name"]
    ciudadf = last["value"]["City"]
    paisf = last["value"]["Country"]
    latitudf = last["value"]["Latitude"]
    longitudf = last["value"]["Longitude"]

    print("\nPrimer aeropuerto cargado")
    print("\nAeropuerto " + str(nombrei) +" (" + str(aiatai) + ").")
    print("Ubicación: " + str(ciudadi) + ", " + str(paisi) + ".")
    print("Latitud: " + str(latitudi) + ", Longitud" + str(longitudi) + ".")
    print("\nUltimo aeropuerto cargado")
    print("\nAeropuerto " + str(nombref) +" (" + str(aiataf) + ").")
    print("Ubicación: " + str(ciudadf) + ", " + str(paisf) + ".")
    print("Latitud: " + str(latitudf) + ", Longitud" + str(longitudf) + ".")

    grafo = cont['cities']
    llavesgrafo = om.keySet(grafo)
    first = om.get(grafo, lt.firstElement(llavesgrafo))
    last = om.get(grafo, lt.lastElement(llavesgrafo))

    ciudadi = first["value"]["city"]
    paisi = first["value"]["country"]
    latitudi = first["value"]["lat"]
    longitudi = first["value"]["lng"]
    poblacioni = first["value"]["population"]

    ciudadf = last["value"]["city"]
    paisf = last["value"]["country"]
    latitudf = last["value"]["lat"]
    longitudf = last["value"]["lng"]
    poblacionf = last["value"]["population"]

    print("\nPrimera ciudad cargada")
    print(str(ciudadi) + ", " + str(paisi) + ".")
    print("Latitud: " + str(latitudi) + ", Longitud" + str(longitudi) + ".")
    print("Población: " + str(poblacioni))
    print("\nUltima ciudad cargada")
    print(str(ciudadf) + ", " + str(paisf) + ".")
    print("Latitud: " + str(latitudf) + ", Longitud" + str(longitudf) + ".")
    print("Población: " + str(poblacionf))


    
def optionThree(analyzer):
    controller.puntosInterconexion(analyzer)

def optionFour(cont, verta, vertb):
    controller.clusteres(cont, verta, vertb)

def optionFive(cont, verta,vertb):
    controller.caminoMasCorto(cont, verta,vertb)

def optionSix(cont, city, km):
    controller.Millas(cont, city, km)

def optionSeven(cont, aeropuerto):
    controller.cerrado(cont, aeropuerto)




    


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
        city = input("Ingrese la ciudad de origen: ")
        millas = input("Ingrese la cantidad de millas disponibles: ")
        km = float(millas)*1.60
        optionSix(cont, city, km)

    elif int(inputs[0]) == 7:
        aeropuerto = input("Ingrese el codigo IATA: ")
        optionSeven(cont, aeropuerto)

    elif int(inputs[0]) == 8:
        pass

    else:
        sys.exit(0)
sys.exit(0)
