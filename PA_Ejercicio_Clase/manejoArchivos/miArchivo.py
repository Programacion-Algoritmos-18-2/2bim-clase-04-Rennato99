import codecs
import sys

class Archivo:

	# Constructor
	def __init__(self, nombreArchivo, modo):
		self.archivo = codecs.open(nombreArchivo, modo)

	# Metodo que retorna una lista cuyos elementos son cada linea
	def obtener_informacion(self):
		return self.archivo.readlines()

	# Metodo para cerrar el archivo
	def cerrar_archivo(self):
		self.archivo.close()

	# Metodo para agregar informacion
	def agregar_informacion(self, equipo):
		self.archivo.write("%s-%s-%d-%d\n" % (equipo.getNombre(), equipo.getCiudad(),\
				equipo.getCampeonatos(), equipo.getNumJugadores()))

	# Metodo para cerrar el archivo
	def cerrar_archivo(self):
		self.archivo.close()

