#Algoritmo de generaccion de contraseñas seguras
import tkinter as tk
from tkinter import messagebox
import random

contrasena_global = ""

def generador_contrasena_segura(longitud):

    # Conjunto de caracteres posibles
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>/?"
        
    # Generación de la contraseña xd
    
    contrasena = ""
    for _ in range(longitud):
        # Selecciona un carácter aleatorio de la cadena 'caracteres'
        caracter_aleatorio = random.choice(caracteres)
        contrasena += caracter_aleatorio

    return contrasena
#funcion para validar contraseña
def revisar_contrasenas(contrasena):
    contiene_mayuscula =  any(c.isupper() for c in contrasena)
    contiene_minuscula =  any(c.lower() for c in contrasena)
    contiene_numeros =  any(c.isdigit() for c in contrasena)
    contiene_especiales =  any(c in "!@#$%^&*()_+-=[]{}|;:,.<>/?" for c in contrasena)

#cumplimiento de parametros
    criterios_cumplidos = sum([contiene_mayuscula, contiene_minuscula, contiene_numeros, contiene_especiales])
    if criterios_cumplidos == 4:
        return "Alta"
    elif criterios_cumplidos >= 2:
        return "Media"
    else:
        return "Debil"

#funcion para validar la longitud
def generar_contrasena():
    try:
        entrada = entrada_longitud.get()
        longitud = int(entrada)
        if longitud < 8:
            messagebox.showwarning("AVISO", "La longitud de la contraseña no cumple con lo requido")
            return
        elif longitud > 16:
            messagebox.showwarning("AVISO", "La longitud de la contraseña no cumple con lo requido")
            return
        global contrasena_global
        contrasena_global = generador_contrasena_segura(longitud)
        #permitir que entrada de texto
        contrasena_generada.config(state='normal')
        #limpiar el cuadro de texto
        contrasena_generada.delete(1.0, tk.END)
        contrasena_generada.insert(tk.END, f"La longitud es: {longitud}. la contraseña generada es: f{contrasena_global}")
        #no permitir ingresar texto
        contrasena_generada.config(state='disabled')
    
    #validacion de exepcion
    except ValueError:
        messagebox.showerror("ERROR","Los caracteres ingresado no son validos")

#valiacion de la fortaleza de la contraseña
def validar_contraseña():
    global contrasena_global
    if contrasena_global:
        seguridad_contraseña = revisar_contrasenas(contrasena_global)
        messagebox.showinfo("Informacion", f"La contraseña tiene nivel de seguridad:{seguridad_contraseña}")
    else:
        messagebox.showerror("Error", "La contraseña validada no existe")


#funcion para limpiar campos
def limpiar_campo():
    entrada_longitud.delete(0, tk.END)
    #permitir que entrada de texto
    contrasena_generada.config(state='normal')
    #limpiar el cuadro de texto
    contrasena_generada.delete(1.0, tk.END)
    #no permitir ingresar texto
    contrasena_generada.config(state='disabled')


# creacion de ventana principal
ventana = tk.Tk()
ventana.title("Generador de contraseñas")

etiqueta_longitud =  tk.Label(ventana, text="Escriba la longitud de su contraseña (mínimo 8, máximo 16):")
etiqueta_longitud.pack()

entrada_longitud = tk.Entry(ventana)
entrada_longitud.pack()

#creacion de boton
boton_generar = tk.Button(ventana, text="Gererar Contraseña", command=generar_contrasena)
boton_generar.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar Campo", command=limpiar_campo)
boton_limpiar.pack()

#campo de contraseña generada
contrasena_generada = tk.Text(ventana, height=4, width=45, state="disabled")
contrasena_generada.pack()

#validar contraseña si es robusta
Boton_validar_contra = tk.Button(ventana, text="Validar Contraseña", command=validar_contraseña)
Boton_validar_contra.pack()


if __name__ == "__main__":
    ventana.mainloop()