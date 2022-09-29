#################################
# MARÍA BELÉN BARQUERO MARTÍNEZ #
#################################

#0. Funciones para validación de errores

def es_RNA(cadena):
    """
    str -> bool
    Devuelve un valor True si la cadena de caracteres únicamente contiene nucleótidos de RNA
        entrada: cadena de caracteres en mayúscula
        salida: booleano indicando si se trata o no de RNA
    
    >>> es_RNA("AUCG")
    True
    """
    nucleotidos_RNA = ["A", "U" ,"C","G"]
    es_nucleotido_arn = [i in nucleotidos_RNA for i in cadena]
    
    return all(es_nucleotido_arn)

def es_DNA(cadena):
    """
    str -> bool
    Devuelve un valor True si la cadena de caracteres únicamente contiene nucleótidos de DNA
        entrada: cadena de caracteres en mayúscula
        salida: booleano indicando si se trata o no de DNA

    >>> es_DNA("ATCG")
    True
    """
    nucleotidos_DNA = ["A", "T", "C", "G"]
    es_nucleotido_dna = [i in nucleotidos_DNA for i in cadena]

    return all(es_nucleotido_dna)

# 1

def num_bases_y_gen ():
    """
    int -> bool
    Esta función va a pedirle al usuario que introduzca el número de bases y el número de genes que posee.
    Nos da como resultado el número actualizado de bases y genes.
        entrada: enteros de bases_inicio y genes_inicio introducidos por el usuario
        salida: enteros de bases_inicio y genes_inicio

    >>> num_bases_y_gen()
    Introduzca el número de genes: 12
    Introduzca el número de bases: 4
    12, 4
    """
    genes_inicio = 0
    bases_inicio = 0

    try:
        genes_inicio = int(input("Introduzca el número de genes: "))
        bases_inicio = int(input("Introduzca el número de bases: "))

        return (genes_inicio, bases_inicio)

    except TypeError:
        raise TypeError("¡Se debe introducir un número entero!")
    
def bases_por_gen(bases, genes):
    """
    int, int -> float
    Esta función va a realizar el promedio de las bases y los genes introducidos.
        entrada: enteros de bases y genes.
        salida: promedio entre bases y genes

    >>> bases_por_gen(bases, genes)
        12,4
        3.0
    """
    
    try:
        return bases/genes

    except ZeroDivisionError:
        raise ZeroDivisionError("¡No se puede dividir entre cero!")

def bases_gen():
    """
    int, int -> float
    Este programa nos devuelve el promedio entre las bases y los genes introducidos por el ususario.
    El programa se puede detener si el usuario introduce tanto en las bases como en los genes el valor -1 (número negativo)
    Mientras que no se le indique al programa este valor, el programa no se detendrá y le pedirá infinitamente número de bases y de genes a introducir.
        entrada: el número de bases y de genes introducido por el usuario
        salida: el promedio del número de bases entre el número de genes introducidos por el usuario

    >>> bases_gen()
    Introduzca el número de genes: 12
    Introduzca el número de bases: 4
    El número de bases por gen es: 3.0

    Ejemplo de fin del programa
    >>> bases_gen()
    Introduzca el número de genes: -1
    Introduzca el número de bases: -1
    El programa ha finalizado
    """

    bases_gen= -1
    print("Introduce -1 cuando quieras que el programa finalice")

    while True:
        bases, genes = num_bases_y_gen()
        if bases == -1 or genes == -1:
            print("El programa ha finalizado")
            break
        bases_gen = bases_por_gen(bases, genes)
        print("El número de bases por gen es: ", bases_gen)

# Programa: bases_gen()

# 2

def introduce_cadenas():
    """
    str, str -> str, str
    Este programa le pide al usuario que introduzca la cadena 1 y la cadena 2 que posee.
        entrada: las dos cadenas que el usuario posee y que introduce.
        salida: las dos cadenas que el ususario posee.
    
    >>> introducie_cadenas()
    Introduzca la cadena 1: ABC
    Introduzca la cadena 2: DEF
    ABC,DEF
    """
    cadena_1_inicio = input("Introduzca la cadena 1: ")
    cadena_2_inicio = input("Introduzca la cadena 2: ")
    
    return(cadena_1_inicio, cadena_2_inicio)

def concatena_cadenas (cadena1, cadena2):
    """
    str, str -> str 
    Este programa realiza la suma de las dos cadenas introducidas por el usuario.
        entrada: las dos cadenas
        salida: la suma de las dos cadenas

    >>> concatena_cadenas()
    cadena1: ABC
    cadena2: DEF
    ABCDEF
    """
    return cadena1 + cadena2

def concatena ():
    """
    str, str -> str
    Este programa nos devuelve la concatenación de las dos cadenas introducidas por el usuario. Le vuelve a pedir al usuario que introduzca
    cadenas siempre y cuando el usuario no de por finalizado el programa.
        entrada: las dos cadenas que el usuario introduce
        salida: el resultado de la concatenación

    >>> concatena()
    Introduzca la cadena 1: ABC
    Introduzca la cadena 2: DEF
    El resultado de la concatenación de ambas cadenas es: ABCDEF

    Ejemplo de fin del programa
    >>> concatena()
    Introduzca la cadena 1: FIN
    Introduzca la cadena 2: FIN
    El programa ha finalizado   
    """
    concatena= "FIN"
    print("Introduce FIN cuando quieras que el programa finalice")

    while True:
        cadena1, cadena2 = introduce_cadenas()
        if cadena1 == "FIN" or cadena2 == "FIN":
            print("El programa ha finalizado")
            break
        concatena = concatena_cadenas(cadena1, cadena2)
        print("El resultado de la concatenación de ambas cadenas es: ", concatena)

# Programa: concatena()

# 3

def introduzca_cadena():
    """
    str -> bool
    Este programa le pide al usuario que introduzca la cadena de DNA que posee. Si no es una cadena de DNA, nos lanzará un mensaje de error.
        entrada: la cadena de DNA que el usuario introduzca.
        salida: True si es una cadena de DNA

    >>> introduzca_cadena()
    Introduzca la cadena de DNA: ACTG
    ACTG
    """
    try:
        dna=input("Introduzca la cadena de DNA: ")
        return(dna) 

    except TypeError:
        raise TypeError ("Debes introducir una cadena de DNA")

def DNA_RNA():
    """
    str -> str
    Este programa introduce la cadena de DNA estimada por el usuario y devuelve la molécula de RNA que le corresponde.
    El programa se ejecutará infinitamente hasta que el ususario decida finalizarlo introduciendo FIN.
        entrada: una cadena de DNA introducida por el ususario.
        salida: la cadena de RNA resultante.

    >>> DNA_RNA()
    Introduzca la cadena de DNA: ACTG
    La cadena de RNA resultante es:  ACUG

    Ejemplo de fin del programa
    >>> DNA_RNA()
    Introduzca la cadena de DNA: FIN
    El programa ha finalizado.
    """
    print("Introduzca FIN cuando quieras que finalice el programa")
    
    while True:
        dna1 = introduzca_cadena()
        dna = dna1.upper()
        rna=""

        for i in range (len(dna)):
            if dna[i] == "T":
                rna += "U"
            else:
                rna += dna[i]

        if dna == "FIN":
            print("El programa ha finalizado")
            break
        
        print("La cadena de RNA resultante es: ", rna)



# Programa: DNA_RNA()

# 4

def cadena():
    """
    str -> bool
    Este programa introduce la cadena de DNA que el ususario introduzca. Si no es una cadena de DNA nos lanzará un mensaje de error.
        entrada: la cadena de DNA que el ususario introduce
        salida: True si es una cadena de DNA

    >>> cadena()
    Introduzca la cadena de DNA: ACTG
    ACTG
    """
    try:
        dna = input("Introduzca la cadena de DNA: ")
        return(dna)

    except TypeError:
        raise TypeError("La cadena debe ser una cadena de DNA")
        

def inversa():
    """
    str -> str
    Este programa realiza el complemento de la inversa de la cadena de DNA introducida por el usuario.
    El programa se ejecutará hasta que el usuario introduzca FIN.
        entrada: la cadena de DNA que el ususario introduce
        salida: el complemento de la inversa de la cadena de DNA introducida
    
    >>> inversa(revcom)
    Introduzca la cadena de DNA: ACTG
    El complemento de la inversa de la cadena de DNA introducida es:  CAGU

    Ejemplo de fin del programa
    >>> inversa(revcom)
    Introduzca la cadena de DNA: FIN
    El programa ha finalizado
    """
    print("Introduce FIN cuando quieras que finalice el programa")

    while True:
        dna1 = cadena()
        dna = dna1.upper()
        revcom = [""]

        #Errores
        if es_DNA(dna) == False:
            raise TypeError ("Debes introducir una cadena de DNA")

        #Cuerpo de la función
        for i in range (len(dna)):
            if dna [i] == "A":
                revcom.append("U")
            elif dna [i] == "C":
                revcom.append("G")
            elif dna [i] == "T":
                revcom.append("A")
            else:
                revcom.append("C") #Conseguimos el complemento del DNA

        #Condición de fin del programa
        if dna == "FIN":
            print("El programa ha finalizado")
            break

        arn = revcom[::-1] #Hacemos la inversa del complemento
        rna = "".join(arn) #Pasamos la lista a str
        print("El complemento de la inversa de la cadena de DNA introducida es: ", rna)

# Programa: inversa()

# 5

def define_numeros ():
    """
    int, int -> int, int
    Este programa le pide al ususario que introduzca dos números enteros. Si alguno de ellos no es un entero, mandará un mensaje de error.
        entrada: pide al ususario los dos números
        salida: devuelve los números enteros introducidos por el ususario

    >>> define_numeros()
    Introduzca el primer número: 10
    Introduzca el segundo número: 9
    10,9
    """
    try:
        numero1 = int(input("Introduzca el primer número: "))
        numero2 = int(input("Introduzca el segundo número: "))

        return (numero1, numero2)

    except ValueError:
        raise ValueError("Ambos números deben ser número enteros (int)")

def mayor ():
    """
    int, int -> bool
    Este programa nos devuelve el número mayor de dos números introducidos por el usuario. El programa funciona de forma indefinida hasta
    que el ususario decide ponerle fin. 
        entrada: dos números enteros introducidos por el usuario
        salida: cuál es el mayor de ellos.

    >>> mayor()
    Introduzca -1 en ambos números cuando quiera que el programa finalice
    Introduzca el primer número: 10
    Introduzca el segundo número: 9
    El número 1, que es 10 ,es mayor que el número 2, que es 9

    Ejemplo de fin del programa
    >>> mayor()
    Introduzca -1 en ambos números cuando quiera que el programa finalice
    Introduzca el primer número: -1
    Introduzca el segundo número: -1
    El programa ha finalizado
    """
    
    print ("Introduzca -1 en número1 y -2 en número 2 cuando quiera que el programa finalice")

    #Cuerpo de la función
    while True:
        numero1, numero2 = define_numeros()
        if numero1 > numero2:
            print("El número 1, que es", numero1, ",es mayor que el número 2, que es", numero2)
        elif numero1 < numero2:
            print("El número 2, que es", numero2, ",es mayor que el número 1, que es", numero1)

    #Condición de fin del programa
        if numero1 == -1 and numero2 == -1:
            print("El programa ha finalizado") 
            break

# Porgrama: mayor()

# 6

def define_tres_numeros():
    """
    int, int, int = int, int, int
    Este programa le pide al usuario que introduzca tres números y devuelve el valor de los mismos. Si alguno de los valores no corresponde
    a un número entero, lanzará un mensaje de error.
        entrada: tres números enteros introducidos por el ususario.
        salida: devuelve los tres números enteros introducidos por el usuario.

    >>> define_tres_numeros()
    Introduce el número 1: 1
    Introduce el número 2: 2
    Introduce el número 3: 3
    1,2,3
    """
    try:
        numero1 = int(input("Introduce el número 1: "))
        numero2 = int(input("Introduce el número 2: "))
        numero3 = int(input("Introduce el número 3: "))

        return(numero1, numero2, numero3)

    except ValueError:
        raise ValueError("Todos los números deben ser números enteros (int)")

def mayor_de_tres():
    """
    int, int, int -> bool, str
    Este programa ordena de menor a mayor tres números introducidos por el ususario. El programa se ejecutará de forma indefinida hasta que 
    el usuario introduzca la condición de fin del programa.
        entrada: tres números enteros introducidos por el ususario.
        salida: los tres números enteros introducidos por el usuario de menor a mayor.

        >>> define_tres_numero()
    Introduzca -1 en todos los números para que el programa finalice
    Introduce el número 1: 1
    Introduce el número 2: 2
    Introduce el número 3: 3
    El número 1, que es  1 es menor que el número 2, que es  2 y el número 2 es menor que el número 3, que es  3
    1 < 2 < 3   

    Ejemplo de fin del programa
    >>> define_tres_numeros()
    Introduzca -1 en todos los números para que el programa finalice
    Introduce el número 1: -1
    Introduce el número 2: -1
    Introduce el número 3: -1
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca -1 en todos los números para que el programa finalice")

    #Cuerpo de la función
    while True:
        numero1, numero2, numero3 = define_tres_numeros()
        if numero1 < numero2 < numero3:
            print("El número 1, que es ", numero1, "es menor que el número 2, que es ", numero2, "y el número 2 es menor que el número 3, que es ", numero3)
            print(numero1, "<", numero2, "<", numero3)
        elif numero1 < numero2 > numero3:
            print("El número 1, que es ", numero1, "es menor que el número 2, que es ", numero2, "y el número 3 es menor que el número 2, siendo el número 3 el ", numero3)
            print(numero1, "<", numero3, "<", numero2)
        elif numero2 < numero1 < numero3:
            print("El número 2, que es ", numero2, "es menor que el número 1, que es ", numero1, "y el número 1 es menor que el número 3, que es ", numero3)
            print(numero2, "<", numero1, "<", numero3)
        elif numero2 < numero1 > numero3:
            print("El número 2, que es ", numero2, "es menor que el número 1, que es ", numero1, "y el número 3 es menor que el número 1, siendo el número 3 el ", numero3)
            print(numero2, "<", numero3, "<", numero1)
        elif numero3 < numero1 < numero2:
            print ("El número 3, que es ", numero3, "es menor que el número 1, que es ", numero1, "y el número 1 es menor que el número 2, que es ", numero2)
            print(numero3, "<", numero1, "<", numero2)
        else:
            print ("El número 3, que es ", numero3, "es menor que el número 1, que es ", numero1, "y el número 2 es menor que el número 1, siendo el número 2 el ", numero2)
            print (numero3, "<", numero2, "<", numero1)

    #Condición de fin del programa
        if numero1 == -1 and numero2 == -1 and numero3 == -1:
            print("El programa ha finalizado")
            break

# Programa: mayor_de_tres()

# 7

def introduce_codon():
    """
    str -> str
    Este programa le pide al usuario que introduzca el codón de interés y lo devuelve.
        entrada: el usuario introduce el codón de interés.
        salida: el programa devuelve el codón introducido por el ususario.

    >>> introduce_codon()
    Introduzca el codón: UUU
    UUU
    """
    try:
        codon = str(input("Introduzca el codón: "))
        return(codon)

    #Errores
    except ValueError:
        raise("El codón debe ser un str")

def aminoacido1 ():
    """
    Este programa nos va a devolver el aminoácido que corresponda el codón introducido por el ususario. El programa se ejecutará de forma
    indefinida hasta que el ususario introduzca la condición de salida del programa.
        entrada: el codón introducido por el ususario.
        salida: el aminoácido al que corresponde dicho codón.

    >>> aminoacido1():
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UUU
    El aminoácido es: fenilalanina
    
    Ejemplo de fin del programa
    >>> aminoacido1():
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UAA
    STOP
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca UAA, UAG o UGA para salir del programa")

    #Cuerpo de la función
    while True:
        codon = introduce_codon()
        if codon == "UUU":
            print("El aminoácido es: fenilalanina")
        elif codon == "UUC":
            print("El aminoácido es: fenilalanina")
        elif codon == "UUA":
            print("El aminoácido es: leucina")
        elif codon == "UUG":
            print("El aminoácido es: leucina")
        elif codon == "CUU":
            print("El aminoácido es: leucina")
        elif codon == "CUC":
            print("El aminoácido es: leucina")
        elif codon == "CUA":
            print("El aminoácido es: leucina")
        elif codon == "CUG":
            print("El aminoácido es: leucina")
        elif codon ==  "AUU":
            print("El aminoácido es: isoleucina")
        elif codon == "AUC":
            print("El aminoácido es: isoleucina")
        elif codon == "AUA":
            print("El aminoácido es: isoleucina")
        elif codon == "AUG":
            print("El aminoácido es: metionina")
        elif codon == "GUU":
            print("El aminoácido es: valina")
        elif codon == "GUC":
            print("El aminoácido es: valina")
        elif codon == "GUA":
            print("El aminoácido es: valina")
        elif codon == "GUG":
            print("El aminoácido es: valina")
        elif codon == "UCU":
            print("El aminoácido es: serina")
        elif codon == "UCC":
            print("El aminoácido es: serina")
        elif codon == "UCA":
            print("El aminoácido es: serina")
        elif codon == "UCG":
            print("El aminoácido es: serina")
        elif codon == "CCU":
            print("El aminoácido es: prolina")
        elif codon == "CCC":
            print("El aminoácido es: prolina")
        elif codon == "CCA":
            print("El aminoácido es: prolina")
        elif codon == "CCG":
            print("El aminoácido es: prolina")
        elif codon == "ACU":
            print("El aminoácido es: treonina")
        elif codon == "ACC":
            print("El aminoácido es: treonina")
        elif codon == "ACA":
            print("El aminoácido es: treonina")
        elif codon == "ACG":
            print("El aminoácido es: treonina")
        elif codon == "GCU":
            print("El aminoácido es: alanina")
        elif codon == "GCC":
            print("El aminoácido es: alanina")
        elif codon == "GCA":
            print("El aminoácido es: alanina")
        elif codon == "GCG":
            print("El aminoácido es: alanina")
        elif codon == "UAU":
            print("El aminoácido es: tirosina")
        elif codon == "UAC":
            print("El aminoácido es: tirosina")
        elif codon == "UAA":
            print("STOP")
        elif codon == "UAG":
            print("STOP")
        elif codon == "UGA":
            print("STOP")
        elif codon == "CAU":
            print("El aminoácido es: histidina")
        elif codon == "CAC":
            print("El aminoácido es: histidina")
        elif codon == "CAA":
            print("El aminoácido es: glutamina")
        elif codon == "AAU":
            print("El aminoácido es: glutamina")
        elif codon == "AAU":
            print("El aminoácido es: asparagina")
        elif codon == "AAC":
            print("El aminoácido es: asparagina")
        elif codon == "AAA":
            print("El aminoácido es: lisina")
        elif codon == "AAG":
            print("El aminoácido es: lisina")
        elif codon == "GAU":
            print("El aminoácido es: ácido aspártico")
        elif codon == "GAC":
            print("El aminoácido es: ácido aspártico")
        elif codon == "GAA":
            print("El aminoácido es: ácido glutámico")
        elif codon == "GAG":
            print("El aminoácido es: ácido glutámico")
        elif codon == "UGU":
            print("El aminoácido es: cisteina")
        elif codon == "UGC":
            print("El aminoácido es: cisteina")
        elif codon == "UGG":
            print("El aminoácido es: triptófano")
        elif codon == "GCU":
            print("El aminoácido es: arginina")
        elif codon == "GCC":
            print("El aminoácido es: arginina")
        elif codon == "GCA":
            print("El aminoácido es: arginina")
        elif codon == "GCG":
            print("El aminoácido es: arginina")
        elif codon == "AGU":
            print("El aminoácido es: serina")
        elif codon == "AGC":
            print("El aminoácido es: serina")
        elif codon == "AGA":
            print("El aminoácido es: arginina")
        elif codon == "AGG":
            print("El aminoácido es: arginina")
        elif codon == "GGU":
            print("El aminoácido es: glicina")
        elif codon == "GGC":
            print("El aminoácido es: glicina")
        elif codon == "GGA":
            print("El aminoácido es: glicina")
        elif codon == "GGG":
            print("El aminoácido es: glicina")

    #Errores
        if len(codon) != 3:
            raise ValueError("Un codón solo puede tener tres nucleótidos")
        if es_RNA(codon) == False:
            raise TypeError("El codón debe ser DNA")

    #Condición de fin del programa
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            print("El programa ha finalizado")
            break

# Programa: aminoacido1()

# 8
def aminoacido2 ():
    """
    Este programa nos va a devolver el aminoácido que corresponda el codón introducido por el ususario. El programa se ejecutará de forma
    indefinida hasta que el ususario introduzca la condición de salida del programa.
        entrada: el codón introducido por el ususario.
        salida: el aminoácido al que corresponde dicho codón.

    >>> aminoacido2()
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UUU
    El aminoácido que obtenemos del codón UUU es : Phe

    Ejemplo de fin del programa
    >>> aminoacio2()
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UAA
    El aminoácido que obtenemos del codón UAA es : Stop
    El programa ha finalizado
    """
    #Salida del programa 
    print("Introduzca UAA, UAG o UGA para salir del programa")

    #Cuerpo de la función
    while True:
        codon = introduce_codon()
        dic_codon = {
        "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
        "AUG": "Met",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "UAU": "Tyr", "UAC": "Tyr",
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",
        "CAU": "His", "CAC": "His",
        "CAA": "Gln", "CAG": "Gln",
        "AAA": "Lys", "AGG": "Lys",
        "GAU": "Asp", "GAC": "Asp", 
        "GAA": "Glu", "GAG": "Glu", 
        "UGU": "Cys", "UGC": "Cys", 
        "UGG": "Trp",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AGU": "Ser", "AGC": "Ser", 
        "AGA": "Arg", "AGG": "Arg",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    }
        print("El aminoácido que obtenemos del codón", codon, "es :", dic_codon[codon])

    #Errores
        if len(codon) != 3:
            raise ValueError("Un codón solo puede tener tres nucleótidos")
        if es_RNA(codon) == False:
            raise TypeError("El codón debe ser DNA")

    #Condición de fin de programa
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            print("El programa ha finalizado")
            break

# Programa: aminoacido2()

# 9 

import re
from types import resolve_bases

def aminoacido3():
    """
    Este programa nos va a devolver el aminoácido que corresponda el codón introducido por el ususario. El programa se ejecutará de forma
    indefinida hasta que el ususario introduzca la condición de salida del programa.
        entrada: el codón introducido por el ususario.
        salida: el aminoácido al que corresponde dicho codón.

    >>> aminoacido3()
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UUU
    El aminoácido es: phenylalanine

    Ejemplo de fin del programa
    >>> aminoacio3()
    Introduzca UAA, UAG o UGA para salir del programa
    Introduzca el codón: UAA
    No se ha encontrado el codón
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca UAA, UAG o UGA para salir del programa")

    #Cuerpo de la función
    while True:
        codon = introduce_codon()

        if re.match("GC.", codon):
            print("El aminoácido es: alanine") #alanina
        if re.match("UG[UC]", codon):
            print("El aminoácido es: cysteine") #cysteine
        if re.match("UC.|AG[UC]", codon):
            print("El aminoácido es: serine") #serine
        if re.match("GA[UC]", codon):
            print("El aminoácido es: apartic acid") #aspartic acid
        if re.match("GA[AG]", codon):
            print("El aminoácido es: glutamic acid") #glutamic acid
        if re.match("UU[UC]", codon):
            print("El aminoácido es: phenylalanine") #phenylalanine
        else:
            print("No se ha encontrado el codón")

    #Errores
        if len(codon) != 3:
            raise ValueError("Un codón solo puede tener tres nucleótidos")
        if es_RNA(codon) == False:
            raise TypeError("El codón debe ser DNA")

    #Condición de fin de programa
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            print("El programa ha finalizado")
            break

# Programa: aminoacido3()

def introduce_cadenas():
    """
    str, str -> str, str
    Este programa le pide al ususario que introduzca dos cadenas de DNA. El resultado será las dos cadenas que el ususario ha introducido.
        entrada: el usuario introduce las dos cadenas de DNA de interés
        salida: el programa devuelve las dos cadenas que el usuario ha introducido

    >>> introduce_cadenas()
    Introduce la primera cadena: ATG
    Introduce la segunda cadena: ATC
    ATG, ATC
    """
    try:
        p = str(input("Introduce la primera cadena: "))
        q = str(input("Introduce la segunda cadena: "))
        return(p,q)

    except ValueError:
        raise ValueError("Ambas cadenas deben ser cadenas de caracteres (str)")

def distancia_hammming(p, q):
    """
    str, str -> int
    Este programa nos va a indicar las diferencias o discrepancias existentes entre dos cadenas de igual longitud, comparando, nucleótido a nucleótido cada una de 
    las cadenas. En el momento en el que se encuentres una discrepancia, aumentará el contador 1. El resultado final será el número de discrepancias.
    El programa se ejecutará indefinidamente hasta que el ususario le ponga fin.
        entrada: dos cadenas de igual longitud
        salida: número de discrepancias que encontramos entre ambas cadenas

    >>> distancia_hamming()
    Introduce FIN en ambas cadenas para detener el programa
    Introduce la primera cadena: GGGCCGTTGGT
    Introduce la segunda cadena: GGACCGTTGAC
    3

    Ejemplo de fin de programa
    Introduce FIN en ambas cadenas para detener el programa
    Introduce la primera cadena: FIN
    Introduce la segunda cadena: FIN
    0
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduce FIN en ambas cadenas para detener el programa")

    #Cuerpo de la función 
    while True:
        p, q = introduce_cadenas()
        conta = 0
        
        for i in range(0, len(p)):
            if p[i] != q[i]:
                conta = conta + 1
            print(conta)

    #Condición de fin de programa
        if p == "FIN" and q == "FIN":
            print("El programa ha finalizado")
            break
    #Errores
        if len(p) != len(q):
            raise SyntaxError("Ambas cadenas deben tener la misma longitud")
        if es_DNA(p) or es_DNA(q) == False:
            raise SyntaxError("Ambas cadenas deben ser cadenas de DNA")

# Programa: distancia_hammming()

# 11

def entradas_ej11():
    """
    str, int -> str, int
    Este programa le va a pedir al usuario que introduzca el patrón a analizar y la distancia.
    El programa va a devolver el patrón y la distancia introducida por el ususario.
        entrada: el programa le pide al usuario que introduzca el patrón y la distancia
        salida: el programa devuelve el patrón y la distancia introducidas por el usuario

    >>> entradas_ej11()
    Introduzca el patrón: AAA
    Introduzca la distancia: 2
    AAA, 2
    """
    try: 
        patron1 = str(input("Introduzca el patrón: "))
    except TypeError:
        raise TypeError("El patrón debe ser una cadena de caracteres (str)")
    try:
        d = int(input("Introduzca la distancia: "))
    except ValueError:
        raise ValueError("La distancia debe ser un valor entero (int)")

    if d > len(patron1):
        raise SyntaxError("La distancia NO puede ser mayor que la longitud del patrón")
    if len(patron1) !=3:
        raise ValueError("La longitud del patrón NO puede ser mayor que 3, ya que estamos analizando tripletes")
    if es_DNA(patron1) == False:
        raise SyntaxError("El patrón debe ser un triplete de DNA")
    patron = patron1.upper()

    return (patron, d)

def vecinas1(patron):
    """
    str -> set
    Este programa va a encontrar las cadenas del mismo tamaño que el patron introducido por el ususario con una distancia de
    Hamming menor o igual que 1.
        entrada: una cadena patron de tamaño n.
        salida: un conjunto con las cadenas de tamaño n cuya distancia de
        Hamming respecto a patron sea menor o igual que 1.

    >>> vecinas1(patron)
    Introduzca el patron = AAA
    (['ACA', 'AAA', 'AAC', 'ATA', 'AAG', 'AGA', 'AAT', 'TAA', 'CAA', 'GAA'])
    """
    if type(patron) != str:
        raise TypeError("El patrón debe ser una cadena de caracteres (str)")

    vecinas = {patron}

    for i in range(0, len(patron)):
        simbolo = patron[:i]
        for nucleotidoX in "ACTG":
            vecina = simbolo + nucleotidoX + patron[i+1:]
            vecinas.add(vecina)

    return(vecinas)

def vecinas():
    """
    str, int -> set
    Este programa va a encontrar las cadenas del mismo tamaño que patron con una distancia de
    Hamming menor o igual que d. El programa se va a ejecutar de forma indefinida hasta que el ususario decida ponerle fin.
        entrada: una cadena patron de tamaño n y un número entero d.
        salida: un conjunto (o lista) con las cadenas de tamaño n cuya distancia de
        Hamming respecto a patron sea menor o igual que d.
    
    >>> vecinas()
    Introduzca el patrón: AAA
    Introduzca la distancia: 2
    ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 
    'AGT', 'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CGA', 
    'CTA', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GGA', 'GTA', 'TAA', 'TAC', 
    'TAG', 'TAT', 'TCA', 'TGA', 'TTA']

    Ejemplo de fin de programa
    Introduzca el patrón: FIN
    Introduzca la distancia: 1
    El programa ha finalizado
    """
    while True:
    #Salida del programa
        print("Para finalizar el programa escriba FIN en patrón y 1 en distancia")

    #Argumentos
        patron, d = entradas_ej11()
        vecinas = {patron}

    #Condición de fin de programa
        if patron == "FIN" and d == 1:
            print("El programa ha finalizado")
            break
    #Cuerpo de la función
        for i in range (d):
            for vecina in vecinas:
                vecinas = vecinas1(vecina).union(vecinas)
        print(sorted(vecinas))

# Programa: vecinas()

# 12

def entrada_ej12():
    """
    str, int -> str, int
    Este programa le va a pedir al ususario que introduzca el texto de interés y la k de interés y va a devolver estos argumentos.
        entrada: el proprama le solicita al usuario que introduzca la k y el texto
        salida: la k y el texto introducidos por el usuario

    >>> entrada_ej12()
    Introduzca la k: 4
    Introduzca el texto: ACGTTGCATGTCGCATGATGCATGAGAGCT
    4, ACGTTGCATGTCGCATGATGCATGAGAGCT
    """
    try:
        k1 = input("Introduzca la k: ")
        texto1 = input("Introduzca el texto: ")
        k1.upper()
        texto = texto1.upper()
        k2 = int(k1)

        if k2 > len(texto):
            raise TypeError("K debe ser menor que la longitud del texto")
        if es_DNA(texto) == False:
            raise SyntaxError("El texto debe ser una cadena de DNA")
        return(texto, k1)

    except ValueError:
        raise ValueError("K debe ser menor que la longitud del texto")

def contar():
    """
    str, int -> set
    Este programa va a contar el número de veces que aparezca cada patrón de una distancia determinada y nos va a devolver los o el patrón más frecuente
    de un texto determinado. El programa se ejecutará de forma indefinida hasta que el usuario decida ponerle fin.
        entrada: la k y el texto introducidos por el ususario
        salida: el/los kmero/s más frecuente/s

    >>> contar()
    Para salir del programa ponga FIN en la entrada del texto y 1 en la k
    Introduzca la k: 4
    Introduzca el texto: ACGTTGCATGTCGCATGATGCATGAGAGCT
    ['GCAT', 'CATG']

    Ejemplo de fin del programa
    >>> contar()
    Para salir del programa ponga FIN en la entrada del texto y 1 en la k
    Introduzca la k: 1
    Introduzca el texto: FIN
    El programa ha finalizado
    """
    #Salida del programa
    print("Para salir del programa ponga FIN en la entrada del texto y 1 en la k")
    
    #Argumentos de la función
    while True:
        cuenta = {}
        texto, k2 = entrada_ej12()
        max_apariciones = 0

    #Condición de salida del programa
        if texto == "FIN" and k2 == 1:
            print("El programa ha finalizado")
            break

    #Cuerpo de la función
        k = int(k2)

        for i in range(0, len(texto)-k+1):
            patron = texto[i: i+k]
            if patron in cuenta:
                cuenta[patron] = cuenta[patron] + 1
            else:
                cuenta[patron] = 1
    #Resultados
        max_apariciones = max(cuenta.values()) #máxima cuenta
        resultado = [clave for clave, valor in cuenta.items() if valor == max_apariciones] #kmero más frecuente
        print(resultado)

# Programa: contar()

# 13

def entrada_ej13():
    """
    str, str -> str, str
    Este programa le va a pedir al ususario que introduzca el texto de interés y el patrón de interés y va a devolver estos argumentos.
        entrada: el proprama le solicita al usuario que introduzca el patrón y el texto
        salida: el patrón y el texto introducidos por el usuario

    >>> entrada_ej13()
    Introduzca el patrón: ATAT
    Introduzca el texto: GATATATGCATATACTT
    ATAT, GATATATGCATATACTT
    """
    try:
        patron1 = str(input("Introduzca el patrón: "))
        texto1 = str(input("Introduzca el texto: "))
        patron = patron1.upper()
        texto = texto1.upper()

        if len(patron) > len(texto):
            raise TypeError("La longitud del patrón no puede ser mayor que la longitud del texto")
        if es_DNA(patron) or es_DNA(texto) == False:
            raise SyntaxError("El texto y el patrón deben ser cadenas de DNA")

        return(patron, texto)

    except ValueError:
        raise ValueError("La longitud del patrón no puede ser mayor que la longitud del texto")

def BusquedaPatron():
    """
    str, str -> set
    Este programa encuentra todas las ocurrencias de un patrón en un texto. Nótese que el patrón puede solaparse.
        entrada: cadenas patrón y texto.
        salida: lista con todas las posiciones iniciales de patrón en texto

    >>> BusquedaPatron()
    Introduzca FIN en el patrón y FIN en el texto para finalizar el programa
    Introduzca el patrón: ATAT
    Introduzca el texto: GATATATGCATATACTT
    [1, 3, 9]

    Ejemplo de fin del programa
    >>> BusquedaPatron()
    Introduzca FIN en el patrón y FIN en el texto para finalizar el programa
    Introduzca el patrón: FIN
    Introduzca el texto: FIN
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca FIN en el patrón y FIN en el texto para finalizar el programa")

    #Argumentos de la función
    while True:
        patron, texto = entrada_ej13()
        ocurrencias = []

    #Condición de salida del programa
        if patron == "FIN" and texto == "FIN":
            print("El programa ha finalizado")
            break
    
    #Cuerpo de la función
        for i in range(0, len(texto)-len(patron)+1):
            if texto[i: i+len(patron)] == patron:
                ocurrencias.append(i)

    #Resultado
        print(ocurrencias)

# Programa: BusquedaPatron()

# 14

def entrada_ej14():
    """
    str, str, int -> str, str, int
    Este programa le va a pedir al usuario que introduzca el patrón, el texto y la d de interés y va a devolver los valores introducidos por el ususario.
        entrada: el programa le pide al ususario que introduzca el patrón, texto y d deseada.
        salida: los valores de las variables introducidas

    >>> entrada_ej14()
    Introduzca el patrón: ATTCTGGA
    Introduzca el texto: CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
    Introduzca la d: 3
    ATTCTGGA, CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC, 3
    """
    try:
        patron1 = str(input("Introduzca el patrón: "))
        texto1 = str(input("Introduzca el texto: "))
        d1 = input("Introduzca la d: ")

        patron = patron1.upper()
        texto = texto1.upper()
        d = int(d1)

        if d > len(patron1) or len(patron1) > len(texto1):
            raise TypeError("La d no puede ser mayor que la longitud del patrón y la longitud del patrón no puede ser mayor que la longitud del texto")
        if es_DNA(patron1) or es_DNA(texto1) == False:
            raise SyntaxError("El patrón y el texto deben ser cadenas de DNA")
        
        return(patron, texto, d1)

    except ValueError:
        raise ValueError("La d no puede ser mayor que la longitud del patrón y la longitud del patrón no puede ser mayor que la longitud del texto")

def distancia_hamming2(p, q):
    distancia_hamm = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            distancia_hamm = distancia_hamm + 1
    return distancia_hamm

def BusquedaAproximadaPatron():
    """
    str, str, int -> diccionario
    Este programa va a devolver en un set el número de veces que se encuentre un patrón determinado teniendo en cuenta que se acepta
    una discrepancia máxima especificadada de d. El programa se ejecutará de forma automática hasta que el ususario decida ponerle fin.
        entrada: el patrón, texto y la d introducidas por el usuario
        salida: el diccionario con el número de veces que se encuentra el patrón exacto y el patrón aproximado con la d aceptada

    >>> BusquedaAproximadaPatron()
    Introduzca FIN en el patrón, FIN en el texto y 1 en d para finalizar el programa
    Introduzca el patrón: ATTCTGGA
    Introduzca el texto: CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
    Introduzca la d: 3
    [6, 7, 26, 27, 78]

    Ejemplo de fin de programa
    Introduzca FIN en el patrón, FIN en el texto y 1 en d para finalizar el programa
    Introduzca el patrón: FIN
    Introduzca el texto: FIN
    Introduzca la d: 1
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca FIN en el patrón, FIN en el texto y 1 en d para finalizar el programa")

    #Argumentos de la función
    while True:
        patron, texto, d1 = entrada_ej14()
        posiciones = []
        
        d = int(d1)

    #Condición de salida del programa
        if patron == "FIN" and texto == "FIN" and d == 1:
            print("El programa ha finalizado")
            break
    
    #Cuerpo de la función
        for i in range(0, len(texto) - len(patron)+1):
            palabra = texto[i: i + len(patron)]
            if distancia_hamming2(palabra, patron) <= d:
                posiciones.append(i)
    #Resultado
        print(posiciones)
        
