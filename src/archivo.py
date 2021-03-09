from  xml.dom import minidom as md
import xml.etree.ElementTree as et
from lstCircular import *
from matriz import *
from error import *
from graphviz import Digraph as g
import os
import re

class Archivo:


    def __init__(self):
        self.nombre=""
        self.lista=Lista()
        self.listaDeErrores=Lista()
        self.listaMatrices=Lista()
        self.listaFrecuencia=Lista()


    def abrir(self,rutaArchivo):
        os.system("cls")
        try:
            print(rutaArchivo)
            arbol=et.parse(rutaArchivo)
            raiz=arbol.getroot()
            os.system('cls')
            l=Lista()
            lstErrores=Lista()
            errores=Lista()
            matriz=Matriz()
            er=Error()
            indError=0
            error=False
            errorMat=False
            errorInt=False


            if(raiz.tag=="matrices"):
                nmat=0
                for elemento in raiz:
                    #print(elemento.tag)
                    lstDato=Lista()

                    #listaAux.agregar(elemento.tag)
                    if(elemento.tag=='matriz'):

                        #print("numero de mat = " + str(nmat))

                        nombre=elemento.attrib.get('nombre')
                        n=elemento.attrib.get('n')
                        m=elemento.attrib.get('m')



                        if nombre==None :
                            errorInt=True
                            #print("error 101")
                            er.agregar(101,"Error en atributo Nombre")
                            lstErrores.agregar(er.getError())


                        if n==None or n.isdigit()==False:
                            errorInt=True
                            #print("error 102")
                            er.agregar(102,"Error en atributo n" )
                            lstErrores.agregar(er.getError())


                        if m==None  or m.isdigit()==False:
                            errorInt=True
                            #print("error 103")
                            er.agregar(103,"Error en atributo m ")
                            lstErrores.agregar(er.getError())


                        numDato=0

                        for subElement in elemento:
                            #print(subElement)
                            lstPosicion=None
                            lstPosicion=Lista()

                            x=subElement.attrib.get('x')
                            y=subElement.attrib.get('y')
                            v=subElement.text

                            if x==None or x.isdigit()==False or x > n:
                                errorInt=True
                                #print("error 201")
                                er.agregar(201,"Error en atributo x en Dato matriz ")
                                lstErrores.agregar(er.getError())

                            if y==None or y.isdigit()==False or y > m:
                                errorInt=True
                                #print("error 202")
                                er.agregar(202,"Error en atributo y en Dato matriz ")
                                lstErrores.agregar(er.getError())
                            if v==None or v.isdigit()==False:
                                errorInt=True
                                #print("error 203")
                                er.agregar(203,"Error en valor en Dato matriz ")
                                lstErrores.agregar(er.getError())

                            lstPosicion.agregar(x)
                            lstPosicion.agregar(y)
                            lstPosicion.agregar(v)

                            lstDato.agregar(lstPosicion)

                            if(subElement.tag=="dato"):
                                error=False
                            else:
                                errorInt=True
                                #print("error 200")
                                er.agregar(200,"Error en etiqueta dato")
                                lstErrores.agregar(er.getError())

                                indError=indError+1
                                #print("Error no se reconoce la etiqueta ")
                            numDato+=1
                        #print(numDato)
                        if (n.isdigit() and m.isdigit()):
                            if numDato!=int(n)*int(m):
                                errorInt=True
                                #print("error 300")
                                er.agregar(300,"Error tamaño de la matriz")
                                lstErrores.agregar(er.getError())


                        if errorInt and error==False:
                            #print("Error en la matriz ", nombre, subElement.tag,errorInt)

                            matriz.crear(nombre,n,m,lstDato,errorInt)
                                #cambie listaAux.getDatos
                            errores.agregar(nombre)
                            errores.agregar(lstErrores.getDatos())

                            indError=indError+1
                            errorInt=False
                        else:
                            #print(matriz.getDatosMatrix())
                            matriz.crear(nombre,n,m,lstDato,errorInt)
                        nmat=nmat+1
                    else:
                        #indError=indError+1
                        #print("Error se esperaba la etiqueta matriz")

                        errores.agregar(elemento.attrib.get('nombre') + " Error : 001 No se reconoce etiqueta" )
                        #errores.agregar(nombre + "Error :" +lstErrores.getErrores() )
                    l.agregar(matriz.getMatriz())
            else:
                print("Error Se esperaba la etiqueta matrices")

            #print("Se cargaron "+ str(nmat) +" matrices ")

            self.lista=l
            self.listaDeErrores=errores
            #l.desplegar()
            print("══════════════════════════════════════════════════════════")
            print("Se ha cargado el archivo a la memoria satisfactoriamente...")
            print("Se detectaron ", l.tamano," matrices ")
            print("En el archivo se detectaron  "+ str(indError) + " matrices con error")
            #self.listaDeErrores.desplegar()
            #l.desplegar()

        except FileNotFoundError as e:
            print("El archivo no existe")

        except Exception as e:
            print("Error en la estructura del archivo de entrada en \n")
            print(e)


    def procesar(self):
        os.system("cls")
        print("Procesando Archivo")

        if self.lista.tamano==0:
            print("Primero debe cargar archivo ")
        else:
            matAux=Matriz()
            listaAux=Lista()
            matAux=Matriz()
            lstDato=Lista()

            print("======")

            for nMat in range(1,self.lista.tamano+1):
                print(nMat)
                matAux=self.lista.getDato(nMat)
                i=0
                for datMatriz in matAux:
                    if i==0:
                        nombre =datMatriz
                        print(nombre)
                    if i==1:
                        n =datMatriz
                        #print(n)
                    if i==2:
                        m =datMatriz
                        #print(m)
                    if i==3:
                        lstDatoX=Lista()
                        lstDatoY=Lista()
                        lstPosicion=Lista()
                        lstDato = datMatriz
                        #print(lstDato)

                    if i==4:
                        estado=datMatriz
                        #print(estado)
                    i+=1
                """Crear la matriz """

                if estado==False:
                    print(nombre)
                    matFrecuencia=Matriz()
                    matrizAux=Matriz()
                    print("Creando Matriz de Frecuencia")
                    mF=matFrecuencia.crearMatrizFrecuencia(lstDato,int(n),int(m))
                    print(mF)
                    print("════════════════════")
                    matrizAux.crear(nombre,n,m,lstDato,True)
                    self.listaFrecuencia.agregar(matrizAux.getMatriz())

                    #   print("Creando Matriz Binaria")

                    matBinaria=Matriz()
                    matBinaria.crearDato(int(n),int(m))
                    mB=matBinaria.crearMatrizBinaria(lstDato,int(n),int(m))
                    #   print("Creando Matriz Reducida")
                    matRed=Matriz()
                    mBin=mB
                    #matBinaria.getDatosMatrix()
                    mFre=mF
                    #matFrecuencia.getDatosMatrix()
                    mR=matRed.crearMatrizReducida(mFre,mBin,n,m)

                    #listaMatrices.agregar("mR")
                    mtRed=Matriz()
                    mtRed.crear(nombre,n,m,mR,True)
                    self.listaMatrices.agregar(mtRed.getMatriz())
                    print("matriz Reducida")
                    print(mR)
                    print("════════")

                else:
                    print("")

    def crearSalida(self,rutaArchivo):
        print("Crear Archivo de Salida")

    def graficar(self):
        matAux=Matriz()

        if self.lista.tamano==0:
            print("Primero debe cargar archivo ")
        else:
            matAux=Matriz()
            listaAux=Lista()
            matAux=Matriz()
            lstDato=Lista()

            print("======")

            print("Lista da Matrices Procesadas")
            print("══════════════════════════════")
            print("       No    Nombre")
            for nMat in range(1,self.listaFrecuencia.tamano+1):
                #print(nMat)
                matAux=self.listaFrecuencia.getDato(nMat)
                i=0
                for datMatriz in matAux:
                    if i==0:
                        nombre =datMatriz
                        print("       "+str(nMat) +" " +nombre)
                    i+=1

            op=input(" \n Elija la matriz que desea graficar:  ")

            for nMat in range(1,self.listaFrecuencia.tamano+1):
                #print(nMat)
                if int(op)==nMat:
                    matAux=self.listaFrecuencia.getDato(nMat)
                    i=0
                    for datMatriz in matAux:
                        if i==0:
                            nombre =datMatriz
                            print("\n")
                            print("   Usted eligio la matriz: ",nombre)
                        if i==1:
                            n =datMatriz
                        if i==2:
                            m =datMatriz
                        if i==3:
                            matriz =datMatriz
                        if i==4:
                            estado =datMatriz

                        i+=1

                    print("     Graficando...")


                    dot=g(comment="Matrices")
                    dot.node('A','Matrices')

                    #Datos de la matriz
                    dot.node('nombre',nombre)
                    dot.node('n','n = '+str(n))
                    dot.node('m','m = '+str(m))

                    dot.edge('A','nombre')
                    dot.edge('nombre','n')
                    dot.edge('nombre','m')

                    matFrecuencia=Matriz()
                    matrizF=matFrecuencia.crearMatrizFrecuencia(matriz,int(n),int(m))
                    print("    ",matrizF)

                    for i in range(0,int(n)):
                        for j in range(0,int(m)):
                            dot.node(str(i)+" " + str(j) ,str(matrizF[i][j]))

                    for i in range(0,1):
                        for j in range(0,int(m)):
                            dot.edge('nombre',str(i)+" "+str(j))

                    for i in range(0,int(n)-1):
                        for j in range(0,int(m)):
                            if j<int(m):
                                dot.edge(str(i)+" " + str(j),str(i+1)+" " + str(j))

                    #print(dot.source)
                    dot.render("Reportes/"+nombre,format="png",view=True)
