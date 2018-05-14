import json
from pprint import pprint

with open('movies3.json') as data_file:
	data= json.load(data_file)

cadena=str(input("Introduce una cadena:"))

for pelicula in data:
	if pelicula['title'].startswith(cadena):
		print(pelicula['title'])