"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Graphs import scc
from DISClib.ADT import queue as q
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

   airports: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre aeropuertos
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
                    'airports': None,
                    'connections': None,
                    'cities': None,
                    'names': None,
                    'components': None,
                    'paths': None
                    }

        analyzer['airports'] = om.newMap(omaptype='BST')
        analyzer['cities'] = om.newMap(omaptype='BST')
        analyzer['names'] = om.newMap(omaptype='BST')
        analyzer['connections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareIATA)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')

# Funciones para agregar informacion al catalogo



def addCity(analyzer, city):
    updateCity(analyzer['cities'], city)
    return analyzer

def updateCity(map, city):
    """
    Se toma la ciudad y se busca si ya existe en el arbol dicha 
    ciudad. Si no se encuentra creado un nodo para esa ciudad 
    en el arbol se crea y se actualiza el indice de datos de la ciudad
    """
    occurredcity = city['city_ascii']
    entry = om.get(map, occurredcity)
        
    if entry is None:
        cityentry = city
        om.put(map, occurredcity, cityentry)
    else:
        pass
    return map


def addAirport(analyzer, city):
    updateAirport(analyzer['airports'], city)
    return analyzer

def updateAirport(map, airport):
    """
    Se toma el aeropuerto y se busca si ya existe en el arbol dicha 
    ciudad. Si no se encuentra creado un nodo para esa ciudad 
    en el arbol se crea y se actualiza el indice de datos de la ciudad
    """
    occurredcity = airport['IATA']
    entry = om.get(map, occurredcity)
        
    if entry is None:
        cityentry = airport
        om.put(map, occurredcity, cityentry)
    else:
        pass
    
    return map

def addName(analyzer, city):
    updateName(analyzer['names'], city)
    return analyzer

def updateName(map, airport):
    """
    Se toma el aeropuerto y se busca si ya existe en el arbol dicha 
    ciudad. Si no se encuentra creado un nodo para esa ciudad 
    en el arbol se crea y se actualiza el indice de datos de la ciudad
    """
    occurredcity = airport['City']
    entry = om.get(map, occurredcity)
        
    if entry is None:
        cityentry = airport
        om.put(map, occurredcity, cityentry)
    else:
        pass
    
    return map







    
    


# Funciones para creacion de datos

# Funciones de consulta

def puntosInterconexion(cont):
    vertices = gr.vertices(cont['connections'])  
    
    aeropuerto = None
    
    x = 1
    n = 0

    while x <= 5:
        mayor = 0
        for v in lt.iterator(vertices):
            if v is not None:
                grado = float(gr.degree(cont['connections'],v))
            if grado > mayor:
                mayor = grado
                aeropuerto = v
                o  = gr.outdegree(cont['connections'], aeropuerto)
                i = gr.indegree(cont['connections'], aeropuerto)
                n = i + o
                

                
        pos = lt.isPresent(vertices, aeropuerto)
        lt.deleteElement(vertices, pos)
        airport = om.get(cont['airports'], aeropuerto)
        nombre = airport["value"]["Name"]
        ciudad = airport["value"]["City"]
        pais = airport["value"]["Country"]

        x +=1 
        print("\nEl aeropuerto " + str(nombre) +"(" + str(aeropuerto) + ")" + ". Tiene " + str (n) + " conexiones.")
        print("Ubicación: " + str(ciudad) + ", " + str(pais) + ".")
        print("Conexiones de entrada: " + str(i))
        print("Conexiones de salida: " + str(o))
    

def connectedComponents(analyzer):
    """
    Calcula los componentes conectados del grafo
    Se utiliza el algoritmo de Kosaraju
    """
    analyzer['components'] = scc.KosarajuSCC(analyzer['connections'])
    ans = scc.connectedComponents(analyzer['components'])
    
    print("\nEl número de elementos conectados o clusters es de: " + str(ans))
    return ans

def clusteres(analyzer, verta, vertb):

    connectedComponents(analyzer)

    sccc = analyzer['components']
    ans = scc.stronglyConnected(sccc, verta, vertb)

    airport = om.get(analyzer['airports'], verta)
    nombre = airport["value"]["Name"]
    ciudad = airport["value"]["City"]
    pais = airport["value"]["Country"]

    print("\nAEROPUERTOS INGRESADOS: ")
    print("\nNombre: " + str(nombre))
    print("Codigo IATA: " + str(verta))
    print("Ciudad: " + str(ciudad))
    print("Pais: " + str(pais))

    airport = om.get(analyzer['airports'], vertb)
    nombre = airport["value"]["Name"]
    ciudad = airport["value"]["City"]
    pais = airport["value"]["Country"]

    print("\nNombre: " + str(nombre))
    print("Codigo IATA: " + str(vertb))
    print("Ciudad: " + str(ciudad))
    print("Pais: " + str(pais))

    if ans == True:
        print("\nLos aeropuertos ingresados están fuertemente conectados.")

    else:
        print("\nlos aeropuertos ingresados NO están fuertemente conectados.")
    print("\n")


