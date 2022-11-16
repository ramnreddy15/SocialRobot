
src = open("img.txt", "r")

img = src.readlines()
img = [i.strip() for i in img]


for row in img:
    binary = int(row, 2)
    hex_val = hex(binary)
    print(hex_val, end=",")