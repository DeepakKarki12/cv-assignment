import cv2
import matplotlib.pyplot as plt

# read the image file in a grayscale mode
img = cv2.imread('r9.png',0)

# variable declaration
sum = 0
count = 0

# logic :- taking average of the value of array of the image so that we can get the threshold value
for i in img:
    for j in i:
        sum = sum+j
        count+=1
avg = int(sum/count)

# converting the grayscale image into binary_inv so that we can the foreground as 1 and background as 0
ret, bw_img = cv2.threshold(img, avg,255, cv2.THRESH_BINARY_INV)

#now converting the gray image to bgr so that we can get the black and white image
black_and_white = cv2.cvtColor(bw_img,cv2.COLOR_GRAY2BGR)

plt.imshow(black_and_white)
plt.show()
print(bw_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
