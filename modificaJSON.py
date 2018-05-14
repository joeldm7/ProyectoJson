import json
import random


from pprint import pprint

with open('movies2.json') as data_file:    
    data = json.load(data_file)
for pelicula in data:
	#if pelicula['title'].startswith('T'):
	#añadir valores aqui tal cual para ir añadiendo campos al fichero Json
		num_al=random.randrange(10)
		fecha_al=random.randrange(1990,2010)
		pelicula['oscar']=num_al
		pelicula['categoria']='accion'
		pelicula['director']='Peter Jackson'
		pelicula['fecha']=fecha_al
file = open("movies3.json",'w')
json.dump(data,file,indent=4)
#pprint(data[2]["title"])
#pprint(data[2]["oscar"])
