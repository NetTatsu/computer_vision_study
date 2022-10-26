import numpy as np, cv2

image = np.zeros((300, 400))
image[:] = 100
new_size = (500, 600)

title = '4-6'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE) # 4-6 이름을 가지고, autosize로 image 행렬 크기 고정
cv2.imshow(title, image)
cv2.resizeWindow(title, 500, 600) # 윈도우 사이즈 변경
cv2.waitKey(0)
cv2.destroyAllWindows()