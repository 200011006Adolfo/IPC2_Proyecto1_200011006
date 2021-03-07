from  xml.dom import minidom as md
import xml.etree.ElementTree as et
from lstCircular import *
from matriz import *
import os
import re

class Archivo:


    def __init__(self):
        self.nombre=""
        self.lista=Lista()


    def abrir(self,rutaArchivo):
        os.system("cls")
        try:
            print(rutaArchivo)
            arbol=et.parse(rutaArchivo)
            raiz=arbol.getroot()
            os.system('cls')
            l=Lista()
            lstErrores=Lista()
            matriz=Matriz()

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

                        print("numero de mat = " + str(nmat))

                        nombre=elemento.attrib.get('nombre')
                        n=elemento.attrib.get('n')
                        m=elemento.attrib.get('m')

                        if nombre==None :
                            errorInt=True
                            print("error 101")
                        if n==None or n.isdigit()==False:
                            errorInt=True
                            print("error 102")
                        if m==None  or m.isdigit()==False:
                            errorInt=True
                            print("error 103")

                        numDato=0

                        for subElement in elemento:
                            #print(subElement)
                            lstPosicion=None
                            lstPosicion=Lista()

                            x=subElement.attrib.get('x')
                            y=subElement.attrib.get('y')
                            v=subElement.text

                            if x==None or x.isdigit()==False :
                                errorInt=True
                                print("error 201")
                            if y==None or y.isdigit()==False:
                                errorInt=True
                                print("error 202")
                            if v==None or v.isdigit()==False:
                                errorInt=True
                                print("error 203")

                            lstPosicion.agregar(x)
                            lstPosicion.agregar(y)
                            lstPosicion.agregar(v)

                            lstDato.agregar(lstPosicion)

                            if(subElement.tag=="dato"):
                                error=False
                            else:
                                errorInt=True
                                indError=indError+1
                                #print("Error no se reconoce la etiqueta ")
                            numDato+=1
                        print(numDato)
                        if (n.isdigit() and m.isdigit()):
                            if numDato!=int(n)*int(m):
                                errorInt=True
                                print("error 300")

                        if errorInt and error==False:
                            print("Error en la matriz ", nombre, subElement.tag,errorInt)
                            matriz.crear(nombre,n,m,lstDato,errorInt)
                                #cambie listaAux.getDatos
                            errorInt=False
                        else:
                            #print(matriz.getDatosMatrix())
                            matriz.crear(nombre,n,m,lstDato,errorInt)
                        nmat=nmat+1
                    else:
                        indError=indError+1
                    #print("Error se esperaba la etiqueta matriz")
                    l.agregar(matriz.getMatriz())
            else:
                print("Error Se esperaba la etiqueta matrices")

            print("Se procesaron "+ str(nmat) +" matrices con exito")

            self.lista=l
            l.desplegar()
            print("En el archivo se detectaron  "+ str(indError) + " matrices con error")

        except FileNotFoundError as e:
            print("El archivo no existe")
        except Exception as e:
            print("Error en la estructura del archivo de entrada en \n")
            print(e)



#ar=Archivo()
#ar.abrir("entradaPrueba.xml")
#ar.procesar()


















#os.system("cls")
#arch=Archivo()
#arch.abrir2("entrada1.xml")
#arch.procesar1()
