import socket
import requests

host = '210.2.120.232'
ports = [80, 8080, 8081, 8082, 8083, 8084,
         8090, 8091, 8092, 8093, 8094]
for port in ports:
    # print(type(port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        #print("Port is Open")
        token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
        url = 'https://api.telegram.org/bot'
        chat_id = '-606599992'
        message = "_Port Up_\nFull Link is: {0}".format(
            host + ":" + str(port))
        params = {'chat_id': chat_id,
                  'text': message, 'parse_mode': 'Markdown'}
        respone = requests.post(url + token + '/sendMessage', params=params)
    else:
        #print("Port is Closed")
        token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
        url = 'https://api.telegram.org/bot'
        chat_id = '-606599992'
        message = "_Port Down_\nFull Link is: {0}".format(
            host + ":" + str(port))
        params = {'chat_id': chat_id,
                  'text': message, 'parse_mode': 'Markdown'}
        respone = requests.post(url + token + '/sendMessage', params=params)
    sock.close()
