from  xml.dom import minidom as md
import xml.etree.ElementTree as et
from lstCircular import *
from matriz import *
from error import *
import os
import re

class Archivo:


    def __init__(self):
        self.nombre=""
        self.lista=Lista()
        self.listaDeErrores=Lista()


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

                            if x==None or x.isdigit()==False :
                                errorInt=True
                                #print("error 201")
                                er.agregar(201,"Error en atributo x en Dato matriz ")
                                lstErrores.agregar(er.getError())

                            if y==None or y.isdigit()==False:
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



#ar=Archivo()
#ar.abrir("entradaPrueba.xml")
#ar.procesar()


















#os.system("cls")
#arch=Archivo()
#arch.abrir2("entrada1.xml")
#arch.procesar1()
