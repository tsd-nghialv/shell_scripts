import requests


server = 'https://thuphihatang.tphcm.gov.vn:'
ports = ['80', '8080', '8081', '8082', '8083', '8084',
         '8090', '8091', '8092', '8093', '8094']
for port in ports:
    try:
        url = server+port
        #url_api = url_begin + str(input("Nhập URL:") + port)
        req = requests.get(str(server+port), verify=False)
        # print(url)
        output = req.status_code
        if "200" in str(output):
            token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
            url = 'https://api.telegram.org/bot'
            chat_id = '-606599992'
            message = "***STATUS:*** _Success_\nFull Link is: {0} ".format(
                server+port)
            params = {'chat_id': chat_id,
                      'text': message, 'parse_mode': 'Markdown'}
            respone = requests.post(
                url + token + '/sendMessage', params=params)
            # print("Success\nStatus is: {0}\nFull Link: {1}\n".format(
            # output, server+port))
            # print("OK")
        elif "404" in str(output):
            #print("Not Found")
            token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
            url = 'https://api.telegram.org/bot'
            chat_id = '-606599992'
            message = "***STATUS:*** _Not Found_\nFull Link is: {0} ".format(
                server+port)
            params = {'chat_id': chat_id,
                      'text': message, 'parse_mode': 'Markdown'}
            respone = requests.post(
                url + token + '/sendMessage', params=params)
        elif "403" in str(output):
            #print("Server Internal Error")
            token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
            url = 'https://api.telegram.org/bot'
            chat_id = '-606599992'
            message = "***STATUS:*** _Forbidden: Access is denied._\nFull Link is: {0} ".format(
                server+port)
            params = {'chat_id': chat_id,
                      'text': message, 'parse_mode': 'Markdown'}
            respone = requests.post(
                url + token + '/sendMessage', params=params)
        elif "500" in str(output):
            #print("Server Internal Error")
            token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
            url = 'https://api.telegram.org/bot'
            chat_id = '-606599992'
            message = "***STATUS:*** _Server Internal Error_\nFull Link is: {0} ".format(
                server+port)
            params = {'chat_id': chat_id,
                      'text': message, 'parse_mode': 'Markdown'}
            respone = requests.post(
                url + token + '/sendMessage', params=params)

        # print(req.headers['server'])
        # print(req.text)
        # print(req.encoding)
        else:
            #print("Status Code: {}".format(output))
            token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
            url = 'https://api.telegram.org/bot'
            chat_id = '-606599992'
            message = "***STATUS CODE: ***{0}\nFull Link is: {1} ".format(
                output, server+port)
            params = {'chat_id': chat_id,
                      'text': message, 'parse_mode': 'Markdown'}
            respone = requests.post(
                url + token + '/sendMessage', params=params)
# except requests.exceptions.ConnectionError:
    except Exception as e:
       # print(e)
        token = '5542561908:AAGGlo2WYnvC_9ONjprPUponitwSEd1pvck'
        url = 'https://api.telegram.org/bot'
        chat_id = '-606599992'
        message = "_Không tồn tại Port: {0}_\nFull Link is: {1}".format(
            port, server+port)
        params = {'chat_id': chat_id,
                  'text': message, 'parse_mode': 'Markdown'}
        respone = requests.post(url + token + '/sendMessage', params=params)
    finally:
        pass
