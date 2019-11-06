
#Aplicfa una funcion a una estructuras
import csv
def lineas(archivo):
#csv.readerpara leer el archivo y por cada linea delimitar con ;
	return csv.reader(archivo, delimiter=";")
#with abre y los guarda con un alias y luego se encarga de cerrar los archivos 

with open("data/data-estudiantes.csv") as midata:
	# Imprime los email excluyendo si en dicha posicion se encuentra la palbra "email"
	print(list(map(lambda x:x[1], list(filter(lambda x :x[1] != "email", list(lineas(midata)))))))

