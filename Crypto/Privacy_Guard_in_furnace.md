#Privacy Guard in furnace


`I am completing my python project and then suddenly one person shouted that your furnance is started and your privacy guard is in danger. Till I reached there our guard is in critical condition. He told me about a file which have the secret code for the treasure and he give me the key. But I think files is protected can you help me to get the secret code`


From it cleares give some like python anf file give hint that it is gpg file and a key is given and a secret.asc key.

So this is simple we have to search from google how python encrytion work then you will one article about fernet encryption from [HERE](https://pyshark.com/encrypt-and-decrypt-files-using-python/)

You will get to know that fernet required a key to decoded any file so we can write code to decode the fernet encrypted flag.txt.gpg file.

After that you have to import the gpg secret file with command 

`gpg --import secret.asc`

But during this it ask for password for password you have to bruteforce the secret.asc with john the ripper

```
gpg2john secret,asc > hash.txt
john --wordlist=rockyou.txt hash.txt
```

You will get password `pazaway`

Then you will import the secret.asc easily

After that you can decrypt the flag.txt.gpg with command

`gpg -d -o decrypted.txt flag.txt.gpg`

Then you can the flag.

Flag : hf0x01{Y0u_4r3_r34L_Cr4ck3r_BuddY}

For more study of GPG you can refer : [This](https://www.tutorialspoint.com/how-to-encrypt-and-decrypt-a-file-using-gpg-command-on-linux) 