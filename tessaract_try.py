import pytesseract
from PIL import Image
import cv2

#img = Image.open(r"C:\Users\Admin\Desktop\image processing\download.png")
img=cv2.imread(r"C:\Users\Admin\Desktop\sudoku\opencv-python-master\sudoku\test1.jpg")

img=cv2.resize(img,(img.shape[1],img.shape[0]))
cv2.imshow('orignal',img)


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray_img)


ret , threshold=cv2.threshold(gray_img,127,225,cv2.THRESH_BINARY_INV)
cv2.imshow('threshold',threshold)

final=cv2.bitwise_not(threshold)
cv2.imshow('final',final)
cv2.waitKey(0)
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
result= pytesseract.image_to_string(final)
print(result)