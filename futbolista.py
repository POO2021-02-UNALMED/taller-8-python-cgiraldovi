from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)


    #get and setter

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getGolesMarcados(self):
        return self._golesMarcados

    def getPiernaHabil(self):
        return self._piernaHabil

    def getListaFutbolistas(cls):
        return cls.listaFutbolistas


    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil


    def setListaFutbolistas(cls,listaFutbolistas):
        cls.listaFutbolistas = listaFutbolistas

    def __str__(self):
        return "Mi nombre es " + super().getNombre() + " soy profesional en el deporte " + super().getDeporte() +" Tengo " + str(super().getEdad()) +" años de edad y llevo " + str(super().getAñosPracticando()) +" años en el deporte"

    #get and setter