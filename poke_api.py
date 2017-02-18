#coding: utf-8

import requests
import json

numero_pokemon = raw_input('Número do pokemon: ')

res = requests.get('http://pokeapi.co/api/v2/pokemon/' + numero_pokemon + '/')

if requests.codes.ok != 200:
	print 'Não foi possível fazer a requisição'

else:
	out = json.loads(res.text)

	print 'Nome: ' + out['name']
	print 'Id: ' + str(out['id'])
	print 'Altura: ' + str(out['weight'])

	# Pegando todas as habilides do pokemon.
	for x in xrange(0, len(out['abilities'])):
		print 'Habilidades: ' + out['abilities'][x]['ability']['name']
	
	# Pegando o tipo.
	for x in xrange(0, len(out['types'])):
		print 'Tipo: ' + out['types'][x]['type']['name']