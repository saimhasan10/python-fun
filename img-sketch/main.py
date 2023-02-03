import cv2
image = cv2.imread("3.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_img)
blur = cv2.GaussianBlur(invert, (21,21),0)
invert_blur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img, invert_blur, scale=256.0)

cv2.imwrite("sketch-2.png", sketch)