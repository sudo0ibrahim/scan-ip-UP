# scan-ip-UP
## how to use ? / ? كيف تستخدم 
```sh
chmod +x scanip.py
```
```sh
./scanip.py 192.168.1
```
or
```sh
python3 scanip.py 192.168.1
```
## Example / مثال
```sh
ibrahim@chc:~$ python3 scanip.py 192.168.1
192.168.1.0 the Host is DOWN
192.168.1.1 the Host is UP
192.168.1.2 the Host is DOWN
192.168.1.3 the Host is UP
192.168.1.4 the Host is UP
192.168.1.5 the Host is DOWN
192.168.1.6 the Host is DOWN
192.168.1.7 the Host is UP
192.168.1.8 the Host is DOWN
192.168.1.9 the Host is DOWN
192.168.1.10 the Host is DOWN
192.168.1.11 the Host is DOWN
```
### Why only 255 ? / ? لماذا فقط 255

1 Byte = 8 bit

1+2+4+8+16+32+64+128 = 255

Example / مثال

|1|2|4|8|16|32|64|128|
|-|-|-|-|-|-|-|-|
|0|0|0|0|0|0|1|1|
|0|0|0|1|0|1|0|1|
|1|0|0|0|0|0|0|0|
|0|0|1|1|0|1|0|0|

192.168.1.44
