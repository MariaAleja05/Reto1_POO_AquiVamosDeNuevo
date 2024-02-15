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