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


from DISClib.DataStructures.arraylist import size, subList
import config as cf
import time 
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def estructuradatos(opciones):
    if opciones == 1:
        temp = 'SINGLE_LINKED'
    else:
        temp = 'ARRAY_LIST'
    return temp 

def newCatalog(): 
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artistas': None,
               'obras': None}

    catalog['artistas'] = lt.newList(estructuradatos,cmpfunction=compareartistas)
    catalog['obras'] = lt.newList(estructuradatos)
    
    return catalog

# Funciones para agregar informacion al catalogo

def cargarCatalogoArtistas(catalog, artistaName):
    
  
    ltArtistas = catalog['artistas']
    artistaNuevo = newArtista(artistaName["ConstituentID"],artistaName["DisplayName"], artistaName["ArtistBio"], artistaName["Nationality"], artistaName["Gender"],artistaName["BeginDate"], artistaName["EndDate"],artistaName["Wiki QID"],artistaName["ULAN"])
    lt.addLast(ltArtistas, artistaNuevo)


def cargarCatalogoObras(catalog, obraName):
    
  
    ltObras = catalog['obras']
    obraNuevo = newObra(obraName["ObjectID"],obraName["Title"],obraName["ConstituentID"],obraName["Date"], obraName["Medium"], obraName["Dimensions"], obraName["CreditLine"],obraName["AccessionNumber"],obraName["Classification"],obraName["Department"], obraName["DateAcquired"],obraName["Cataloged"],obraName["URL"],obraName["Circumference (cm)"],obraName["Depth (cm)"],obraName["Diameter (cm)"])
    lt.addLast( ltObras, obraNuevo)    


def relacionArtistaObra(catalog,catalog2):
      
 artistas= catalog['artistas']
 obras=catalog2['obras']

 artistas = sortConstituentID(artistas)
 obras=sortConstituentID(obras)
 i =0 

 while i <lt.size(artistas):
     j=0
     artista= lt.getElement(artistas,i)

     while j< lt.size(obras):
         obra=lt.getElement(obras,j)

         if artista['ConstituentID'] == obra['ConstituentID']:
             lt.addLast(artista['obra'],obra)
             lt.addLast(obra['artista'],artista)
         j=+1
     i=+1
    

def addArtista(catalog, artistaName):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    ltArtistas = catalog['artistas']
    artistaNuevo = newArtista(artistaName["ConstituentID"],artistaName["DisplayName"], artistaName["ArtistBio"], artistaName["Nationality"], artistaName["Gender"],artistaName["BeginDate"], artistaName["EndDate"],artistaName["Wiki QID"],artistaName["ULAN"])
    print(artistaNuevo)
    posartista = lt.isPresent(ltArtistas, artistaNuevo)
    if posartista > 0:
        artista = lt.getElement(ltArtistas, posartista)
        return artista
    else:
        lt.addLast(ltArtistas, artistaNuevo)
        return artistaNuevo


def addObra(catalog, obraName):
    
    ltObras = catalog['obras']
    obraNuevo = newObra(obraName["ObjectID"],obraName["Title"],obraName["ConstituentID"],obraName["Date"], obraName["Medium"], obraName["Dimensions"], obraName["CreditLine"],obraName["AccessionNumber"],obraName["Classification"],obraName["Department"], obraName["DateAcquired"],obraName["Cataloged"],obraName["URL"],obraName["Circumference (cm)"],obraName["Depth (cm)"],obraName["Diameter (cm)"])
    print(obraNuevo)
    posobra = lt.isPresent(ltObras, obraNuevo)
    if posobra > 0:
        obra = lt.getElement(ltObras, posobra)
        return obra
    else:
        lt.addLast(ltObras, obraNuevo)
        return obraNuevo

# Funciones para creacion de datos

def newArtista(id,name,artistbio,nationality,gender,beginDate,endDate,wiki,ulan):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artista = {'ConstituentID': "", 'DisplayName': "", "ArtistBio": "" , "Nationality": "", "Gender": "","BeginDate": ""  , "EndDate" : "", "Wiki QID": "", "ULAN": "" }
    artista['ConstituentID'] = id
    artista['DisplayName'] = name
    artista['ArtistBio'] = artistbio
    artista['Nationality'] = nationality
    artista['Gender'] = gender
    artista['BeginDate'] = beginDate
    artista['EndDate'] = endDate
    artista['WikiQID'] = wiki 
    artista['ULAN'] = ulan 
    artista ['obra'] = lt.newList('ARRAY_LIST')
    return artista

def newObra(objectID,title,constituentID, date,medium,dimensions,creditline,accessionnumber, depth, classification, department, dateAcquired, cataloge, url, diameter, circumference):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    obra = {"ObjectID": "",'Title': "", "ConstituentID": "", "Date" : "", "Medium" : "", "Dimensions" : "", "CreditLine" : "", "AccessionNumber" : "", "Depth": "", "Classification" : "", "Department": "", "DateAcquired" : "", "Cataloge": "", "URL" : "","Circumference": ""} 
    obra['Title'] = title
    obra['Date'] = date
    obra['ConstituentID'] = constituentID
    obra['Medium'] = medium
    obra['Dimensions'] = dimensions
    obra['CreditLine'] = creditline
    obra['Department'] = department
    obra['DateAcquired'] = dateAcquired
    obra['ObjectID'] = objectID
    obra['Diameter'] = diameter
    obra['Circumference'] = circumference
    obra['Depth'] = depth 
    obra['AccessionNumber'] = accessionnumber
    obra['Classification'] = classification 
    obra['Cataloge'] = cataloge
    obra['URL'] = url 
    obra['artista'] = lt.newList('ARRAY_LIST')
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

