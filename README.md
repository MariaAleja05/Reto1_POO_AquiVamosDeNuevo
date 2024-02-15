# Reto número 1 repo POO

 ### **Fecha:** 14-02-2024

**1.** Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).

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

    for i in range(longitud_palabra):       # Para verificar si el caracter en la ubicación en la palabra original y la invertida es el ismo
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

* Mirar archivo Punto_3.py

```python
code
```

**4.** Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

* Mirar archivo Punto_4.py

```python
code
```

**5.** Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

* Mirar archivo Punto_5.py

```python
code
```
