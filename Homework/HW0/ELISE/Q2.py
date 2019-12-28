from PIL import Image

lena = Image.open("/Users/chenxinranshen/Desktop/ML/ML_homework.notsync/NTU-Machine-learning/李宏毅机器学习-作业/HW0/01-Data/lena.png")
lena_modified = Image.open("/Users/chenxinranshen/Desktop/ML/ML_homework.notsync/NTU-Machine-learning/李宏毅机器学习-作业/HW0/01-Data/lena_modified.png")
w,h = lena.size


img= Image.new("RGB", (w,h))
for i in range (h):
    for j in range (w):
        if lena.getpixel((i,j))!=lena_modified.getpixel((i,j)):
            # r,g,b = lena_modified.getpixel((i,j))
            pixel = lena_modified.getpixel((i,j))
            r, g, b = pixel[0], pixel[1], pixel[2]
            print(r,g,b)
            img.putpixel((i,j),(r,g,b))
img.show()

