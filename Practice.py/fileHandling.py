f = open("img.png", "rb")

f1 = open("img_copy.png", "wb")

print(f.read())

for i in f:
    f1.write(i)
