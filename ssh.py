#!/usr/pkg/bin/python

#Importing modules
import paramiko
import sys
import time

#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "10.11.214.143"
USER = "admin"
PASS = "passwd"
ITERATION = 3

#A function that logins and execute commands
def fn():
  client1=paramiko.SSHClient()
  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #connect to switch
  client1.connect(HOST,username=USER,password=PASS)
  print ("SSH connection to %s established", HOST)
  #Gather commands and read the output from stdout
  stdin, stdout, stderr = client1.exec_command('show version\n')
  print(stdout.read())
  stdin, stdout, stderr = client1.exec_command('show alarms | no-more\n')
  print(stdout.read())
  stdin, stdout, stderr = client1.exec_command( 'show processes memory | no-more\n')
  print(stdout.read())
  client1.close()
  print("Logged out of device %s", HOST)

#for loop to call above fn x times. Here x is set to 3
for x in range(ITERATION):
  fn()
  print("%s Iteration/s completed", (x+1))
  print("********")
  time.sleep(5) #sleep for 5 seconds