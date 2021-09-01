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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la lista cronológica de los artistas")
    print("3- Consultar las obras adquiridas en el museo")
    print("4- Consultar las obras de un artista por técnica")
    print("5- Consultar las obras por la nacionalidad de sus creadores")
    print("6- Calcular el costo para transportar todas las obras de un departamento del MoMA")
    print("7- Consultar la nueva idea de exposición del museo según la disponibilidad del área del MoMA")
    print("0- Salir")
    


def initCatalog():
    """
    Inicializa el catálogo del museo
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga el museo en la estructura de datos
    """
    controller.loadData(catalog)

def printUltimosTresArtistas(artista):
    size = lt.size(artista)
    if size:
        print(' Estos son los ultimos tres artistas: ')
        for artistas in lt.iterator(artista):
            print('Nombre: ' + artista['DisplayName'])
    else:
        print('No se encontraron los artistas')    

def printUltimosTresObras(obra):
    size = lt.size(obra)
    if size:
        print(' Estos son los ultimos tres obra: ')
        for obras in lt.iterator(obra):
            print('Nombre: ' + obra['DisplayName'])
    else:
        print('No se encontraron libros')            

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Obras Cargadas: ' + str(lt.size(catalog['obras'])))
       

    elif int(inputs[0]) == 2:
        number = input("ultimos 3 artistas: ")
        artistas = controller.getUltimosTresArtistas(catalog)
        printUltimosTresArtistas(artistas)

        number = input("ultimos 3 obras: ")
        obras = controller.getUltimosTresObra(catalog)
        printUltimosTresObras(obras)

    else:
        sys.exit(0)
sys.exit(0)
