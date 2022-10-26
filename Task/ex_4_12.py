
import numpy as np, cv2

def onChange(value) :
    global image, title
    
    add_value = value - int(image[0][0])
    image[:] = image + add_value
    cv2.imshow(title, image)
    
image = np.zeros((300, 500), np.uint8)


title = '4-12'
cv2.imshow(title, image)
bar_name = 'Brightness'
new_pos = 0
cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)

while True :
    key = cv2.waitKeyEx(100)
    if key == 27 :
        break
    try :
        now = cv2.getTrackbarPos(bar_name, title)
        if key == 2424832 :
            if now - 5 >= 0 :
                new_pos = now - 5
            else :
                new_pos = 0
        
        if key == 2555904 :
            if now + 5 <= 255 :
                new_pos = now + 5
            else :
                new_pos = 255
            
        cv2.setTrackbarPos(bar_name, title, new_pos)
    except KeyError:
        print('KeyError')
        
cv2.destroyAllWindows()