def caminoMasCorto(cont, verta, vertb):
    
    IATA1 = findIATA(cont, verta)
    IATA2 = findIATA(cont, vertb)
            
    cont['paths'] = djk.Dijkstra(cont['connections'], IATA1)
    path = djk.pathTo(cont['paths'], IATA2)
    trayecto = lt.newList()
    
    size = q.size(path)
    i=0
    distancia = 0
    print("\nLos aeropuertos presentes en el recorrido son los siguientes: ")
    while i < size:
        elm = q.dequeue(path)
        distancia += float(elm['weight'])        
        
        iata = elm['vertexA']
        lt.addLast(trayecto, iata)
        airport = om.get(cont['airports'], iata)
        nombre = airport["value"]["Name"]
        ciudad = airport["value"]["City"]
        pais = airport["value"]["Country"]

        print("\nNombre: " + str(nombre))
        print("Codigo IATA: " + str(iata))
        print("Ciudad: " + str(ciudad))
        print("Pais: " + str(pais))
        i+=1

    iata = IATA2
    lt.addLast(trayecto, iata)
    airport = om.get(cont['airports'], iata)
    nombre = airport["value"]["Name"]
    ciudad = airport["value"]["City"]
    pais = airport["value"]["Country"]

    print("\nNombre: " + str(nombre))
    print("Codigo IATA: " + str(iata))
    print("Ciudad: " + str(ciudad))
    print("Pais: " + str(pais))

    print("\nLa distancia total recorrida es de: " + str(distancia))
    

def DistanciaMasCorta(cont, verta, vertb):
    
    IATA1 = findIATA(cont, verta)
    IATA2 = findIATA(cont, vertb)
    
        
    cont['paths'] = djk.Dijkstra(cont['connections'], IATA1)
    path = djk.pathTo(cont['paths'], IATA2)
    
    trayecto = lt.newList()
    
    size = q.size(path)
    i=0
    distancia = 0
    while i<size:
        elm = q.dequeue(path)
        distancia += float(elm['weight'])
        i+=1
        lt.addLast(trayecto, elm['vertexA'])
    return distancia
    
    
def rutamascorta(cont, verta, vertb):
    
    IATA1 = findIATA(cont, verta)
    IATA2 = findIATA(cont, vertb)
    
        
    cont['paths'] = djk.Dijkstra(cont['connections'], IATA1)
    path = djk.pathTo(cont['paths'], IATA2)
    
    trayecto = lt.newList()
    
    size = q.size(path)
    i=0
    distancia = 0
    while i<size:
        elm = q.dequeue(path)
        distancia += float(elm['weight'])
        i+=1
        lt.addLast(trayecto, elm['vertexA'])
    return trayecto


def findIATA(cont, ciudad):
    arbol = cont['names']
    keys = om.keySet(arbol)
    values = om.valueSet(arbol)

    pos = lt.isPresent(keys, ciudad)
    lst = lt.getElement(values, pos)

    IATA = lst['IATA']

    return IATA


def Millas(cont, city, km):
    
    IATA = city
    grafo = cont['connections']
    distancia_total = 0
    flag = True
    verta = IATA
    vertb = None
    aeropuertos = lt.newList()
    lt.addLast(aeropuertos, IATA)
    
    while flag:
        distancia_act = 1000000000000000
        adyacentes = gr.adjacents(grafo, verta)
        
        for v in lt.iterator(adyacentes):
            distancia = hallardistancia(cont, verta, v)
            if float(distancia) < float(distancia_act):
                distancia_act = distancia
                vertb = v
        distancia_total += distancia_act
        
        distancia_regreso = DistanciaMasCorta(cont, verta, vertb)
        
        if float(distancia_total) + float(distancia_regreso) < float(km):
            flag = True
            lt.addLast(aeropuertos, vertb)
        else:
            flag = False
        
        verta = vertb
        
        
    trayecto = rutamascorta(cont, IATA, vertb)
    
    for x in lt.iterator(trayecto):
        lt.addLast(aeropuertos, x)
    dis = distancia_total + distancia_regreso
    print("Número de aeropuertos visitados es de: " + str(lt.size(aeropuertos)))
    print("La distancia total es de: " +str(dis))
    
    

def hallardistancia(cont, verta, vertb):
    
    grafo = cont['connections']
    distancia = gr.getEdge(grafo, verta, vertb)
    
    return distancia['weight']

def cerrado(cont, aeropuerto):
    
    grafo = cont['connections']
    arcos = gr.adjacentEdges(grafo, aeropuerto)
    size = lt.size(arcos)
    aeropuertos = gr.adjacents(grafo, aeropuerto)
    print("La cantidad de aeropuetos afectados es: " + str(size))

    for n in lt.iterator(aeropuertos):

        grafo = cont['airports']
        airp = om.get(grafo, n)

        aiatai = airp["key"]
        nombrei = airp["value"]["Name"]
        ciudadi = airp["value"]["City"]
        paisi = airp["value"]["Country"]

        print("\nAeropuerto " + str(nombrei) +" (" + str(aiatai) + ").")
        print("Ubicación: " + str(ciudadi) + ", " + str(paisi) + ".")


    
 


# Funciones Helper

def cleanServiceDistance(lastservice, service):
    """
    En caso de que el archivo tenga un espacio en la
    distancia, se reemplaza con cero.
    """
    if service['distance_km'] == '':
        service['distance_km'] = 0
    if lastservice['distance_km'] == '':
        lastservice['distance_km'] = 0

def formatVertex(service):
    """
    Se formatea el nombrer del vertice con el id de la estación
    seguido de la ruta.
    """
    name = service['Departure'] + '-'
    name = name + service['Destination']
    return name

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def compareIATA(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1
