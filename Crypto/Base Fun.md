# Base Fun

> CipherText : QEgAAAoDAAAAALxtdFHz9fhaSgAAAEoAAAAIAAAAYmFzZS50eHQ5UkNqNWdVb0VXMTZWOTVSdHc3TDFjSE5FdHNMbzh5blZjS3NQSjZzWkViUHIyVVJmVXZvZVdoZFUzYXFhbmlHVThkY1FCcVhKa1BLAQI/AwoDAAAAALxtdFHz9fhaSgAAAEoAAAAIACQAAAAAAAAAIICkgQAAAABiYXNlLnR4dAoAIAAAAAAAAQAYAIDzxmBtv9YBgPi5pG2/1gGA88Zgbb/WAVBLBQYAAAAAAQABAFoAAABwAAAAAAA=

When you try to decode it online you can see there is Base.txt in it .This is the base64 of Zip file so to get zip file from base 64 just hit this command in terminal 


**$echo "base64 string" | base64 -d > abc.zip**


After getting the Zip you are unable to extract it first you have to change the Magic number of zip file then you are able to extract it .After changing the magic number of zip you can extract it and you can get text file which hase base58 encoding 

After decoding it you can get the flag 


Flag `hf0x01{every_encrypted_base_is_teach_us_something_new}`
