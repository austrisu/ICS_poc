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



resault = []


payload1 = [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x06\x01\x05\x00\xa1\x00\x00', b'\x00\x3c\x00\x00\x00\x00\x01\x05\x00\xa1\x00\x00',
b'\x00\x3c\x00\x00\x00\x06\x00\x05\x00\xa1\x00\x00',
b'\x00\x3c\x00\x00\x00\x06\x01\x00\x00\xa1\x00\x00',
b'\x00\x3c\x00\x00\x00\x06\x01\x05\x00\x00\x00\x00']



ports = [500, 502, 503, 506]

for port in range(102,103):
	print(port)
	print('---')
	for pay in payload1:
		temp = inject(pay, port)
		if temp == 0:
			break;
		resault.append('Port ' +  str(port) + ' retrns : ' + str(temp))
		time.sleep(1)
	time.sleep(1)


for res in resault:
	print(res)







