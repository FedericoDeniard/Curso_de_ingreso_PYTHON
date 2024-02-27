import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Federico
Apellido: Deniard
En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha 
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden 
crear un programa para calcular y dividir los gastos de manera equitativa. 
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo, 
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 1).
Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 1).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”

bis 
cantidad de usuarios que pidieron mas de una bebida
cantidad de amigos que pidieron menos de dos plato principal

el nombre del que compro mas bebidas
el nombre del que menos platos principales pidio 

el nombre de la persona que pidio mas pizzas
el promedio de bebidas por persona
el precio promedio de bebidas pagada por cada persona
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Aventuras Extremas")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
            continuar = True

            total_personas = 0

            aguas = 0
            jugos = 0
            refrescos = 0
            bebida_mas_vendida = ""
            usuarios_multiple_bebidas = 0
            nombre_usuario_mas_bebidas = ""
            cantidad_usuario_mas_bebidas = 0

            hamburguesas = 0
            pizzas = 0
            ensaladas = 0
            usuarios_unico_plato = 0

            cantidad_menos_platos = 0
            nombre_usuario_menos_platos = ""

            precio_plato = 3000
            bebida_precio = 1000

            nombre_menos_hamburguesas = "Nadie pidio hamburguesa"
            cantidad_menos_hamburguesas = 0

            nombre_mas_pizzas = "Nadie pidio pizza"
            cantidad_mas_pizzas = 0


            while continuar == True:
                total_personas += 1

                nombre = ""
                nombre = prompt("","Ingrese su nombre")

                plato_elegido = prompt("","Ingrese el plato que desea (Pizza, Hamburguesa o Ensalada)")
                while plato_elegido != "Pizza" and plato_elegido != "Hamburguesa" and plato_elegido != "Ensalada":
                    plato_elegido = prompt("","Ingrese un plato válido (Pizza, Hamburguesa o Ensalada)")

                cantidad_platos = prompt("","¿Cuantos platos va a pedir?")
                cantidad_platos = int(cantidad_platos)
                while cantidad_platos < 1:
                    cantidad_platos = prompt("","Ingrese al menos 1 plato")
                    cantidad_platos = int(cantidad_platos)

                bebida_elegida = prompt("","Ingrese la bebida que desea (Refresco, Agua o Jugo)")
                while bebida_elegida != "Refresco" and bebida_elegida != "Agua" and bebida_elegida != "Jugo":
                    bebida_elegida = prompt("","Ingrese una bebida válida (Refresco, Agua o Jugo)")

                cantidad_bebidas = prompt("","¿Cuantas bebidas va a pedir?")
                cantidad_bebidas = int(cantidad_bebidas)
                while cantidad_bebidas < 1:
                    cantidad_bebidas = prompt("","Ingrese al menos 1 bebida")
                    cantidad_bebidas = int(cantidad_bebidas)

                match bebida_elegida:
                    case "Agua":
                        aguas += cantidad_bebidas
                    case "Jugo":
                        jugos += cantidad_bebidas
                    case _:
                        refrescos += cantidad_bebidas

                if cantidad_bebidas > 1:
                    usuarios_multiple_bebidas += 1

                if cantidad_platos < 2:
                    usuarios_unico_plato +=1

                if nombre_usuario_mas_bebidas == "":
                    nombre_usuario_mas_bebidas = nombre
                    cantidad_usuario_mas_bebidas = cantidad_bebidas
                elif cantidad_usuario_mas_bebidas < cantidad_bebidas:
                    nombre_usuario_mas_bebidas = nombre
                    cantidad_usuario_mas_bebidas = cantidad_bebidas

                if cantidad_menos_platos == 0:
                    cantidad_menos_platos = cantidad_platos
                    nombre_usuario_menos_platos = nombre
                elif cantidad_menos_platos  > cantidad_platos:
                    cantidad_menos_platos = cantidad_platos
                    nombre_usuario_menos_platos = nombre
                elif cantidad_menos_platos == cantidad_platos:
                    nombre_usuario_menos_platos +=  ", "+nombre

                match plato_elegido:
                    case "Ensalada":
                        ensaladas += cantidad_platos
                    case "Pizza":
                        pizzas += cantidad_platos
                        if nombre_mas_pizzas == "Nadie pidio pizza":
                            nombre_mas_pizzas = nombre
                            cantidad_mas_pizzas = cantidad_platos
                        elif cantidad_platos > cantidad_mas_pizzas:
                            nombre_mas_pizzas = nombre
                            cantidad_mas_pizzas = cantidad_platos
                        elif cantidad_platos == cantidad_mas_pizzas:
                            nombre_mas_pizzas += ", "+nombre
                    case _:
                        hamburguesas += cantidad_platos
                        if nombre_menos_hamburguesas == "Nadie pidio hamburguesa":
                            nombre_menos_hamburguesas = f"{nombre} fue quien pidio menos hamburguesas"
                            cantidad_menos_hamburguesas = cantidad_platos
                        elif cantidad_platos < cantidad_menos_hamburguesas:
                            nombre_menos_hamburguesas = nombre
                            cantidad_menos_hamburguesas = cantidad_platos

                continuar = question("","Desea continuar?")
            if nombre_mas_pizzas != "Nadie pidio pizza":
                nombre_mas_pizzas += f" pidio/pidieron mas pizza"
                
            if aguas > jugos and aguas > refrescos:
                bebida_mas_vendida = "agua"
            elif jugos > refrescos:
                bebida_mas_vendida = "jugos"
            else:
                bebida_mas_vendida = "refrescos"
            

            total_bebidas = refrescos + jugos + aguas
            promedio_bebidas = total_bebidas / total_personas

            promedio_precio_bebidas = (total_bebidas * bebida_precio) / total_personas

            total_platos = hamburguesas + pizzas + ensaladas
            porcentaje_pizzas = (pizzas / total_platos) * 100
            porcentaje_hamburguesas = (hamburguesas / total_platos) * 100
            porcentaje_ensaladas = (ensaladas / total_platos) * 100

            promedio_gastado_pizzas = (precio_plato * pizzas) / total_personas

            print(f"La bebida mas vendida fue {bebida_mas_vendida}\nLos porcentajes de los platos pedidos fueron: \n   Pizza: %{porcentaje_pizzas}\n   Hamburguesa: %{porcentaje_hamburguesas}\n   Ensalada: %{porcentaje_ensaladas}\nSe vendieron {refrescos} refrescos\nSe gasto {promedio_gastado_pizzas} promedio en pizzas.\n{nombre_menos_hamburguesas}\nBIS\n{usuarios_multiple_bebidas} personas pidieron mas de 1 bebida\n{usuarios_unico_plato} personas pidieron solo 1 plato principal\n{nombre_usuario_mas_bebidas} compro mas bebidas\n{nombre_usuario_menos_platos} pidio/pidieron menos platos\n{nombre_mas_pizzas}\nSe pidieron {promedio_bebidas} bebida promedio por persona\nEl precio promedio de bebidas por persona es de {promedio_precio_bebidas}")



'''bis 
cantidad de usuarios que pidieron mas de una bebida
cantidad de amigos que pidieron menos de dos plato principal

el nombre del que compro mas bebidas
el nombre del que menos platos principales pidio 

el nombre de la persona que pidio mas pizzas
el promedio de bebidas por persona
el precio promedio de bebidas pagada por cada persona'''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()