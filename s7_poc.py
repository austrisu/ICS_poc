#!/usr/bin/python -tt

# Switching Q1 of 1200 controler

# RESOURCES
# 

import snap7
import sys

target_ip = input('Enter target IP: ')

if target_ip == str(1):
	target_ip = '192.168.1.203'

plc = snap7.client.Client()
plc.connect(str(target_ip),0,1)

print('Connected to %s' % target_ip)

print('Chose what to do:')
print('1. Read from DB')
print('2. Read from Outputs')
print('3. Writing to DB')
print('4. Writing to Output')
print('5. Read PLC status')

item = int(input('Chose Number: '))

def read_from_db(plc, db_num, mem_start, size=1):


	try:
		res = plc.db_read(db_num, mem_start, size)
	except Exception as err:
		print(err)
		return err
	return res

def read_from_q(plc, area, db_num, mem_start, size=1):

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



