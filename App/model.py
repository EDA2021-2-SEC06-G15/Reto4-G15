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
                    'components': None
                    }

        analyzer['airports'] = om.newMap(omaptype='BST')
        analyzer['cities'] = om.newMap(omaptype='BST')
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
    updateAirport(analyzer['cities'], city)
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







    
    


# Funciones para creacion de datos

# Funciones de consulta

def puntosInterconexion(cont):
    vertices = gr.vertices(cont['connections'])
    
    mayor = 0
    aeropuerto = None
    print(vertices)

    for v in lt.iterator(vertices):
        print(v)
        if v is not None:
            grado = float(gr.degree(cont['connections'],v))
        if grado > mayor:
            mayor = grado
            aeropuerto = v
        
    print("El aeropuerto con más conecciones es: " + str(aeropuerto) + ". Con: " + str (mayor) + "conecciones")
    print(str(gr.outdegree(cont['connections'], aeropuerto)))
    print(str(gr.indegree(cont['connections'], aeropuerto)))

def connectedComponents(analyzer):
    """
    Calcula los componentes conectados del grafo
    Se utiliza el algoritmo de Kosaraju
    """
    analyzer['components'] = scc.KosarajuSCC(analyzer['connections'])
    ans = scc.connectedComponents(analyzer['components'])
    print("El número de elementos conectados es de: " + str(ans))
    return ans

def clusteres(analyzer, verta, vertb):

    connectedComponents(analyzer)

    sccc = analyzer['components']
    ans = scc.stronglyConnected(sccc, verta, vertb)

    if ans == True:
        print("Los aeropuertos están fuertemente conectados.")

    else:
        print("los aeropuertos NO están fuertemente conectados.")


def caminoMasCorto(cont, verta, vertb):
    pass
    
        
        


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
