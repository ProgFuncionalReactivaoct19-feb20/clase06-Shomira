
'''
FUNCIONES PURAS:
Efectos Secundarios:

'''
# En map se envia funciones y se las itera....El filter se envia dos funciones y se las compara
import csv
def lineas(archivo):
# csv.readerpara leer el archivo y por cada linea delimitar con ;
	return csv.reader(archivo, delimiter=";")
# with abre y los guarda con un alias y luego se encarga de cerrar los archivos 

with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata)))



# midata = open ("data/data-estudiantes.csv")
# en usos grandes volumenes de datps es necesario cerrar el archivo*.
# print(list(lineas(midata)))
# midata.close()

