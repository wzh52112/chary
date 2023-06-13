#coding=utf-8

from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别，中文识别
text=pytesseract.image_to_string(Image.open(r'C:\Users\11988\Desktop\爬取\2end.jpg'),lang='chi_sim')
print(text)

# print("\n")
# print('='*100)
# print("\n")

# #chi_tra
# text=pytesseract.image_to_string(Image.open('D:/workspace/pys/img/hanzi.jpg'),lang='chi_sim')
# print(text)
#
# print("\n")
# print('='*100)
# print("\n")
#
# #chi_tra
# text=pytesseract.image_to_string(Image.open('D:/workspace/pys/img/hanzi.jpg'),lang='chi_tra')
# print(text)