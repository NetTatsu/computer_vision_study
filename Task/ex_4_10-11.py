import numpy as np, cv2

def onMouse(event, x, y, flags, param = None) :
    global title, bold, r # 전역 변수 참조
    pt = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.rectangle(image, pt + (30, 30), (255, 0, 0), bold)
    elif event == cv2.EVENT_RBUTTONDOWN :
        cv2.circle(image, pt, r, (0, 255, 0), bold) # pt + (30, 30) 은 pt가 튜플 정수값으로 지정되어있기에 변경 불가능 pt + (30, 30) = (x, y, 30, 30)  
    cv2.imshow(title, image)

def bold_onChange(value) : 
    global title, bold
    
    add_value = value - bold
    bold = bold + add_value
    cv2.imshow(title, image)
    
def r_onChange(value) :
    global title, r
    
    add_value = value - r
    r = r + add_value
    cv2.imshow(title, image)
    
image = np.full((600, 500, 3), 255, np.uint8)
bold = 3
r = 20
title = '4-10'
r_name = 'r'
bold_name = 'bold'
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar(r_name, title, r, 50, r_onChange)
cv2.createTrackbar(bold_name, title, bold, 10, bold_onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()    