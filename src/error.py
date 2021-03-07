"""
clase Error()
"""
class Error:
    def __init__(self):
        self.idError=0
        self.descripcion=""
    def agregar(self,cod,descripcion):
        self.idError=int(cod)
        self.descripcion=descripcion
    def getError(self):
        return self.idError,self.descripcion
