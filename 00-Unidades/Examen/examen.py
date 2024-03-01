import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre:     Federico
Apellido:   Deniard

De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
Informe B- El porcentaje de mascotas femeninas y el de las masculinas.
Informe C -El tipo de la mascota más pesada
Informe D- El nombre del gato más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Examen")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        total_mascotas = 5

        gato = 0
        perro = 0
        exotico = 0

        tipo_mas_ingresado = "" 

        tipo_mascota_mas_pesada = ""
        peso_mascota_mas_pesada = 0

        nombre_gato_joven = ""
        edad_gato_joven = None

        suma_peso_mascotas = 0

        masculinos = 0
        femeninos = 0

        for i in range (total_mascotas):
            nombre = prompt("","Ingrese el nombre de la mascota")

            tipo = prompt("","Seleccione el tipo de mascota")
            if tipo != "perro" and tipo != "gato":
                tipo = "exotico"
            
            peso = prompt("","Ingrese el peso de la mascota")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = prompt("","Ingrese un peso entre 10kg y 80kg")
                peso = int(peso)
            
            sexo = prompt("","Igrese el sexo de la mascota (f o m)")
            while sexo != "f" and sexo != "m":
                sexo = prompt("","Igrese el sexo de la mascota (f o m)")
            
            edad = prompt("","Ingrese la edad de la mascota")
            edad = int(edad)
            while edad < 1:
                edad = prompt("","Ingrese una edad válida")
                edad = int(edad)

            match tipo:
                case "gato":
                    gato += 1
                    if edad_gato_joven == None:
                        edad_gato_joven = edad
                        nombre_gato_joven = nombre
                    elif edad_gato_joven  > edad:
                        edad_gato_joven = edad
                        nombre_gato_joven = nombre
                case "perro":
                    perro +=1
                case _:
                    exotico += 1

            match sexo:
                case "f":
                    femeninos += 1
                case "m":
                    masculinos += 1

            if peso_mascota_mas_pesada == 0:
                peso_mascota_mas_pesada = peso
                tipo_mascota_mas_pesada = tipo
            elif peso_mascota_mas_pesada < peso:
                peso_mascota_mas_pesada = peso
                tipo_mascota_mas_pesada = tipo

            suma_peso_mascotas += peso

            

        if gato > perro and gato > exotico:
            tipo_mas_ingresado = "gato"
        elif perro > exotico:
            tipo_mas_ingresado = "perro"
        else:
            tipo_mas_ingresado = "exotico"
        

        porcentaje_masculinos = (masculinos / total_mascotas) * 100
        porcentaje_femeninos = (femeninos / total_mascotas) * 100

        promedio_peso_mascotas = suma_peso_mascotas / total_mascotas

        print(f"El tipo más ingresado fue: {tipo_mas_ingresado}\nEl porcentaje de mascotas femeninas es de {porcentaje_femeninos}% y el de masculinos de {porcentaje_masculinos}%\nEl tipo de mascota mas pesada es {tipo_mascota_mas_pesada}\nEl nombre del gato mas joven es {nombre_gato_joven}\nEl promedio de peso de todas las mascotas es de {promedio_peso_mascotas}")
        

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()