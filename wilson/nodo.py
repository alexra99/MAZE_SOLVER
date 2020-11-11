class Nodo:

    def __init__(self, id, estado, valor, profundidad, costo, heuristica, accion, id_padre):
        self.id = id
        self.estado = estado
        self.valor = valor
        self.profundidad = profundidad
        self.costo = costo
        self.heuristica = heuristica
        self.accion = accion
        self.id_padre = id_padre

    def getID(self):
        return self.id

    def getValor(self):
        return self.valor

    def getProf(self):
        return self.profundidad

    def getCosto(self):
        return self.costo

    def getHeuristica(self):
        return self.heuristica

    def getAccion(self):
        return self.accion

    def getIDP(self):
        return self.id_padre

    def __str__(self):
        s = "["+str(self.id)+"]"+"["+str(self.costo)+","+str(self.estado)+","+str(self.id_padre)+","\
            +str(self.accion)+","+str(self.profundidad)+","+str(self.heuristica)+","+str(self.valor)+"]"
        return s
