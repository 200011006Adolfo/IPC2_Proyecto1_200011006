
from lstCircular import *
"""
Matriz
"""
class Matriz:
    def __init__(self):
        self.nombre=None
        self.n=0
        self.m=0
        self.datos=Lista()
        self.matrix=[]
        self.estado=False

    def crear(self,nombre,n,m,dato,estado):
        self.nombre=nombre
        self.n=n
        self.m=m
        self.datos=dato
        self.estado=estado

    def getMatriz(self):
        return self.nombre,self.n,self.m,self.datos,self.estado

    def datosMatriz(self,datos):
        self.datos=datos
        return self.datos

    def ordenarMatriz(self,x,y,v):
        self.x=x
        self.y=y
        self.v=v
        print(x,y,v)

        lstAct=self.datos

        for i in range(self.n):
            for j in range(self.m):
                if x==i and y==j:
                    lstAct.tamano
                    #if y>lstAct.tamano:
                    lstAct.agregar(v)
                    #else:
                    #     y<lstAct.tamano:
                else:
                    print("error")
