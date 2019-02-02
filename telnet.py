#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import re
import getopt

try:
	opts, args = getopt.getopt(sys.argv[1:], 'x')

except getopt.GetoptError:
	print('ERRO AO PROCESSAR INFORMAÇÕES INFORMADAS')

#Organizando os argumentos
try:
	host = args[0]
	port = args[1]
	bindip = args[2]
except:
	bindip = 'None'

#Exemplo de IP não permitido abrir socket.
#Para mais de um IP, utilizar expressão regular

if re.search('8.8.8.8',host):
	print('OPERAÇÃO NÃO PERMITIDA - IP DO GOOGLE')
	sys.exit(1)
else:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(5)

	if bindip != 'None':
		try:
			sock.bind((bindip,0))
		except:
			print('NÃO FOI POSSÍVEL UTLIZAR ORIGEM')
			sys.exit(1)

	try:
		sock.connect((host,int(port)))
		print "CONECTIVIDADE OK"
		sys.exit(0)
	except socket.timeout:
		print "TIMEOUT: FALHA AO CONECTAR"
		sys.exit(1)
