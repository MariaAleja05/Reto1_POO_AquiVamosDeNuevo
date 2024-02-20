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
