import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Federico
apellido:   Deniard

para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  "
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        primer_nombre = prompt(title="", prompt="Ingrese el nombre del primer pasajero")
        second_name = prompt(title="", prompt="Ingrese el nombre del primer pasajero")
        primer_edad = prompt(title="", prompt=f"Ingrese la edad de {primer_nombre}:")
        primer_edad = int(primer_edad)
        segunda_edad = prompt(title="", prompt=f"Ingrese la edad de {second_name}:")
        segunda_edad = int(segunda_edad)
        edad_promedio = (primer_edad + segunda_edad) / 2
        primer_peso = prompt(title="", prompt=f"Ingrese el peso de {primer_nombre}:")
        primer_peso = int(primer_peso)
        segundo_peso = prompt(title="", prompt=f"Ingrese el peso de {second_name}:")
        segundo_peso = int(segundo_peso)
        total_kilos = primer_peso + segundo_peso
        total_kilos = int(total_kilos)
        precio_total = total_kilos * 1000
        precio_total = int(precio_total)
        alert("",f"Hola {primer_nombre} y {second_name}, sus pesos son {primer_peso} kilos y {segundo_peso} kilos respectivamente,\n sumados da {total_kilos} kilos, el promedio de edad es {edad_promedio} y su viaje vale {precio_total} pesos")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
