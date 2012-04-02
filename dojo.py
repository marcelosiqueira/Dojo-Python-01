#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Programa

class Dojo:
    cedulas=[100,50,20,10]
    def __init__(self):
        pass

    def saque(self, valor):
	resultado = {}
	if valor==0:
	    return {}
	    
	if valor % 10 != 0:
	    return dict()
	
	for cedula in self.cedulas:
	    if valor >= cedula:
		
		resto = valor % cedula
		quociente = valor / cedula
		
		resultado[cedula] = quociente
		
		if resto == 0 :
		    return resultado

		valor = resto
	
	
	    