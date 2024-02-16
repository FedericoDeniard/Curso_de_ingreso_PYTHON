import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Federico
apellido:   Deniard
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        while True:
            numero = prompt("","Ingrese un número")

            if numero == None:
                break

            numero = int(numero)
            if(numero > 0):
                cantidad_positivos += 1
                suma_positivos += numero
            elif(numero < 0):
                cantidad_negativos +=1
                suma_negativos += numero
            else:
                cantidad_ceros += 1
            print("",f"suma positivos: {suma_positivos}\n suma negativos: {suma_negativos}")

        diferencia_positivos_negativos = cantidad_positivos - cantidad_negativos
        diferencia_mensaje = ""
        if(diferencia_positivos_negativos > 0):
            diferencia_mensaje = f"Se ingresaron {diferencia_positivos_negativos} números positivos más que negativos"
        elif(diferencia_positivos_negativos < 0):
            diferencia_positivos_negativos = abs(diferencia_positivos_negativos)
            diferencia_mensaje = f"Se ingresaron {diferencia_positivos_negativos} números negativos más que positivos"
        else:
            diferencia_mensaje = "Se ingresó la misma cantidad de números negativos y positivos"
        alert("", f"Suma de los negativos: {suma_negativos}\n Suma de los positivos: {suma_positivos}\n Cantidad positivos: {cantidad_positivos}\n Cantidad negativos: {cantidad_negativos}\n Cantidad ceros: {cantidad_ceros}\n Diferencia entre positivos y negativos: {diferencia_mensaje}")



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
