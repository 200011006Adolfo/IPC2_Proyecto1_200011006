
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


    def crearDato(self,n,m):
        for i in range(n):
            self.matrix.append([0]*m)

    def agregarDato(self,x,y,v):
        self.matrix[int(x)-1][int(y)-1]=int(v)

    def getDatosMatrix(self):
        return self.matrix

    def crearMatrizFrecuencia(self,matriz,n,m):
        print("Creando Matriz de Frecuencia")
        matFrecuencia=Matriz()
        matFrecuencia.crearDato(int(n),int(m))

        lstDato=Lista()
        lstDato=matriz
        lstDatoX=Lista()
        lstPosicion=Lista()

        for i in range(1,lstDato.tamano+1):
            lstDatoX=lstDato.getDato(i)
            for j in range(1,lstDatoX.tamano+1):
                lstPosicion=lstDatoX.getDato(j)
                #print(" ",lstPosicion)
                if j==1:
                    x=lstPosicion
                else:
                    if j==2:
                        y=lstPosicion
                    else:
                        if j==3:
                            v=lstPosicion
                            matFrecuencia.agregarDato(x,y,v)
        print(matFrecuencia.getDatosMatrix())
        print("════════")
        return matFrecuencia.getDatosMatrix()

    def crearMatrizBinaria(self,matriz,n,m):
        lstDato=matriz
        matBinaria=Matriz()
        matBinaria.crearDato(int(n),int(m))

        for i in range(1,lstDato.tamano+1):
            lstDatoX=lstDato.getDato(i)
            for j in range(1,lstDatoX.tamano+1):
                lstPosicion=lstDatoX.getDato(j)
                #print(" ",lstPosicion)
                if j==1:
                    x=lstPosicion
                else:
                    if j==2:
                        y=lstPosicion
                    else:
                        if j==3:
                            v=lstPosicion
                            if int(v)>0:
                                matBinaria.agregarDato(x,y,1)
        print("Matriz De Patron Binaria")
        print(matBinaria.getDatosMatrix())
        print("════════")
        return matBinaria.getDatosMatrix()

    def crearMatrizReducida(self,matrizFre,matrizBin,n,m):
        matBin=matrizBin
        matFre=matrizFre
        matAux=matrizFre
        inc=0
        lstMatch=Lista()
        cMatch=0

        for fc in range(0,len(matBin)):
            for f in range(1+inc,len(matBin)):
                esIgual=False
                unoDiferente=False
                for c in range(0,int(m)):
                    #print(matBin [fc][c] , matBin[f][c])

                    if(matBin [fc][c]==matBin[f][c]):
                        esIgual=True

                    else:
                        unoDiferente=True
                        #print("diferente")

                if(esIgual and unoDiferente==False):
                    #print("coincidencia en ", fc , f)

                    for c in range(0,int(m)):
                        matAux[fc][c]=matFre[fc][c]+matFre[f][c]
                    matBin.pop(f)
                    matAux.pop(f)
                    #matFre.pop(f)
                    matFre=matAux
                    self.crearMatrizReducida(matFre,matBin,len(matBin),m)
                    break
                else:
                    if(esIgual==False and unoDiferente==False):
                        break
            inc+=1


        #print("Matriz Reducida")
        #print(matFre)
        #print("════════")
        return matFre
