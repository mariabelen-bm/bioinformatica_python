#################################
# MARÍA BELÉN BARQUERO MARTÍNEZ #
#################################

# Módulos
from itertools import *
from tabnanny import verbose

def powerset(elementos):
    s = list(elementos)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

# Ejercicio 1

def CalculaDX(posCortes):
    """
     (list) –> list
    Calcula la posicion de los cortes
        Entrada: lista
        Salida: lista
    >>> posCortes=[0, 6, 7, 8, 9, 11, 12]
    >>> CalculaDX(posCortes)
    [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 11, 12]
    >>> CalculaDX([0, 4, 5])
    [1, 4, 5]
    """
    #Errores
    if type (posCortes) not in(list, tuple):
        raise TypeError("ERROR: posCortes debe ser una lista")
    if len(posCortes) < 2:
        raise IndexError("ERROR: posCortes debe ser una lista con al menos dos elementos")
    if not all (i>=0 for i in posCortes):
        raise AssertionError("ERROR: Los cortes de restricción de posCortes NO pueden ser negativos")
    if not all(isinstance(i, int) for i in posCortes):
        raise TypeError("ERROR: Todos los cortes de restricciones deben ser números enteros (int)")
    
    #Cuerpo del algoritmo
    posCortes=sorted(posCortes) #la ordenamos
    solucion=[] #creamos un lista vacía para añadir soluciones
    n=int(2) #n va a ser dos (cortes) # longitud maximo de los puntos de corte

    for i in powerset(posCortes): # powerset = genera un elemento iterable que consume menos recursos.
        if len(i) == n: #si la combinación tiene la misma longitud que n, 
            diferencia=i[1]-i[0] # hacemos la diferencia entre los dos tamaños y obtenemos el fragmento de DNA
            solucion.append(diferencia) # añadimos la diferencia a la solución

    #Resultado
    return(sorted(solucion)) #le decimos que nos lo ordene

# Ejercicio 2

def MapaRestriccionesBusquedaExhaustivaMax(n,L):   
    """
    (int,list) –> list
    Todas las listas de posiciones candidatas a puntos de corte, quedandose con las que tengan el punto de corte mas cercano a M
        Entrada: entero, lista
        Salida: lista
    >>> n=7
    >>> L=[1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12] 
    >>> MapaRestriccionesBusquedaExhaustivaMax(n,L)
    ([(0, 1, 2, 5, 7, 9, 12), (0, 1, 5, 7, 8, 10, 12), (0, 2, 4, 5, 7, 11, 12), (0, 3, 5, 7, 10, 11, 12)], [(0, 2, 4, 5, 7, 11, 12), (0, 3, 5, 7, 10, 11, 12)])
    >>> n=3
    >>> L=[2, 3, 5]
    >>> MapaRestriccionesBusquedaExhaustivaMax(n,L)
    ([(0, 2, 5), (0, 3, 5)], [(0, 3, 5)])
    """
    #Errores
    if type(L) not in (list,tuple):
        raise TypeError("ERROR: L debe ser una lista")
    if type(n) != int or n <= 1:
        raise TypeError("ERROR: n debe ser un número entero mayor que 1")
    if len(L) < 1:
        raise IndexError("ERROR: L debe ser una lista con al menos un elemento")
    if not all(isinstance(numeros, int) for numeros in L):
        raise TypeError("ERROR: Todos los elementos de la lista L deben ser números enteros ")
    if not all(numeros>=1 for numeros in L):
        raise AssertionError("ERROR: Los números presentes en L deben ser mayores que 0")

    #Cuerpo del algoritmo                   # N maximo de puntos de corte, entrammos con una lista con los posibles fragmentos de DNA
    solucion_total=[] #añadimos las soluciones
    maxAparicion=0 # inicializamos el máximo de operaciones
    for candidato in combinations(range(0,L[-1]+1),n): #el rango va desde 0 hasta el valor de L[-1] (el ultimo valor de la lista) +1 porque python comienza en 0. 
        if CalculaDX(candidato) == L:  # te pide que sea desde 0 hasta el tamaño máximo, por eso L-1
            solucion_total.append(candidato)
            if candidato[n-2] > maxAparicion: # posición n-2 de cada candidato ya que n estaría fuera del rango y n-1 sería el máximo
                solucion=[]                   # n-1 sería el máximo por eso tenemos que añadir el que le precede que es el n-2
                maxAparicion = candidato[n-2]
                solucion.append(candidato)
            elif candidato[n-2] == maxAparicion:
                    solucion.append(candidato)

    #Resultado
    return(solucion_total, solucion)

# Ejercicio 3

