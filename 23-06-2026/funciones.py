#Creamos la lista donde almacenaremos los vehiculos
vehiculos = []

#0.-Funcion para validar la patente
def buscar(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"] == patente:
            return i
    return -1
    
#1.-Agregar
def agregar(patente,tipo,anio,precio):
    #Validar que tenga 6 caracteres 
    if len(patente)!=6:
        print("Numero de caracteres no valido")
        return
    #Validar que no tenga espacios en blanco
    elif " " in patente:
        print("No puede tener espacios en blanco") 
        return
    #Validar que la patente no se repita
    elif buscar(patente)>=0:
        print("No se puede repetir la patente")
        return
    #Validar tipo
    elif tipo.lower() not in ("sedan","suv","camioneta"):
        print("Tipo no valido")
        return
    elif anio<2015 or anio>2026:
        print("Año no valido")
        return
    elif precio<=5000000:
        print("Precio no valido")
        return
    
    #Si los datos son validos creamos el diccionario con los datos
    auto = {"patente":patente,"tipo":tipo,"anio":anio,"precio":precio}
    vehiculos.append(auto)
    print("Vehiculo registrado")

def mostrar(patente):
    posicion = buscar(patente)
    if posicion >= 0:
        print(f"Patente encontrada : {vehiculos[posicion]}")
    else:
        print("Patente no encontrada")

#6.-Listar vehiculos con iva
def listarConIva():
    if len(vehiculos)>0:
        print(f"{N} {"patente":<8} {"tipo":<10} {"Año":<6} ${"Precio":<10}")
        for i in range(len(vehiculos)):
            print(f"{i+1} {vehiculos[i]["patente"]:<8} {vehiculos[i]["tipo"]:<10} {vehiculos[i]["anio"]:<6} ${vehiculos[i]["precio"]:<10}")
    else:
        print("No hay vehiculos registrados")