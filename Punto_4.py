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