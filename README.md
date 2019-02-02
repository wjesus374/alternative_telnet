# Alternative telnet

Uma alternativa simples para abertura de socket (telnet ou nc) feito em Python

Script só testa conectividade com o host de destino, uma solução bem simples ao telnet ou nc. Ideal para adicionar ao Zabbix e monitorar conectividade com host e porta.

Exemplo de uso:

python telnet.py google.com.br 443

Você pode especificar a interface de origem também:

python telnet.py google.com.br 443 192.168.2.1
