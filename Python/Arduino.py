#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import serial
from time import sleep

# iniciar a comunicação Serial
serialcomm = serial.Serial('COM5', 9600, timeout=1)

# leitura dos sensores fica atualizando e imprimindo na tela
while True:

    i = 't'
    serialcomm.write(i.encode())
    sleep(0.1)
    print(serialcomm.readline().decode('ascii'))


''' para acender o led teste
while True:
    i = input("input (on / off): ").strip()
    if i == 'done':
        print('finished programa')
        break
    serialcomm.write(i.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

serialcomm.close()
'''