def tamañoMuestra(catalog,valor):
    tamaño = lt.size(catalog['obra'])
    if valor > tamaño:
        print('Error')
    else:
        return valor 
        
def subListObras(catalog, pos):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    return lt.subList(catalog['obra'],pos,tamañoMuestra)
  
# Funciones utilizadas para comparar elementos dentro de una lista
def compareartistas(artistaname1, artista):
    if (artistaname1.lower() in artista['name'].lower()):
        return 0
    return -1

def compareObras(obra1, obra):
    if (obra1.lower() in obra['Title'].lower()):
        return 0
    return -1   

def cmpArtworkByDateAcquired(artwork1,artwork2):
    """
    Devuelve verdadero (True) si el DateAcquired de artwork1 < artwork2
        Args: 
        Artwork1: informacion de la primera obra de DateAcquired
        Artwork2: informacion de la segunda obra de DateAcquired
    """
    respuesta = False 
    if artwork1['DateAcquired'] < artwork2['DateAcquired']:
        respuesta = True 
    return respuesta

def cmpArtistasPorAño(artista1, artista2):
    rta=False
    if artista1['BeginDate']<artista2['BeginDate']:
        rta =True
    return rta

def cmpConstitudID(objeto1, objeto2):
 
    rta= False
    if objeto1['ConstituentID']<objeto2['ConstituentID']:
     rta=True
    return rta
    



# Funciones de ordenamiento


def tipoSorter(opciones,lst):
    if opciones == 0:
        return insertionsort(lst)
    elif opciones == 1:
        return shellsort(lst)
    elif opciones == 2:
        return quicksort(lst)
    else:
        print ("error")


def insertionsort(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpArtworkByDateAcquired(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst


def shellsort(lst):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpArtworkByDateAcquired(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst



def partition(lst, lo, hi, cmpfunction):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if cmpfunction(
           lt.getElement(lst, leader), lt.getElement(lst, hi)):
            lt.exchange(lst, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lst, follower, hi)
    return follower


def quicksort(lst, lo, hi, cmpfunction):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lst, lo, hi, cmpfunction)
    quicksort(lst, lo, pivot-1, cmpfunction)
    quicksort(lst, pivot+1, hi, cmpfunction)


def quicksortsort(lst):
    quicksort(lst, 1, lt.size(lst),cmpArtworkByDateAcquired)
    return lst


def InserecionOrdenarfechaobras(catalog):
    size = lt.size(catalog['obras'])
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1                                                   
        while (pos2 > 1) and (cmpArtworkByDateAcquired (lt.getElement(catalog['obras'], pos2), lt.getElement(catalog['obras'], pos2-1))):
            lt.exchange(catalog['obras'], pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return catalog 



def selectionsort(lst, cmpfunction):
    size = lt.size(lst)
    pos1 = 1
    while pos1 < size:
        minimum = pos1    # minimun tiene el menor elemento
        pos2 = pos1 + 1
        while (pos2 <= size):
            if (cmpfunction(lt.getElement(lst, pos2),
               (lt.getElement(lst, minimum)))):
                minimum = pos2  # minimum = posición elemento más pequeño
            pos2 += 1
        lt.exchange(lst, pos1, minimum)  # elemento más pequeño -> elem pos1
        pos1 += 1
    return lst

# funcion de ordenamiento - tiempo 
def sortObras(catalog,opcion):
    sub_list = lt.subList(catalog['obras'], 1, lt.size(catalog['obras']))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list=tipoSorter(opcion, sub_list)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,sorted_list

def mergeSort(lst, cmpfunction):
    size = lt.size(lst)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lst, 1, mid)
        rightlist = lt.subList(lst, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        mergeSort(leftlist, cmpfunction)
        mergeSort(rightlist, cmpfunction)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpfunction(elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(lst, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                lt.changeInfo(lst, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lst, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lst, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lst


    
def sortConstituentID(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and (cmpConstitudID(
               lt.getElement(lst, pos2), lt.getElement(lst, pos2-1))):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst


def getUltimosPrimerosTresArtistas(catalog,fechaInicio,fechaFin):
    """
    """
    artista = catalog['artistas']
    listaOrdenada = mergeSort(artista,cmpArtistasPorAño)
    sizelt=lt.size(listaOrdenada)

    posicioninicial= 0
   
    found = False
    posicion = 0

    while  posicion < sizelt and not found:
        artista1=lt.getElement(listaOrdenada,posicion)
        
        if artista1['BeginDate']<fechaInicio:
            posicion =  posicion + 1

        elif artista1['BeginDate']>=fechaInicio:
            found = True
            posicioninicial=posicion
            
    subLista1= lt.subList(listaOrdenada,posicioninicial,(sizelt-posicioninicial))

    posicionfinal = 0
    found2 = False
    posicion2 = 0
    sizelt2=lt.size(subLista1)

    while  posicion2 < sizelt2 and not found2:
        artista2=lt.getElement(subLista1,posicion2)
        
        if artista2['BeginDate']<=fechaFin:
            posicion2 =  posicion2 + 1
            posicionfinal=posicion2+1

        if artista2['BeginDate']>fechaFin:
         found2 = True
         

    subLista2=lt.subList(subLista1,0,posicionfinal)
    return (subLista2)