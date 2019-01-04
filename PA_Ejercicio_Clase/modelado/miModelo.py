
#  Creamo la clase equipo
class Equipo:
	
	# Constructor
	def __init__(self, nombre, ciudad, campeonatos, numJugadores):
		self.setNombre(nombre)
		self.setCiudad(ciudad)
		self.setCampeonatos(campeonatos)
		self.setNumJugadores(numJugadores)

	# Metodos set
	def setNombre(self, nombre):
		self.nombre = nombre.capitalize()

	def setCiudad(self, ciudad):
		self.ciudad = ciudad.capitalize()

	def setCampeonatos(self, campeonatos):
		self.campeonatos = int(campeonatos)

	def setNumJugadores(self, numJugadores):
		self.numJugadores = int(numJugadores.replace("\n", ""))

	# Metodos get
	def getNombre(self):
		return self.nombre

	def getCiudad(self):
		return self.ciudad

	def getCampeonatos(self):
		return self.campeonatos

	def getNumJugadores(self):
		return self.numJugadores

	# Metodo que presenta el objeto
	def __str__(self):
		cadena = ("%s - %s - %d - %d\n" % (self.getNombre(), self.getCiudad(), self.getCampeonatos(), self.getNumJugadores()))
		return cadena

	# Metodo que presenta el objeto
	def __repr__(self):
		cadena = ("%s - %s - %d - %d\n" % (self.getNombre(), self.getCiudad(), self.getCampeonatos(), self.getNumJugadores()))
		return cadena



class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenar(self, modo):
    	if (modo == 1):
    		return sorted(self.listado_equipos, key=lambda equipo: equipo.getNombre())
    	elif (modo == 2):
    		return sorted(self.listado_equipos, key=lambda equipo: equipo.getCampeonatos())
    	else:
    		return sorted(self.listado_equipos, key=lambda equipo: equipo.getNombre())