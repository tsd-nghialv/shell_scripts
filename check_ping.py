
import requests
import os
host = ['113.160.86.242', '']
for hosts in host:
    cmd = os.system('ping -c4 ' + hosts)
    if cmd != 0:
        token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
        url = 'https://api.telegram.org/bot'
        chat_id = '-711836222'
        message = "*Critical:* *WAN Down*\n{}".format(hosts)
        params = {'chat_id': chat_id,
                  'text': message, 'parse_mode': 'Markdown'}
        respone = requests.post(url + token + '/sendMessage', params=params)
    else:
        print("")
