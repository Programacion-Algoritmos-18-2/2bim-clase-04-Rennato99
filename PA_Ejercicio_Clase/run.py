from modelado.miModelo import * # Importamos la clase Equipo y Operaciones
from manejoArchivos.miArchivo import * # Importamos la clase Archivo
from data import * # Importamos la carpeta data en la cual está la informacion 


# Creamos un objeto de tipo Archivo y le enviamos como argumento el nombre del archivo con la informacion
archivo01 = Archivo("data/informacion.csv", "r")

# Abrimos asi mismo el archivo 2 en el cual se va  a guardar la informacion
archivo02 = Archivo("data/informacionOrdenada.csv", "a")

# Obtenemso la informacion del archivo 1 en una lista
lista = archivo01.obtener_informacion()
lista = [l.split("|") for l in lista]	 # Dividimos cada linea en otra lista

# Instanciamos los objetos equipos y los agregamos a una nueva lista
listaEquipos = []
for linea in lista:
	equipo = Equipo(linea[0], linea[1], linea[2], linea[3])
	listaEquipos.append(equipo)

print("Informacion leida con exito!\n")

# Instanciamos el objeto para ordenar la lista
operar = Operaciones(listaEquipos)


'''
Ordenamiento
'''
modo = int(input("Ordenar de acuerdo al nombre = 1\nOrdenar de acuerdo a los campenatos = 2\nRespuesta -->"))


# Creamos otra lista Ordenada de acuerdo al nombre
listaEquiposOrdenada = operar.ordenar(modo)

print("\nLista ordenada con exito!:\n")
# Agregamos de la lista ordenada cada equipo al archivo 2 y tambien la imprimimos
for equipo in listaEquiposOrdenada:
	print(equipo)
	archivo02.agregar_informacion(equipo)

# Cerramos los archivos
archivo01.cerrar_archivo()
archivo02.cerrar_archivo()