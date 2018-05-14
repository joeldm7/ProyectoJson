import json
from pprint import pprint

with open('movies3.json') as data_file:
	data= json.load(data_file)

listaPeliculas=[]



for p in data:
	listaPeliculas.append((int(p["oscar"]),p["title"]))

listaPeliculas.sort(reverse=True)

for peli in listaPeliculas:
        print("El número de oscars de la pelicula: ",peli[1],"es: ",peli[0])


