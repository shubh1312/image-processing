import glob
import cv2
lis=glob.glob1(r"C:\Users\Admin\Desktop\image processing\Image size converter",'*.jpg')
print(lis)
for l in lis:
    img=cv2.imread(l,1)
    resize=cv2.resize(img,(img.shape[1]//4,
                           img.shape[0]//4))

    cv2.imwrite(str('size')+l,resize)

    cv2.imshow(l, resize)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()