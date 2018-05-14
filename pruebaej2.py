import json
from pprint import pprint
with open('movies3.json') as data_file:    
    data = json.load(data_file)

contador=0
listaanno=[]

for anno in data:
	if anno["fecha"] not in listaanno:
		listaanno.append(anno["fecha"])
listaanno.sort()

for anno in listaanno:
	for fecha in data:
		if anno==fecha["fecha"]:
			contador=contador+1
	print("En el año",anno,"se rodaron",contador,"peliculas")
	contador=0