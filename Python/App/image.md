# Tool

## Remove image background
```
from PIL import Image
from rembg import remove

img_in = Image.open('test.jpg')
remove(img_in).save('new.png')
```
