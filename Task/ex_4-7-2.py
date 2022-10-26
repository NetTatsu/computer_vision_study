import numpy as np, cv2

def onMouse(event, x, y, flags, param = None) :
    global title
    pt = (x, y)
    pt2 = (x + 30, y + 30)
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(image, pt, 5, 100, 1)
    elif event == cv2.EVENT_RBUTTONDOWN :
        cv2.rectangle(image, pt, pt2, 100, 2) # pt + (30, 30) 은 pt가 튜플 정수값으로 지정되어있기에 변경 불가능 pt + (30, 30) = (x, y, 30, 30)  
    cv2.imshow(title, image) # 들여쓰기로 인해 오른쪽 버튼 누를시에만 실행 되었다.

image = np.ones((300, 300), np.uint8) * 255

title = 'Draw Event'
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

