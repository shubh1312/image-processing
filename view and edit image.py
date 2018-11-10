import cv2

img=cv2.imread(r'C:\Users\Admin\Desktop\image processing\166 galaxy.jpg',1)
print(img)
print(type(img))
print(img.shape)
print(img.ndim)

resized_img=cv2.resize(img,(img.shape[1]//2,
                            img.shape[0]//2 ))

cv2.imwrite('galaxy_resized2.jpg',resized_img)

cv2.imshow('galaxy',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()