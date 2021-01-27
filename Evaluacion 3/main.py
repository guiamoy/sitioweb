#https://github.com/germ4nmc/PROYECTOX.git

import time
import string
import random


class Inventario:
    def __init__(self):
        especie_flores = ["a", "b", "c", "d"]
        tamano_flores = ["L", "S"]
        for i in range(0,100):
            with open("bodega_flores.txt", "a") as archivo_salida:
                variable = random.choice(especie_flores)
                variable2 = random.choice(tamano_flores)
                variable3 = (variable + variable2)
                archivo_salida.write(variable3 + "\n")
                print(variable3)
                time.sleep(0.002)

    def pop(self):
        pass

    def contenido(self):
        pass

    def vaciar(self):
        pass

    def guardar(self):
        pass

class InventarioTipoRamos(Inventario):

    def __init__(self, nombre, nombre_archivos):
        super().__init__(nombre, nombre_archivos)

    def tipos_de_flores_en_uso(self):
        pass

class InventarioFlores(Inventario):
    pass
    def declarar_ramo(self, ramo):
        
        if len(ramo) < 8:
            print("formato no valido")
        else:
            pass
            with open("bodega_ramos.txt", "w") as archivo_salida1:
                archivo_salida1.write(ramo)

    def extrae_flor(self, nombre, tamano):
        pass

    def inventario(self):
        pass

class Flor:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class TipoRamo:
    def __init__(self, nombre, tamano, sec_base, largo_sec_extra):
        self.nombre = nombre
        self.tamano = tamano
        self.sec_base = sec_base
        self.largo_sec_extra = largo_sec_extra
    
    def genera_sec_extra(self):
        pass

class Ramo(TipoRamo):
    def __init__(self):
        self.sec_extra = __genera_sec_extra(self)
        self.ramo_
        self.fecha_hora = __genera_fecha_hora(self)

    def despachar(self):
        pass

    def __genera_sec_extra(self):
        pass

    def __genera_fecha_hora(self):
        pass

class FabricadorRamos:
    def __init__(self):
        pass

    def generar_ramo(self):
        pass

    def despachar_ramo(self):
        pass



ramo =InventarioFlores()
bodega = Inventario()
pedido = input("Ingrese el ramo que fabricaremos:")
ramo.declarar_ramo(pedido)


bodega_flores_disponibles = InventarioFlores()
tipos_de_ramos_en_fabricacion = InventarioTipoRamos()
bodega_ramos_ya_fabricados = InventarioRamos()
jefe_de_compras_de_flores = AbastecedorFlores(bodega_flores_disponibles, tipos_de_ramos_en_fabricacion)
jefe_de_produccion = FabricadorRamos(bodega_flores_disponibles, tipos_de_ramos_en_fabricacion, bodega_ramos_ya_fabricados)

while True:
    flor_a_agregar = jefe_de_compras_de_flores.generar_flor(tipos_de_ramos_en_fabricacion)
    jefe_de_compras_de_flores.abastecer_flor(flor_a_agregar) #bodega recibio flor nueva

    if jefe_de_produccion.puede_generar_ramo() == True:
        ramo = jefe_de_produccion.generar_ramo()
        jefe_de_produccion.despachar_ramo()