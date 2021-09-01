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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList('SINGLE_LINKED')
    catalog['obras'] = lt.newList('SINGLE_LINKED')
    
    return catalog

# Funciones para agregar informacion al catalogo
def addArtista(catalog, artistaName, obra):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    artistas = catalog['artistas']
    posartista = lt.isPresent(artistas, artistaName)
    if posartista > 0:
        artista = lt.getElement(artistas, posartista)
    else:
        artista = newArtista(artistaName)
        lt.addLast(artistas, artista)
    lt.addLast(artista['obra'], obra)


def addObra(catalog, obra):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['obras'], obra)
    # Se obtienen los autores del libro
    authors = obra['DisplayName'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addArtista(catalog, author.strip(), obra)

# Funciones para creacion de datos

def newArtista(name,artistaID):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artista = {'DisplayName': "", 'ConstituentID': None ,"obra": None, }
    artista['DisplayName'] = name
    artista ['obra'] = lt.newList('SINGLE_LINKED')
    return artista

def newObra(name , obraID, artistaID):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    obra = {'title': "", "ObjectID": None, 'ConstituentID': None }
    obra['title'] = name
    obra['ObjectID'] = obraID
    return obra    

# Funciones de consulta


def sizesArtistas(catalog):
    """
    """
    return lt.size(catalog['artistas'])

def sizesObras(catalog):
    """
    """
    return lt.size(catalog['obras'])


def getUltimosTresArtistas(catalog):
    """
    Retorna los mejores libros
    """
    artista = catalog['artistas']
    ultimostres = lt.newList()
    i=sizesArtistas
    for cont in reversed(range(sizesArtistas)):
        i-=1
        artista = lt.getElement(artista, cont)
        lt.addFirst(ultimostres, artista)
    return ultimostres


def getUltimosTresObra(catalog):
    """
    Retorna los mejores libros
    """
    obra = catalog['artistas']
    ultimostres = lt.newList()
    i=sizesArtistas
    for cont in reversed(range(sizesObras)):
        i-=1
        obra = lt.getElement(obra, cont)
        lt.addFirst(ultimostres, obra)
    return ultimostres



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento