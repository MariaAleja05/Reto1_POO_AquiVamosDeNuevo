# Reto número 1 repo POO

 ### **Fecha:** 14-02-2024

**1.** Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

La función main le solicita al usuario ingresar los 2 números con los que desea realizar la operación correspondiente. Además, se le solicita ingresar el simbolo correspondiente a la operación que desea realizar entre ellos. Se llama la función "operaciones", la cual está compuesta por un condicional que realizará la operación requerida que haya seleccionado el usuario en la función main. La función retornará el resultado de la operación.

* Mirar archivo Punto_1.py

```python
suma = 0          # Se definen variables
resta = 0
divi = 0
multi = 0
num1 : float = 0
num2 : float = 0
operacion: str

def operaciones(num1, num2, operacion): # Función para realizar la operación deseada, con valores de entrega establecidos por el usuario
    if operacion == "+":
        suma = num1 + num2
        print("El resultado de la suma es: " + str(suma))

    elif operacion == "-":
        resta = num1 - num2
        print("El resultado de la resta es: " + str(resta))

    elif operacion == "/":
        if num2 != 0:         # Si se puede realizar la división cuando el segundo número es diferente de cero
            divi = num1 / num2
            print("El resultado de la división es: " + str(divi))
        else:                 # No se puede realizar la división cuando el segundo número es cero
            print("Los números ingresados no son válidos para realizar la operación")

    elif operacion == "*":
        multi = num1 * num2
        print("El resultado de la multiplicación es: " + str(multi))

if __name__ == "__main__":    # Función main para que el usuario ingrese los números y operación a realizar entre estos
    operacion = input("Ingrese '+' si desea realizar una suma; '-' si desea realizar una resta; '/' si desea realizar una división; '*' si desea realizar una multiplicación: ")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operaciones(num1, num2, operacion)    # Se llama la función operaciones para que se realice el calculo entre los números
```

**2.** Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

La función main le solicita al usuario ingresar la palabra que desea verificar si es un palíndromo, se llama la función "verificar_si_es_palíndromo" para realizar las operaciones correspondientes. Esta función hace usos de varios for para invertir el orden de los caracteres de la palabra original, si al invertirla la posición de los caracteres es el mismo se mostrara un mensaje informando que si es un palíndromo, de lo contrario, se mostrará que no lo es.

* Mirar archivo Punto_2.py

```python
palabra: str         # Se definen variables
palabra_min: str     
caracteres = []
longitud_palabra = 0
palabra_al_reves : str

def verificar_si_es_palíndromo(palabra): # Función para verificar si la palabra ingresada es un palíndromo
    palabra_min = palabra.lower()
    longitud_palabra = len(palabra_min)
    
    for i in range (longitud_palabra - 1, -1, -1): # Para colocar la palabra ingresada al revés
        caracteres.append(palabra_min[i])
    
    palabra_al_reves = ''.join(caracteres)  # Para volver esos caracteres de la palabra al reves en un str

    for i in range(longitud_palabra):       # Para verificar si el caracter en la ubicación en la palabra original y la invertida es el mismo
        if palabra_min[i]==palabra_al_reves[i]:
            continue
        else:
            print("La palabra ingresada NO es un palíndromo")
            return                          # Se detiene el for ya que encontró una letra que no coincide
        
    print("La palabra " + "'" + palabra_min + "'" + " SI es un palíndromo")   # Mostrara que si es un palíndromo

if __name__ == "__main__":    # Función main para que el usuario ingrese los números y operación a realizar entre estos
    palabra = input("Ingrese la palabra: ")
    verificar_si_es_palíndromo(palabra)    # Se llama la función para ver si la palabra ingresada es un palíndromo
```

**3.** Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

En la función main se le pide al usuario ingresar la cantidad de elementos que tendrá su lista, luego haciedo uso de un for se le solicita ingresar esa cantidad de números a la lista, se llama la función "verificar_si_es_primo". Dentro de esta función hay un for anidado, en el cual, se va seleccionando cada elemento de la lista y se busca cuales son sus divisores; si al final de este proceso con cada número la cantidad de divisores de ese número seleccionado es igual a 2 se va a añadir el elemento a la lista de números primos (ya que se cumple la condición de que solamente sea divisible por 1 y por el mismo) y se procederá a evaluar los divisores del siguiente número. Finalmente un condicional if evalua si hay elementos dentro de la lista números primos, y de haberlos, procede a mostrarle al usuario cuáles de los números ingresados son primos.

* Mirar archivo Punto_3.py

```python
cantidad_numeros: int = 0       # Se definen variables
num: int = 0
contador_divisores: int = 0
lista_usuario = []
lista_primos = []

def verificar_si_es_primo(lista_usuario): # Función para verificar si los números son primos
    
    for i in lista_usuario:               # Es un for para ir evaluando si es primo cada número de la lista
        contador_divisores = 0            # Para saber cuantos divisores tiene, si tiene más de 2 entonces no es un número primo
        for j in range(1, i+1):           # Va buscando todos los divisores posibles desde 1 hasta ese mismo número que se está evaluando
            if i % j == 0:                # Si es divisible si el residuo es cero
                contador_divisores = contador_divisores+1   # Si es un divisor se le suma 1 al contador
        if contador_divisores == 2:       # Si el número tiene solo 2 divisores se cuenta como número primo
            lista_primos.append(i)        # Se añade el número primo a su lista correspondiente
    
    if len(lista_primos) != 0:            # Si la longitud de la lista es diferente de cero se mostrarán los número primos ingresados
        print("De los números ingresados son primos los siguientes: ")
        print(lista_primos)
    else:                                 # Si la lista de números primos no tiene elementos significa que no hay npumero primos
        print("No hay algún número primo")

if __name__ == "__main__":    # Función main para que el usuario ingrese los números y operación a realizar entre estos
    cantidad_numeros = int(input("Ingrese la cantidad de números de la lista: "))
    for i in range (cantidad_numeros):      # Un for que se repite según la cantidad de números que desea ingresar el usuario
        num = int(input("Ingrese el número entero: "))
        lista_usuario.append(num)
    verificar_si_es_primo(lista_usuario)   # Se llama la función para ver si los números ingresados son primos
```

**4.** Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

En la función main se le pide al usuario ingresar la cantidad de elementos que tendrá su lista, luego haciedo uso de un for se le solicita ingresar esa cantidad de números a la lista, se llama la función "mayor_suma". Dentro de esta función hay un for que va realizando la suma de dos números consecutivos de la lista y se va estableciendo en la variable mayor_suma, cada vez que el programa realice una nueva suma se comparará con el resultado anterior; en caso de ser mayor el nuevo ese será el nuevo valor de la variable, de lo contrario se seguira comparando con la suma anterior. Luego de evaluar todas las sumas el programa mostrará la de mayor valor.

* Mirar archivo Punto_4.py

```python
lista_usuario = []

def mayor_suma(lista_usuario): # Función para ver cual es la mayor suma entre 2 números consecutivos
    suma_actual = 0
    mayor_suma = 0
    for i in range (cantidad_numeros-1):          # Se repetira la cantidad de números ingresados -1 porque es la cantidad de grupos consecutivos que se pueden armar
        suma_actual = lista_usuario[i]+lista_usuario[i+1]           # Suma los elementos consecutivos
        if mayor_suma>=suma_actual:               # Si el valor de mayor suma es mayor a la suma realizada se seguiran mirando otras sumas de pareja para ver si alguna mayor
            continue
        else:                                     # Cuando se encuantra una suma mayor a la anterior se cambia ese nuevo mayor para ser el estandar de comparación
            mayor_suma=suma_actual
    print("La mayor suma de 2 elementos de la lista consecutivos es: " + str(mayor_suma))

if __name__ == "__main__":    # Función main para que el usuario ingrese la lista de números
    cantidad_numeros = int(input("Ingrese la cantidad de números de la lista: "))
    for i in range (cantidad_numeros):      # Un for que se repite según la cantidad de números que desea ingresar el usuario
        num = int(input("Ingrese el número entero: "))
        lista_usuario.append(num)
    mayor_suma(lista_usuario)   # Se llama la función para ver cual es la mayor suma entre 2 números consecutivos
```

**5.** Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

En la función main se le pide al usuario ingresar la cantidad de elementos que tendrá su lista, luego haciedo uso de un for se le solicita ingresar esa cantidad de palabras a la lista, se llama la función "igualdad_caracteres". Dentro de esta función hay un primer for el cual ordenará los caracteres de cada palabra en orden alfabetico; un segundo for que evalua si hay palabras repetidas dentro de la lista ya que por defecto tendrán los mismos caracteres, estas palabras se irán añadiendo a la lista de palabras repetidas; un tercer for revisa si dentro de la lista de elementos ordenados alfabeticamente hay alguno que sea igual para añadirlo a loa lista de "mismos_caracteres"; finalmente se sumarán esas dos listas obtenidas para mostrarle al usuario cuales de esas palabras tienen los mismos caracteres.

* Mirar archivo Punto_5.py

```python
lista_usuario = []
lista_copia = []
lista_palabras_repetidas = []
lista_mismos_caracteres = []

def igualdad_caracteres(lista_usuario, lista_copia, lista_palabras_repetidas, lista_mismos_caracteres): 
    for i in lista_usuario:             # Va tomando cada palabra de a lista
        i = ''.join(sorted(i))          # Ordena las letras de la palabra en orden alfabetico para que sea más fácil compararlas
        lista_copia.append(i)           # Se añaden a la lista donde se van a poner todas las palabras con sus letras en orden alfabetico 
           
           # Este for es para mirar si hay palabras repetidas que por defeto tendrán los mismos caracteres
    for j in range(len(lista_usuario)): # Toma la primera palabra a comparar
        for k in range(len(lista_usuario)): # Toma la segunda palabra a comparar
            if j == k:                  # No se compara la palabra con ella misma
                continue
            else:
                if lista_usuario[j] == lista_usuario[k]:  # Si hay dos elementos con caracteres iguales 
                    if lista_usuario[j] in lista_palabras_repetidas:    # Si no esta en la lista se agrega
                        continue
                    else:
                        lista_palabras_repetidas.append(lista_usuario[j])   # Se añade a palabras repetidas porque no es una nueva

            # Este for es para mirar las palabras que quedaron con los caracteres ordenados en orden alfabetico
            # Misma lógica que el anterior for anidado
    for i in range(len(lista_copia)):
        for k in range(len(lista_copia)):
            if i == k:
                continue
            else:
                if lista_copia[i] == lista_copia[k]:
                    if lista_usuario[i] in lista_mismos_caracteres:
                        continue
                    else:
                        lista_mismos_caracteres.append(lista_usuario[i])
        
        # Ahora se suman ambas listas resultantes de los for anteriores
            # La lista de las palabras que estan escritas más de una vez y que por defecto tienen la misma cantidad de caracteres
            # La lista de las palabras que tienen los mismos caracteres sin estar repetidas           
    
    lista_mismos_caracteres = lista_mismos_caracteres + lista_palabras_repetidas
    
    print("Las palabras que tienen los mismos caracteres son: " + str(lista_mismos_caracteres))

if __name__ == "__main__":
    cantidad_palabras = int(input("Ingrese la cantidad de palabras de la lista: "))  
    for i in range(cantidad_palabras):            # Un for que se repite según la cantidad de números que desea ingresar el usuario
        palabra = input("Ingrese la palabra: ")  
        lista_usuario.append(palabra)
    igualdad_caracteres(lista_usuario, lista_copia, lista_palabras_repetidas, lista_mismos_caracteres)     # Se llama la función
```
