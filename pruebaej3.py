import json
from pprint import pprint

with open('movies3.json') as data_file:
	data= json.load(data_file)

pregunta=int(input("Introduce una fecha: "))

for pelicula in data:
	if pelicula['fecha'] == pregunta:
		print(pelicula['title'])