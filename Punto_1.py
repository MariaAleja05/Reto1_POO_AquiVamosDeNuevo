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