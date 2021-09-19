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

defauly_limit=1000
sys.setrecursionlimit(defauly_limit*100)

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
    


def initCatalog(opciones):
    """
    Inicializa el catálogo del museo
    """
    return controller.initCatalog(opciones)

def loadData(catalog):
    """
    Carga el museo en la estructura de datos
    """
    controller.loadData(catalog)

def printUltimosTresArtistas(sublista1,sublista2):
    size1 = lt.size(sublista1)
    size2 = lt.size(sublista2)
    if size1 :
       
        for artistas in lt.iterator(sublista1):
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

def printSortResults(sort_obra, sample=10):
    size= lt.size(sort_obra)
    if size > sample:
     print("los primeros ", sample, "las primeras obras son:")
     i=1
     while i <= sample:
         obras= lt.getElement(sort_obra,i)
         print('Titulo:' + obras['title']+' Artistas:'+ obras['']+ ' Fecha:'+ obras['Date_Acquired'] + 'Medio:' + obras['Medium'] + 'Dimensiones:'+ obras[''])
         i+=1    

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        opciones = int(input('De que forma desea cargar el catalogo: 1= linkedlist, culquier otro numero Arraylist'))
    
        catalog = initCatalog(opciones)
        loadData(catalog) 

        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        print('Obras Cargadas: ' + str(lt.size(catalog['obras'])))

    elif int(inputs[0]) == 2:
        fechaInicio = input("fecha de nacimiento: ")
        fechaFin = input("fecha de Fallecimiento: ")
        artistas = controller.getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin)
        printUltimosTresArtistas(artistas)

    elif int(inputs[0]) == 3:
        valor = int(input('Ingrese el tamaño de la lista que quiere crear:'))
        number = input("ultimos 3 obras: ")
        sort=input("selecciones el ordenanimento que quiere: 0= Insercionsort, 1= shellsort, 2= quicksort")
        ordenamiento=controller.getSorter(catalog,sort)
        obras = controller.getUltimosTresObra(catalog)
        tamaño = controller.getTamañoSubLista(catalog,valor)
        printUltimosTresObras(obras) 

    elif int(inputs[0]) == 4:
        number = input("obras por tecnica de artista: ")
        artistas = controller.getUltimosTresObra(catalog)
        printUltimosTresObras(obras) 

    elif int(inputs[0]) == 5:
        number = input("obra por nacionalidad artista: ")
        obras = controller.getUltimosTresObra(catalog)
        printUltimosTresObras(obras)

    elif int(inputs[0]) == 6:
        number = input("costo transportar obras: ")
        artistas = controller.getUltimosTresArtistas(catalog)
        printUltimosTresArtistas(artistas)

    elif int(inputs[0]) == 7:
        number = input("nueva exposicion: ")
        artistas = controller.getUltimosTresArtistas(catalog)
        printUltimosTresArtistas(artistas)


    else:
        sys.exit(0)
sys.exit(0)
