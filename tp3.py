# -*- coding: utf-8 -*-
from grafo import *
import sys
'''import collections
from print_test import *'''

def cargar_archivo():
	#print ('Argument List:', str(sys.argv))
	try:
		#archivo = open((sys.argv),'r')
		archivo = open("marvel.pjk",'r')
		return archivo
	except IOError:
		raise IOError("no se reconocio")
		
def crear_grafo(archivo):
	primer_linea = archivo.readline()
	
	palabras = []
	palabras = primer_linea.split(" ")
	
	cant_vertices = int(palabras[1])
	
	grafo = Grafo()
	
	for pos in range(0, cant_vertices):
		#print(pos)
		linea = archivo.readline()
		palabras = linea.split(" ")
		nombre_personaje = palabras[1]
		nombre_personaje = nombre_personaje[1:-1] #saco comillas
		id = int(palabras[0])
		grafo[id] = nombre_personaje
		
	linea = archivo.readline()
	linea = archivo.readline()
	
	while(linea):
		#print(linea)
		palabras = linea.split(" ")
		vertice_origen = int(palabras[0])
		vertice_destino = int(palabras[1])
		peso = int(palabras[2])
		grafo.agregar_arista(vertice_origen, vertice_destino, peso)
		linea = archivo.readline()
	
	print("holaaaaaa")
	archivo.close()
	
def main():
	archivo = cargar_archivo()
	crear_grafo(archivo)
	
main()