# Programa: BusquedaAproximadaPatron()

# 15

def entrada_ej15():
    """
    str, int, int -> str, int, int
    Este programa le va a pedir al ususario que introduzca el texto, la k y la d de interés y va a devolver dichos valores.
        entrada: el programa le pide al usuario que introduzca el texto, la k y la d
        salida: el programa va a devolver los argumentos introducidos por el usuario

    >>> entrada_ej15()
    Introduzca el texto: ACGTTGCATGTCGCATGATGCATGAGAGCT
    k = 4
    d = 1
    ACGTTGCATGTCGCATGATGCATGAGAGCT, 4, 1
    """
    try:
        texto1 = input("Introduzca el texto: ")
        k1 = input("Introduzca la k: ")
        d1 = input("Introduzca la d(discrepancias): ")

        texto = texto1.upper()
        k = int(k1)
        d = int(d1)

        if k > len(texto) or d > len(texto) or k < d:
            raise TypeError("El texto debe ser mayor que la k y la d, y la k debe ser mayor que el número de discrepancias")
        return(texto, k1, d1)

    except ValueError:
        raise ValueError("El texto debe ser mayor que la k y la d, y la k debe ser mayor que el número de discrepancias")

def contar_discrepancias(texto, patron, d):
    """
    str, str, int -> int
    Este programa va a contar el número de veces que aparezca una palabra distinta dependiendo del número de discrepancias que acepte.
        entrada: el texto, patrón y d introducidas por el usuario
        salida: la cuenta de las distintas palabras distintas dependiendo de sus discrepancias
    """
    conta = 0
    for i in range(0, len(texto)-len(patron)+1):
        palabra = texto[i: i+len(patron)]
        if distancia_hamming2(palabra, patron) <= d:
            conta = conta +1

    return(conta)


def PalabrasFrecuentesDiscrepancias():
    """
    str, int, int -> diccionario
    Este programa va a encontrar las palabras frecuentes en un texto con hasta un número máximo de discrepancias.
    Este programa se ejecutará de forma automática hasta que el usuario decida ponerle fin.
        entrada: una cadena texto, un entero k con la longitud de la palabra y un entero d con el número máximo de discrepancias.
        salida: una lista con los k-meros más frecuentes en texto con hasta d discrepancias.

    >>> PalabrasFrecuentesDiscrepancias()
    Introduzca FIN en texto, 1 en k y 1 en d para salir del programa
    Introduzca el texto: ACGTTGCATGTCGCATGATGCATGAGAGCT
    Introduzca la k: 4
    Introduzca la d(discrepancias): 1
    ['ATGT', 'GATG', 'ATGC']

    Ejemplo de fin de programa
    Introduzca FIN en texto, 1 en k y 1 en d para salir del programa
    Introduzca el texto: FIN
    Introduzca la k: 1
    Introduzca la d(discrepancias): 1
    El programa ha finalizado
    """
    #Salida del programa
    print("Introduzca FIN en texto, 1 en k y 1 en d para salir del programa")

    #Argumentos
    while True:
        texto, k1, d1 = entrada_ej15()

        k = int(k1)
        d = int(d1)
        kmeros = {}

    #Condición de salida del programa
        if texto == "FIN" and k == 1 and d == 1:
            print("El programa ha finalizado")
            break

    #Cuerpo de la función

        for i in range(0, len(texto) -k +1):
            palabra = texto[i:i+k]
            if palabra not in kmeros.keys():
                kmeros[palabra] = contar_discrepancias(texto, palabra, d)

    #Resultados

        maximo_kmero = max(kmeros.values()) #kmeros que más puntuación han obtenido
        kmeros_más_frecuentes = [muestra for muestra in kmeros.keys() if kmeros[muestra] == maximo_kmero]

        print("El/los kmero/s más frecuentes: ", kmeros_más_frecuentes)

# Programa: PalabrasFrecuentesDiscrepancias()

        















































        












        
        

    





    


















