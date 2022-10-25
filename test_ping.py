import requests
import os
host = '210.245.51.189'
cmd = os.system('ping -c4 ' + host)
if cmd != 0:
    token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
    url = 'https://api.telegram.org/bot'
    chat_id = '-711836222'
    message = "*Critical:* *WAN Down*"
    params = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    respone = requests.post(url + token + '/sendMessage', params=params)
else:
    print("")
