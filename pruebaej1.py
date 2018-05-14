import json
from pprint import pprint

with open('movies3.json') as data_file:
	data= json.load(data_file)

for titulo in data:
	print("-----------------")
	print("Titulo:",titulo["title"])
	print("Director:",titulo["director"])
	print("Categoria:",titulo["categoria"])
	print("-----------------")