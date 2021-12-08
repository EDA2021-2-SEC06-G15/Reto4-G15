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
 """

import config as cf
import model
import csv
from DISClib.ADT.graph import gr
from DISClib.ADT import orderedmap as om


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos


def loadAirports(analyzer, airportsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    airportsfile = cf.data_dir + airportsfile
    input_file = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addAirport(analyzer, avistamiento)

    print("Cantidad de aeropuertos: " + str(om.size(analyzer['airports'])))
    return analyzer

def loadCities(analyzer, citiesfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    citiesfile = cf.data_dir + citiesfile
    input_file = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    for avistamiento in input_file:
        model.addCity(analyzer, avistamiento)

    print("Cantidad de ciudades: " + str(om.size(analyzer['cities'])))
    return analyzer

def loadRoutes(analyzer, airportsfile, routesfile):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile = cf.data_dir + airportsfile
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")
    graph = analyzer['connections']
    for airport in input_file:
        esta = gr.containsVertex(graph, airport['IATA'])
        if not esta:
            gr.insertVertex(graph, airport['IATA'])
    
    servicesfile2 = cf.data_dir + routesfile
    input_file2 = csv.DictReader(open(servicesfile2, encoding="utf-8"),
                                delimiter=",")
    for airport in input_file2:
        if gr.getEdge(graph, airport['Departure'],airport['Destination']) is None:
            gr.addEdge(graph, airport['Departure'], airport['Destination'], airport['distance_km'])

    countgraphvalues(graph)

def countgraphvalues (graph):
    verts = gr.numVertices(graph)
    arcs = gr.numEdges(graph)

    print("El grafo cargado cuenta con " + str(verts) + " vertices y " + str(arcs) + " arcos.")

    print(gr.vertices(graph))

        



# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
