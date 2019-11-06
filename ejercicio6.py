import csv
'''

def lineas(archivo):
#csv.readerpara leer el archivo y por cada linea delimitar con ;
	return csv.reader(archivo, delimiter=";")
	Anderdon - juamsimon@hotmail
	mitchell - boylejennifer@gmail
'''

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter= ";")

with open("data/data-estudiantes.csv") as midata:
	lineas = list(lineasDiccionario(midata))
	
	# Cadeba Final que itera las lineas deacuerdo a las posiciones y les realiza un SPLIT al nombre y al email
	# Finalmente con el split excluye a los segundos nombres y el .com del email
	print(list(map(lambda x: "%s-%s" %(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lineas)))





