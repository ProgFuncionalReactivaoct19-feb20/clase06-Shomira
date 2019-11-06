
'''
Dado el siguiente archivo:

- Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10

- Ordenar la lista en función del día de nacimiento.
'''

# En map se envia funciones y se las itera....El filter se envia dos funciones y se las compara
import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter= "\t")

with open("data/trabajadores.csv") as midata:
	lineasDoc = list(lineasDiccionario(midata))

	# Filtra los nombres de los paises que son mas largos de 10
	
	print("  IMPRESION DE DATOS DEACUERDO AL PAIS CON NUMERO DE LETRAS MAYOR A DIEZ \n")
	# Filter primero 
	print(list(filter(lambda x: len(list(x.items())[2][1]) > 10, lineasDoc)))

	# print(list(map(lambda x: "%s-%s" %(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lineas)))

	# Ordenar en base  a el de dia de nacimiento
	print("   IMPRESION DE DATOS ORDENADOS DEACUERDO AL DIA DE NACIMIENTO\n")
	# Sorted del dia de nacimiento ... hacerle un split y acceder a la posicion 2
	# key ordena unicamente loq eu le envian 
	print(sorted( lineasDoc, key = lambda x: (list(x.items())[1][1].split("-")[2])))
	
	
	
 