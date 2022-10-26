import numpy as np, cv2

image = np.full((600, 400, 3), 255, np.uint8)
pt = (100, 100, 200, 300)

title = '4-9'
red = (0, 0, 255)
cv2.namedWindow(title)
cv2.rectangle(image, pt, red, 3, cv2.LINE_4)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()



