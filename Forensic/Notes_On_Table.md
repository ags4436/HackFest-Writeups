# Notes On Desk

`
Our team get information that one hacker group is going to orgainze a meeting and they are planning which can be threat to the nation. So when we raided the house of one on the member of that hacker group we get lot's of pieces of paper on the desk. can you help us to find what is that message`


We are also given with the zip file having 600 images pieces. So from the first sight we can get to know that we have to join all the images to get the flag.


So in this you have to google how to contact the imgaes and join them all.

If you not find any refer [THIS](https://note.nkmk.me/en/python-pillow-concat-images/).

So to solve this i wrote the script using PIL and numpy module in python to merge or contact all of them.

CODE 

```
import numpy as np
import PIL
from PIL import Image
list_im=[]
for b in range(0,500):
	list_im.append(f"robot-{b}.jpg")

def get_concat_v(list_im):
    dst = Image.new('RGB', (600,600))
    height_add = 0 
    for item in list_im:
    	print(item)
    	img = Image.open(item)
    	
    	print(height_add)
    	dst.paste(img, (height_add, 0 ))
    	# height_add+=item.height
    	height_add+=img.width
    # dst.paste(im2, (0, im1.height))
    return dst


get_concat_v(list_im).save('hackfest.jpg')
```

After running this code it will combine all images and you will get the flag.


Flag : hf0x01{3nj0y_7h3_3v31ng_w17h_u$}