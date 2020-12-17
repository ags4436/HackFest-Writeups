from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()


f = Fernet(key)

with open('flag.txt.gpg', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('flag.txt.gpg', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)