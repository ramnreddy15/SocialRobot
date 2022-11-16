from PIL import Image

file = "Smiley8x8"
img = Image.open(file+'.png')
gray = img.convert('L')
img = gray.point(lambda x: 1 if x<128 else 0, '1')
with open(file+'.txt', 'w') as f:
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            f.write(str(img.getpixel((j,i))))
        if(i!=img.size[0]-1):
            f.write("\n")
f.close()

src = open(file+".txt", "r")

img = src.readlines()
img = [i.strip() for i in img]


for row in img:
    binary = int(row, 2)
    hex_val = hex(binary)
    print(hex_val, end=",")