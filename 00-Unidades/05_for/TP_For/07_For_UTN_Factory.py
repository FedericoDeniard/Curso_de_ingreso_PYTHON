import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Federico
apellido:   Deniard
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr. Hecho?
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género. Hecho
d. Tecnologia con mas postulantes (solo hay una). Hecho
e. Porcentaje de postulantes de cada genero. Hecho

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        jr_mas_joven = 0
        nombre_jr_mas_joven = ""

        edad_mujeres = 0
        cantidad_mujeres = 0

        edad_hombres = 0
        cantidad_hombres = 0

        edad_nb = 0
        cantidad_nb = 0

        cantidad_postulantes = 0

        postulantes_python = 0
        postulantes_js = 0
        postulantes_asp__net = 0

        nb_ssr_js_asp__net = 0
        tecnologia_mas_postulantes = ""

        for i in range(0,10):

            nombre = prompt(f"Candidiato {i}",f"Ingrese el nombre del cadidato {i}:")
            edad = prompt(f"Candidiato {i}",f"Ingrese la edad del cadidato {i}:")
            edad = int(edad)
            while edad < 18:
                edad = prompt(f"Candidiato {i}","Ingrese una edad válida:")
                edad = int(edad)
            genero = prompt(f"Candidiato {i}",f"Ingrese el género del cadidato {i}: (F-M-NB)")
            tecnologia = prompt(f"Candidiato {i}",f"Ingrese la tecnología principal del cadidato {i}: (PYTHON - JS - ASP.NET)")
            puesto = prompt(f"Candidiato {i}",f"Ingrese el puesto del cadidato {i}: (Jr - Ssr - Sr)")
            
            if genero == "F":
                cantidad_mujeres += 1
                edad_mujeres += edad
            elif genero == "H":
                cantidad_hombres += 1
                edad_hombres += edad
            else: #No binario
                cantidad_nb += 1
                edad_nb += edad
                if edad > 24 and edad < 41 and tecnologia != "JS" and puesto == "Ssr":
                     nb_ssr_js_asp__net += 1

            if i == 0:
                jr_mas_joven = edad
                nombre_jr_mas_joven = nombre
            elif edad < jr_mas_joven:
                jr_mas_joven = edad
                nombre_jr_mas_joven = nombre

            match tecnologia:
                case "JS":
                    postulantes_js += 1
                case "PYTHON":
                    postulantes_python += 1
                case _:
                    postulantes_asp__net += 1

            cantidad_postulantes += 1
        
        if postulantes_python > postulantes_js and postulantes_python > postulantes_asp__net:
            tecnologia_mas_postulantes = "Python"
        elif postulantes_js > postulantes_asp__net:
            tecnologia_mas_postulantes = "JavaScript"
        else:
            tecnologia_mas_postulantes = "ASP.NET"

        promedio_edad_mujeres = edad_mujeres / cantidad_mujeres
        promedio_edad_hombres = edad_hombres / cantidad_hombres
        promedio_edad_nb = edad_nb / cantidad_nb

        porcentaje_mujeres = (cantidad_mujeres / cantidad_postulantes) * 100
        porcentaje_hombres = (cantidad_hombres / cantidad_postulantes) * 100
        porcentaje_nb = (cantidad_nb / cantidad_postulantes) * 100
        
        print(f"Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS {nb_ssr_js_asp__net} \nNombre del Jr con menor edad: {nombre_jr_mas_joven}\nPromedio edad hombres: {promedio_edad_hombres}\nPromedio edad mujeres: {promedio_edad_mujeres}\nPromedio edad nb: {promedio_edad_nb}\nTeconología con más postulantes:{tecnologia_mas_postulantes}\nPorcentaje hombres: {porcentaje_hombres}\nPorcentaje mujeres: {porcentaje_mujeres}\nPorcentaje nb: {porcentaje_nb}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
