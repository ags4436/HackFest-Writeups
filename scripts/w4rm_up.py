import base64

f = open('chall.txt', 'r')
flag = f.read()

while True:
  flag = base64.b64decode(flag).decode('utf-8')

  if '{' in flag:
    print(flag)
    break