import requests
username = 'thaison'
pasword = 'xxxx'
receiver = '0987492093'
content = 'Test'
target = '0987492093'
url = 'http://g3g4.vn:8008/smsws/services/SendMT?wsdl'
headers = {'content-type': 'text/xml'}
body = '''<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sms="http://sms.neo">
   <soapenv:Header/>
   <soapenv:Body>
      <sms:sendSMS>
         <!--Optional:-->
         <sms:username>{0}</sms:username> 
         <!--Optional:-->
         <sms:password>{1}</sms:password>
         <!--Optional:-->
         <sms:receiver>{2}</sms:receiver>
         <!--Optional:-->
         <sms:content>{3}</sms:content>
         <!--Optional:-->
         <sms:loaisp>2</sms:loaisp>
         <!--Optional:-->
         <sms:brandname>THAISON</sms:brandname>
         <!--Optional:-->
         <sms:target>{4}</sms:target>
      </sms:sendSMS>
   </soapenv:Body>
</soapenv:Envelope>'''.format(username, pasword, receiver, content, target)
response = requests.post(url, data=body, headers=headers)
print(response.text)
