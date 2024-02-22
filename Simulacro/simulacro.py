import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


""" 
Simulacro 01 - Dr. UTN

Nombre:     Federico
Apellido:   Deniard

Enunciado:


DNI terminados en 0 o 1

1) Informar la cantidad de personas de sexo femenino
2) La edad promedio de personas de sexo masculino
3) El nombre de la persona la persona de sexo nb con más temperatura(si la hay)

DNI terminados en 4 o 5
1) Informar la cantidad de personas de sexo nb
2) La edad promedio de personas de sexo femenino
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7
1) Informar la cantidad de personas mayores de edad (desde los 18 años)
2) La edad promedio en total de todas las personas mayores de edad (18 años)
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9
1) Informar la cantidad de personas menores de edad (menos de 18 años)
2) La temperatura promedio en total de todas las personas menores de edad
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)

Pedir datos por Prompt y mostrar por Print

Punto A - por el número de DNI del alumno:

DNI terminados en 2 o 3
1) Informar la cantidad de personas de sexo masculino
2) La edad promedio de personas de sexo nb
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

Todos los alumnos:
B - Informar cual fue el sexo mas ingresado
C - El porcentaje de personas con fiebre y el porcentaje sin fiebre
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        pacientes = 5
        #Masculinos
        masculinos = 0

        #Femeninos
        femenino_nombre_temperatura_baja = ""
        femenino_temperatura_baja = 0
        femeninos = 0

        #NoBinarios
        suma_edad_nb = 0
        no_binarios = 0

        sexo_mas_ingresado = ""

        #Fiebre es más de 37.5°C
        personas_con_fiebre = 0

        for i in range(0,pacientes):
            nombre = prompt("",f"Ingrese el nombre del paciente {i+1}:")
            while nombre.isdigit():
                nombre = prompt("",f"Nombre inválido, ingrese nuevamente")

            temperatura = prompt("",f"Ingrese la temperatura del paciente {i+1}:")
            temperatura = int(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura =  prompt("Error", "La temperatura debe ser entre 35 y 42 grados.\nIngrese nuevamente la temperatura:")
                temperatura = int(temperatura)
            
            sexo = prompt("",f"Ingrese el género del paciente {i+1}")
            while sexo != "f" and sexo != "m" and sexo != "nb":
                sexo = prompt("","Ingrese un género válido (f, n o nb):")
            
            edad = prompt("",f"Ingrese la edad del paciente {i+1}:")
            edad = int(edad)
            while edad < 1:
                edad = prompt("","Edad inválida, reingrese la edad:")
                edad = int(edad)

            match sexo:
                case "m":
                    masculinos += 1
                case "f":
                    femeninos += 1
                    if temperatura == 0:
                        femenino_temperatura_baja = temperatura
                        femenino_nombre_temperatura_baja = nombre
                    elif temperatura < femenino_temperatura_baja:
                        femenino_temperatura_baja = temperatura
                        femenino_nombre_temperatura_baja = nombre
                case "nb":
                    suma_edad_nb += edad
                    no_binarios += 1
            
            if masculinos > femeninos and masculinos > no_binarios:
                sexo_mas_ingresado = "masculino"
            elif femeninos > no_binarios:
                sexo_mas_ingresado = "femenino"
            else:
                sexo_mas_ingresado = "no binario"

            if temperatura > 37:
                personas_con_fiebre += 1

        if no_binarios == 0:
            promedio_edad_nb = "No se ingresaron personas de este género"
        else:
            promedio_edad_nb = suma_edad_nb / no_binarios
        porcentaje_fiebre = (personas_con_fiebre / pacientes) * 100
        porcentaje_sanas =  ((pacientes - personas_con_fiebre) / pacientes ) * 100

        print("",f"Cantidad de masculinos: {masculinos}\nEdad promedio de nb: {promedio_edad_nb}\nFemeino con la temperatura más baja: {femenino_nombre_temperatura_baja}\nEl género más ingresado fue: {sexo_mas_ingresado}\nEl porcentaje de personas con fiebre es de {porcentaje_fiebre}%\n y el de personas sanas es de {porcentaje_sanas}%")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()