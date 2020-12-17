# Something Hidden 

`People are saying that wireshark capture everything and get the secret hidden in everything is that true I don't think`

Fo this challenge we are provided the pcap file so when you important the pcap file in your system you will and go to 

Analyze -> TCP 

you will see that data is transferred between with the http method not https so now we can extarct the http-objects from the pcap file for this go to

File -> Export objects -> HTTP 

Then simply save all in a folder and when you check the js files you find some files have key in it so firstly you have to find all the keys available for that you can simply use


`grep -irn "key"` it will give you all the keys but only one is correct from all that is `aGZ7SDRjazNyc180cjNfdzR0Y2gxbkd9` so know with this key you have to use steghide on the hacker.jpg you got from the wiresahrk it will give you the flag.txt.


Flag : hf0x01{H4ck3r5_4r3_3v3rywh3r3_4r3_Y0u_S3cur3D}