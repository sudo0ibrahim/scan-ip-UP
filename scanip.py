#!/usr/bin/python3

import subprocess
import sys

if len(sys.argv)==1: sys.exit("taip error! please check the options.")

ip =  sys.argv[1]

count = 0
for f in range(0,255):
		
	host = f"{ip}.{f}"

	scan = subprocess.call(['ping','-c','1',host],stdout=subprocess.PIPE)

	if scan == 0:

		print(f"{host} the Host is UP")

	else:
		print(f"{host} the Host is DOWN")
	

	count = count + 1

print(f"scanned {count} systems")