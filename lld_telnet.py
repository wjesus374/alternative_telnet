#!/usr/bin/python 

import telnetlib
import re
import json
import argparse

hosts = [
    {'host': '192.168.106.151', 'port': 6666, 'send': 'PING\n', 'reply': '(PONG)'},
    {'host': '192.168.106.153', 'port': 6666, 'send': 'PING\n', 'reply': '(PONG)'},
    {'host': '192.168.106.168', 'port': 6666, 'send': 'PING\n', 'reply': '(PONG)'}
]

def sendtest(hostlist):

    #Dict para retorno de dados
    result = {}
    result['data'] = []

    for info in hostlist:
        try:
            tn = telnetlib.Telnet(info['host'],int(info['port']))
            tn.write(info['send'])
            reply = tn.read_all()

            if re.search(info['reply'],reply):
                #print('OK')
                result['data'].append({'host': info['host'], 'status' : 'OK'})
            else:
                #print('No data')
                result['data'].append({'host': info['host'], 'status' : 'KO'})
        except Exception as e:
            #print(e)
            result['data'].append({'host': info['host'], 'status' : str(e)})

    return result

def discovery_def():
    result = sendtest(hosts)
    print(json.dumps(result))

def read_def():
    print('Read')

#Mapa de valores:
fmap = { 'discovery': discovery_def, 'read': read_def }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Host Monitor')
    parser.add_argument('commands', choices=fmap.keys())
    #, help='Gerar JSON LLD para Zabbix')
    #parser.add_argument('read', choices=fmap.keys(), help='Ler os dados gravados e retornar status do host')
    args = parser.parse_args()
    func = fmap[args.commands]
    func()

