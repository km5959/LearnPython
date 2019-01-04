import cv2
import math

img = cv2.imread(r'C:\Users\Administrator\Desktop\logo.png', cv2.IMREAD_GRAYSCALE)

# print(img)

# print(img.shape)  # 图像的宽度、高度和通道数
# print(img.size)  # 图像的像素大小
# print(img.dtype)  # 图像的数据类型

f = open(r'C:\Users\Administrator\Desktop\out.txt', 'w')

string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."
unit = math.ceil((255 / len(string)))
print(img[69, 224])  # 图片大小 70*225
# px = img[10, 10]
for y in range(0, 17):
    f.write('\n')
    for x in range(0, 112):
        if img[y * 4, x * 2] != 255:
            print(y * 4, x * 2)
            f.write(string[int(math.floor(img[y * 4, x * 2] / unit))])
            # print(, file=f)
            #
        else:
            f.write(' ')
f.close()
