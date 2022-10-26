import numpy as np, cv2

mat1 = np.full((200, 300), 100, np.uint8)
mat2 = np.full((200, 300), 100, np.uint8)

title1 = 'mode1'
title2 = 'mode2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE)

w, h = 300, 180 # 가로 300, 높이 180 
cv2.moveWindow(title1, 0, 0) # (0, 0)좌표에 title1 윈도우 이동
cv2.moveWindow(title2, w, h) # (300, 180)좌표에 title2 윈도우 이동
cv2.imshow(title1, mat1)
cv2.imshow(title2, mat2)
cv2.waitKey(0)
cv2.destroyAllWindows()