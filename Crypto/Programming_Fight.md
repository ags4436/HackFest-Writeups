#Programmming Fight 

Description States 

`Me and my friend want security so we so we digest our password five times with our programming skills. Now we Think we are secured and no one guess our password. Is it true ?`

Hint : Next File Name Matters a Lot


So from the description we can get that password is 5 times digested which clearly states that it is MD5 hash and from hint we get that next file is important.

We are provided with the a zip name 1300.zip and it is password protected. So if we combine all the hint what we collect till yet then we can got that password will be MD5 hash of the name of the next file. To solve this you can simply write python script to extract all the zip.

```
import os
import hashlib
j=1
for i in range(1301,0,-1):
	prev = i-j
	p = hashlib.md5(str(prev).encode())
	p = p.hexdigest()
	print(f"{i}"+f".zip password: {p}")
	os.system(f'unzip -P {p} {i}.zip ')

```
so after this you get the 0.zip then if you see 0.zip it have flag.txt in it. Apply the same concept on it just MD5 of the flag and use as a password you will get flag.txt. Which have your flag.


Flag : `hf0x01{T7h1$_sh0w$_Y0u_Kn0w_pr0gr4mm1nG_4nD_ha$1nG_v3rY_W3LL}`