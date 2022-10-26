#!/usr/bin/python3
import smtplib
fromaddr = 'nghialv@thaison.vn'
toaddr = 'luunghianghia@gmail.com'

msg = input('Enter Your Text Message: ')

username = 'nghialv@mail.com'
password = 'xxxx'

server = smtplib.SMTP('mail1.thaison.vn:587')
#server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
