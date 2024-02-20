import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Federico
apellido:   Deniard
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mayor_votos = None
        candidato_mayor_votos = ""
        menor_votos = None
        candidato_menor_votos = ""
        edad_menor_votos = 0
        promedio_edad = 0
        total_votos = 0
        contador = 0
        while True:
            candidato = prompt("","Ingrese el nombre del candidato")
            if candidato == None:
                break
            edad = prompt("","Ingrese la edad del candidato")
            votos = prompt("","Ingrese la cantidad de votos")
            edad = int(edad)
            votos = int(votos)
            promedio_edad += edad
            total_votos += votos
            if contador == 0:
                mayor_votos = votos
                menor_votos = votos
                candidato_mayor_votos = candidato
                candidato_menor_votos = candidato
                edad_menor_votos = edad
            elif votos > mayor_votos:
                mayor_votos = votos
                candidato_mayor_votos = candidato
            elif votos < menor_votos:
                menor_votos = votos
                candidato_menor_votos = candidato
                edad_menor_votos = edad
            contador += 1


        promedio_edad = promedio_edad / contador
        alert("",f"El candidato con más votos es {candidato_mayor_votos} \n El candidato con menos votos es {candidato_menor_votos} y su edad es: {edad_menor_votos}\n El promedio de la edad de los candidatos es: {promedio_edad}\n El total de los votos fue de: {total_votos} ")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
