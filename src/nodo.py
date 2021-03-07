# -*- coding: utf-8 -*-
"""
Lista no ordenada
"""
class Nodo:

    def __init__(self,datos):
        self.dato =datos
        self.siguiente =None

    def getDato(self):
        return self.dato
    def setDato(self,datos):
        self.dato=datos
