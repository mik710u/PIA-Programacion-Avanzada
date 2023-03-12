import csv
import datetime
import os
from pia_clases import Mascota

nombre_archivo = "mascotas_consulta.csv"

formato = "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}"

def enter():
    input("-- Presione ENTER para continuar --")

def obtenerNuevaClave():

    if os.path.isfile(nombre_archivo):
        # Abrir el archivo CSV
        with open(nombre_archivo, 'r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)

            # Crear una lista con todas las claves de la columna "clave"
            claves = []

            for fila in lector_csv:
                claves.append(int(fila['clave']))

            # Obtener la última clave de la lista y sumarle uno
            nueva_clave = max(claves) + 1
    else:
        nueva_clave = 1

    return nueva_clave


def agregar():
    lista_mascotas = []
    mascotas_agregadas = 0
    v_clave = obtenerNuevaClave()

    while True:
        if mascotas_agregadas != 0:
            v_clave = v_clave + 1

        v_nombre = input("Ingrese el nombre: ")
        v_especie = input("Ingrese la especie: ")
        v_raza = input("Ingrese la raza: ")
        v_peso = input("Ingrese el peso en kg: ")

        momento = datetime.datetime.now()
        v_fecha_consul = momento.strftime("%d-%m-%Y %H:%M:%S")

        v_mascota = Mascota(v_clave, v_nombre, v_especie, v_raza, v_peso, v_fecha_consul)

        lista_mascotas.append(v_mascota)

        while True:
            finalizar = input("¿Finalizar registro? [SI/NO]: ")
            if finalizar.upper() == "SI" or finalizar.upper() == "NO":
                break
            else:
                print("Opcion invalida")
                enter()

        if finalizar.upper() == "SI":
            break

        mascotas_agregadas = mascotas_agregadas + 1

    # Guardar datos en CSV

    # Si el archivo CSV existe:
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, "a+", newline="") as archivo:
            writer = csv.writer(archivo)
            for registro in lista_mascotas:
                writer.writerow([registro.clave, registro.nombre, registro.especie, registro.raza, registro.peso, registro.fecha_consul])
        print("\nSe han anadido los datos correctamente \n")

    # Si no existe:
    else:
        with open(nombre_archivo, "w", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)

            # Escribir las columnas en el archivo CSV
            columnas = ["clave", "nombre", "especie", "raza", "peso en kg", "fecha consulta"]
            writer.writerow(columnas)

            # Escribir cada instancia de objeto de la clase Persona en el archivo CSV
            for registro in lista_mascotas:
                writer.writerow([registro.clave, registro.nombre, registro.especie, registro.raza, registro.peso, registro.fecha_consul])
        print("\nSe ha creado el archivo csv con los datos \n")


def consultarUnRegistro():
    clave_consulta = input("Ingrese la Clave que desea consultar sus datos: ")

    # Si el archivo CSV existe:
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)

            # Buscar el registro con la clave especificada
            for fila in lector_csv:
                if fila['clave'] == clave_consulta:
                    print(formato.format("clave", "nombre", "especie", "raza", "peso en kg", "fecha consulta"))
                    print(formato.format(fila['clave'], fila['nombre'], fila['especie'], fila['raza'], fila['peso en kg'], fila['fecha consulta']))
                    break
            else:
                print("No hay datos asociados a esa clave")
    else:
        print("No se ha creado aun el archivo csv")


def verTodosLosRegistros():
    if os.path.isfile(nombre_archivo):
        datos = []
        with open(nombre_archivo, 'r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)

            print(formato.format("clave", "nombre", "especie", "raza", "peso en kg", "fecha consulta"))
            for fila in lector_csv:
                print(formato.format(fila['clave'], fila['nombre'], fila['especie'], fila['raza'], fila['peso en kg'], fila['fecha consulta']))
    else:
        print("No se ha creado aun el archivo csv")




def menu():
    while True:
        print("-- MENU VETERINARIA --")
        print("[1] Agregar mascota atendida")
        print("[2] Consultar mascota atendida")
        print("[3] Ver todas las mascotas atendidas")
        print("[0] Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar()

        elif opcion == "2":
            consultarUnRegistro()

        elif opcion == "3":
            verTodosLosRegistros()

        elif opcion == "0":
            print("-- Fin del programa --")
            break
        else:
            print("Opcion invalida. Intente de nuevo")


# Iniciar programa
menu()