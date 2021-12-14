class Deportista():

    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando


    #get and setter

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAñosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando

    #get and setter