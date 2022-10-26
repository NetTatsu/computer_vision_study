import numpy as np, cv2

img1 = np.full((300, 200, 3), 255, np.uint8)
img2 = np.full((300, 200), 255, np.uint8)

title1, title2 = 'window1', 'window2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
w, h = 600, 500
cv2.moveWindow(title1, 100, 100)
cv2.moveWindow(title2, 300, 400)
cv2.imshow(title1, img1)
cv2.imshow(title2, img2)
cv2.resizeWindow(title1, w, h)
cv2.resizeWindow(title2, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()