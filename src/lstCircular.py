from nodo import *

"""
Lista Circular
"""
class Lista:
    def __init__(self):
        self.inicio=Nodo(None)
        self.final=Nodo(None)
        self.tamano=0
    def esVacia(self):
        if self.inicio.getDato()==None:
            return True
    def agregar(self,nuevoDato):
        nuevoNodo=Nodo(nuevoDato)

        if(self.esVacia()==True):

            self.inicio=nuevoNodo
            self.inicio.siguiente=self.inicio
            self.final=nuevoNodo
        else:

            self.final.siguiente=nuevoNodo
            nuevoNodo.siguiente=self.inicio
            self.final=nuevoNodo
        self.tamano=self.tamano+1
    def modificar(self,nodoModificar,nuevoNodo):
        nodoModi=Nodo(nodoModificar)
        nuevo=Nodo(nuevoNodo)
        actual=self.inicio

        if(self.esVacia()==True):
            print('La lista esta vacia')
        else:
            i=0
            salir=False
            while i<(self.tamano-1) and salir==False :
                if(nodoModi.getDato()==actual.getDato()):
                    #print(nuevo.getDato())
                    actual.setDato(nuevo.getDato())
                    ##self.inicio=actual
                    print("Dato modificado")
                    salir=True
                    break
                else:
                    if(i==self.tamano-1):
                        print("Dato no Existe")
                i=i+1
                actual=actual.siguiente
    def eliminar(self,nodoEliminar):
        nodoEli=Nodo(nodoEliminar)
        anterior=Nodo(None)
        actual=self.inicio
        eliminado=False
        if(self.esVacia()==True):
            print('La lista esta vacia')
        else:
            i=0
            while i<self.tamano and eliminado==False:
                if(nodoEli.getDato()==actual.getDato()):
                    if(actual.getDato()==self.inicio.getDato()):
                        if(self.inicio==self.inicio.siguiente):
                            self.inicio.setDato(None)
                            print("Eliminando el unico Dato ")
                            eliminado=True
                            break

                        else:
                            self.inicio=self.inicio.siguiente
                            self.final.siguiente=self.inicio
                            print("Dato eliminado 1")
                            eliminado=True
                            break
                    else:
                        if(actual.getDato()==self.final.getDato()):
                            anterior.siguiente=self.inicio
                            self.final=anterior
                            print("Dato eliminado 2")
                            eliminado=True
                            break
                        else:
                            anterior.siguiente=actual.siguiente                          #print(anterior.siguiente.getDato())
                            #print("!!!")
                            print("Dato eliminado 3")
                            eliminado=True
                            break

                else:
                    if(i==self.tamano-1):
                        print("Dato no Existe")
                        break

                i=i+1
                anterior=actual;
                actual=actual.siguiente
    def desplegar(self):
        actual = self.inicio
        if self.inicio.getDato()!=None:
            while actual.getDato()!=None:
                print(actual.getDato())
                actual=actual.siguiente
                if(actual.getDato()==self.inicio.getDato()):
                    break
        else:
            print("Lista Vacia")
    def getDatos(self):
        actual = self.inicio
        cadena=""
        if self.inicio.getDato()!=None:
            i=0
            while actual.getDato()!=None:
                #print(actual.getDato())
                if i==0:
                    cadena=str(actual.getDato())
                    actual=actual.siguiente
                else:
                    cadena=cadena+","+str(actual.getDato())
                    actual=actual.siguiente
                if(actual.getDato()==self.inicio.getDato()):
                    break
                i=i+1
        else:
            print("Lista Vacia")
        #print(len(cadena))

        return cadena

    def getDato(self,indice):
        ind=indice-1
        actual = self.inicio
        #cadena=Lista()
        cadena=""
        if self.inicio.getDato()!=None:
            i=0
            while i<self.tamano:
                #print(actual.getDato())
                if i==ind:
                    #cadena.agregar(actual.getDato())
                    cadena=actual.getDato()
                    #print(cadena ,i ,ind)
                    return cadena
                    break
                i=i+1
                actual=actual.siguiente
        else:
            print("Lista Vacia")
            #print(len(cadena))

    def getDato11(self,lista):
        ind=indice-1
        actual = self.inicio
        #cadena=Lista()
        cadena=Lista()
        if self.inicio.getDato()!=None:
            i=0
            while i<self.tamano:
                #print(actual.getDato())
                if i==ind:
                    #cadena.agregar(actual.getDato())
                    cadena=actual
                    #print(cadena ,i ,ind)
                    return cadena
                    break
                i=i+1
                actual=actual.siguiente
        else:
            print("Lista Vacia")
