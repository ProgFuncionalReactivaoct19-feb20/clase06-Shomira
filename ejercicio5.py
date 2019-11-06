
import csv
'''

def lineas(archivo):
#csv.readerpara leer el archivo y por cada linea delimitar con ;
	return csv.reader(archivo, delimiter=";")
'''

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter= ";")

with open("data/data-estudiantes.csv") as midata:
	lineas = list(lineasDiccionario(midata))
	# imprime los nombres accediendo a las listas
	print(list(map(lambda x: list(x.items())[0][1], lineas)))




