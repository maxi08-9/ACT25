from os import system
from funciones import *
while True:
    try:
        system("pause")
        system("cls")
        print("""
        CONTROL DE INVENTARIO AUTOMOTRIZ
        1. Ingresar Nuevo Vehiculo
        2. Verificar Existencia de patente
        3. Actualizar Datos de un Vehiculo (Precio y Año)
        4. Aplicar Descuento Masivo por Año
        5. Exportar Inventario Filtrado por Tipo
        6. Listar Catalogo Completo con IVA incluido
        7. Finalizar Programa""")
        opcion = int(input("Seleccione :"))

        match(opcion):
            case 1:
                patente = input("Ingrese patente :").upper().strip()
                tipo = input("Ingrese tipo :")
                anio = int(input("Ingrese año (2015-2026) :"))
                precio = int(input("Ingrese precio $"))
                agregar(patente,tipo,anio,precio)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break
    except Exception as e:
        print(f"Error {e}")