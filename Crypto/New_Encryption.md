#New Encyption

Description : 
`Today we are able to crack any hashing and encryption. so I feel insecure to send message in plain text or by using old technequies so I developed my new way to encrypt the message. Let's see can anyone crack it :>`

With this we have python file and a hash file. If we check the Python script.



```
import hashlib

flag = "**REDACTED**"
result = ""
md5_cipher=""
for p in flag:
  p = hashlib.md5(p.encode())
  p = p.hexdigest()
  md5_cipher +=str(p)
for n in md5_cipher:
 
  n = hashlib.sha1(n.encode())
  n = n.hexdigest()
  result += str(n)

f = open('hash.txt','w')
f.write(result)
f.close()

```


So from it we can clearly sees that flag is hashed MD5 letter by letter and after that MD5 hash value is hashed SHA1 leter by letter.
It means we have to reverse the process and get the flag.

So I wrote the python script for this which I break down into parts. So that you can get better how it works.

Firstly I made a dict having all alphabets, numbers and special character as key and their sha1 value as value of the dict.

code :

```
#creating of sha of every letter 
import hashlib
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_}{1234567890~`!@#$%^&*()-=+:][?/.>,<|'
dict_cipher = {}
for i in letter:
    i1 = hashlib.sha1(i.encode())
    i1   = i1.hexdigest()
    dict_cipher[i] = i1
print(dict_cipher)

```

result :

```
{'a': '86f7e437faa5a7fce15d1ddcb9eaeaea377667b8', 'b': 'e9d71f5ee7c92d6dc9e92ffdad17b8bd49418f98', 'c': '84a516841ba77a5b4648de2cd0dfcb30ea46dbb4', 'd': '3c363836cf4e16666669a25da280a1865c2d2874', 'e': '58e6b3a414a1e090dfc6029add0f3555ccba127f', .......................

```


Since we know that sha1 is of length 40 and the total length 80640 so we have to make list of the complete hash given in the file and each element of the list shoould of length so that each element represent the each charcter of the md5 string.

Code : 
```
sha1cipher = Copy_SHA1_Cipher_Here
i=0
n=0
parts = []
for t in range(2016):
  n= i+40
  parts.append(sha1cipher[i:n])
  i+=40

f = open('sha.txt','w')
f.write(str(parts))
f.close()
```

It Will give you list of sha1 cipher of each element of md5 string and now bruteforce it with the list of sha1 of alphabets numbers and symbol to get MD5 string.

Code : 

```
import hashlib
ciphered_text = list_of_cipher_value_from above 
Sha_value = dict_sha_values of all_alphabets
sha_value_value = list(sha_value.values())
sha_value_key = list(sha_value.keys())
decoded = ''
i = 0
print(len(ciphered_text))
for n in ciphered_text:
    i+=1
    n = sha_value_key[sha_value_value.index(n)]
    decoded+=n

print(len(decoded))
f = open('sha_decoded.txt','w')
f.write(str(decoded))
f.close()


```

After this repeat same step for MD5 you will get the flag

code :

```
md5cipher = md5_string_you_get_from_sha1
i=0
n=0
parts = []
for t in range(63):
  n= i+32
  parts.append(md5cipher[i:n])
  i+=32

f = open('md5.txt','w')
f.write(str(parts))
f.close()


DECODING MD5 TO plain
ciphered_text = list_of_cipher_value_from above
md5_value = dict_MD5_values of all_alphabets
md5_value_value = list(md5_value.values())
md5_value_key = list(md5_value.keys())
decoded = ''
i = 0
print(len(ciphered_text))
for n in ciphered_text:
    i+=1
    n = md5_value_key[md5_value_value.index(n)]
    decoded+=n
    
print(decoded)

```

Complete code will be in [file](https://github.com/VulnFreak/HackFest-Writeups/blob/main/scripts/decrypt.py)

Flag :  hf0x01{N0w_y0u_4r3_r3ady_f0r_7h3_3ncryp710n_j0urn3y_may_y0u_3nj0y3d_I7}