def lecturaizquierda(permutacionInicial):
    """
    (list) –> list
    Devuelve una lista con los cambios necesarios para la ordenacion
        Entrada: lista
        Salida: lista

    >>> permutacionInicial = [1, 2, 3, 6, 4, 5]
    >>> lecturaizquierda(permutacionInicial)
    [(3, 4), (4, 5)]

    >>> permutacionInicial = [6, 1, 2, 3, 4, 5]
    >>> lecturaizquierda(permutacionInicial)
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

    >>> permutacionInicial = [3, 4, 2, 1, 5, 6, 7, 10, 9, 8]
    >>> lecturaizquierda(permutacionInicial)
    [(0, 3), (2, 3), (7, 9)]
    """

    #Cuerpo del algoritmo
    permutacionOrdenada= sorted(permutacionInicial) #hemos ordenado la lista de permutaciones
    permutaI=permutacionInicial #permutaI es permuta inicial, lo hicimos para ver si así no pasaba lo del aliasing
    solucion_final_izq=[] # creamos una lista con las soluciones de lectura de la izquierda
    n = len(permutacionInicial)
    
    for pos in range(n): #en este caso el rango es de la longitud de la lista
        if permutaI[pos] != permutacionOrdenada[pos]: #comprobamos la diferencia entre la lista ordenada y la lista inicial
            primer_frag = pos #pos en este caso es la posicion que hay en el rango de la lista [0,1,2,3...] donde está el error          
            segundo_frag=permutaI.index(permutacionOrdenada[pos]) #aqui se coge la posicion correcta donde queremos hacer el cambio, seria lo mismo que pos + 1 
            permutaI[primer_frag:segundo_frag+1] = reversed(permutaI[primer_frag:segundo_frag+1]) #mediante el reverse se hace el cambio y se actualiza la nueva lista, 
            #el +1 es para coger el valor que queremos intercambiar y el anterior
            solucion_final_izq.append((primer_frag, segundo_frag)) #se añaden las dos posibles soluciones a la lista de soluciones
    
    #Resultado
    return solucion_final_izq

def lecturaderecha(permutacionInicial):
    """
    (list) –> list
    Devuelve una lista con los cambios necesarios para la ordenacion
        Entrada: lista
        Salida: lista

    >>> permutacionInicial = [1, 2, 3, 6, 4, 5]
    >>> lecturaderecha(permutacionInicial)
    [(3, 5), (3, 4)]

    >>> permutacionInicial = [6, 1, 2, 3, 4, 5]
    >>> lecturaderecha(permutacionInicial)
    [(0, 5), (0, 4)]

    >>> permutacionInicial = [3, 4, 2, 1, 5, 6, 7, 10, 9, 8]
    >>> lecturaderecha(permutacionInicial)
    [(7, 9), (1, 3), (0, 2), (0, 1)]
    """

    #Cuerpo del algoritmo
    permutaD=(permutacionInicial)
    permutacionOrdenada= sorted(permutacionInicial)
    solucion_final_der=[]
    n = len(permutacionInicial)

    for pos in range(n-1,0,-1): #con este rango se recoge la lista de forma inversa [5,4,3...], y cambiamos las posiciones, es decir:
            # cuando leemos al reves cogemos el primer fragmento es la posicion correcta y el segundo es el error.
        if permutaD[pos] != permutacionOrdenada[pos]: #comprobamos la posicion donde puede haber una diferencia entre la lista ordenada
            primer_frag = permutaD.index(permutacionOrdenada[pos]) #seleccionamos el indice donde aparece el error seria igual que pos -1
            segundo_frag= pos #posicion del rango donde está el error 
            permutaD[primer_frag:segundo_frag+1] = reversed(permutaD[primer_frag:segundo_frag+1]) #hacemos el intercambio y actualizamos la lista, el +1 es para coger el valor que queremos intercambiar y el anterior
            solucion_final_der.append((primer_frag, segundo_frag))
    
    #Resultado
    return solucion_final_der


def OrdenacionInversionSimple(permutacionInicial):
    """
    (list) –> list
    Devuelve una lista con los cambios necesarios para la ordenacion
        Entrada: lista
        Salida: lista

    >>> permutacionInicial = [1, 2, 3, 6, 4, 5]
    >>> OrdenacionInversionSimple(permutacionInicial)
    ([(3, 4), (4, 5)], ([(3, 4), (4, 5)], [(3, 5), (3, 4)]))

    >>> permutacionInicial = [6, 1, 2, 3, 4, 5]
    >>> OrdenacionInversionSimple(permutacionInicial)
    ([(0, 5), (0, 4)], ([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], [(0, 5), (0, 4)]))

    >>> permutacionInicial = [3, 4, 2, 1, 5, 6, 7, 10, 9, 8]
    >>> OrdenacionInversionSimple(permutacionInicial)
    ([(0, 3), (2, 3), (7, 9)], ([(0, 3), (2, 3), (7, 9)], [(7, 9), (1, 3), (0, 2), (0, 1)]))
    """

    #Errores
    if type(permutacionInicial) not in (list,tuple):
        raise TypeError ("ERROR: permutacionInicial debe ser una lista o una tupla")
    if len(permutacionInicial)<1:
        raise ValueError("ERROR: permutacionInicial debe ser una lista de almenos 1 elemento")
    if not all (isinstance(numero, int) for numero in permutacionInicial):
        raise TypeError ("ERROR: Todos los elementos de permutacionInicial deben ser números enteros")
    if not all(numero>=1 for numero in permutacionInicial):
        raise ValueError ("ERROR: Los números en la lista permutacionInicial deben ser mayores que 0")
        
    #Cuerpo de la función
    lista=tuple(permutacionInicial)# se nos igualaban todas las listas a el mismo valor de la lista ordenada
    solucion_izquierda=lecturaizquierda(list(lista)) #necesitamos que sea una lista para los cambios que se van a hacer
    solucion_derecha=lecturaderecha(list(lista))
    posibles_soluciones=solucion_izquierda,solucion_derecha

    #Resultados
    if len(solucion_izquierda) <= len(solucion_derecha):
        return solucion_izquierda, posibles_soluciones 
    else:
        return solucion_derecha, posibles_soluciones

# Pruebas
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
