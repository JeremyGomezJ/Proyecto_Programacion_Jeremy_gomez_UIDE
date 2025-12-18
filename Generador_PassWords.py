
#Algoritmo de generaccion de contraseñas seguras
import tkinter as tk
import random
def generador_contrasena_segura():

    # Conjunto de caracteres posibles
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>/? "
    
    longitud = 0
    
    # Entrada y Validación
    
    while not (8 <= longitud <= 16):
        try:
            # Solicitud de la longitud
            entrada = input("Escriba la longitud de su contraseña (mínimo 8, máximo 16): ")
            
            # Intentar convertir la entrada a un entero
            longitud = int(entrada)
            
            # Validación de la longitud
            if longitud < 8:
                print("¡AVISO! La Contraseña es muy corta. La longitud minima es de 8.")
            elif longitud > 16:
                print("¡AVISO! La Contraseña es muy larga. La longitud máxima es de 16.")
            # Si la longitud está entre 8 y 16, el bucle terminará
                
        except ValueError:
            # Muestra si la entrada no es un número entero
            print("¡ERROR! Entrada inválida. Por favor, introduzca un número entero.")
            
    # Generación de la contraseña xd
    
    contrasena = ""
    for _ in range(longitud):
        # Selecciona un carácter aleatorio de la cadena 'caracteres'
        caracter_aleatorio = random.choice(caracteres)
        contrasena += caracter_aleatorio
        
    # Salida de la funcion
    
    print("-" * 40)
    print(f"La contraseña generada de {longitud} caracteres es: {contrasena}")
    print("-" * 40)

if __name__ == "__main__":
    generador_contrasena_segura()