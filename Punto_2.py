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