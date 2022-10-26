import numpy as np, cv2

def set_key_value() :
    switch_case = {
        ord('a') : 'a키 입력',
        ord('b') : 'b키 입력',
        0x41 : 'A키 입력',
        int('0x42', 16) : 'B키 입력',
        2424832 : '왼쪽 화살표키 입력',
        2490368 : '윗쪽 화살표키 입력',
        2555904 : '오른쪽 화살표키 입력',
        2621440 : '아래쪽 화살표키 입력'
    }
    
    return switch_case

def make_window(title, size_type) :
    if size_type == 1 :
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    elif size_type == 2 :
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        
def show_window(title, image) :
    cv2.imshow(title, image)
    
if __name__ == '__main__':
    img_mat = np.ones((200, 300), np.float)
    title = 'Keyboard Event'
    
    make_window(title, 1)
    show_window(title, img_mat)
    
    key_case = set_key_value()
    
    while True :
        key = cv2.waitKeyEx(100)
        if key == 27 :
            break
        
        try :
            result = key_case[key]
            print(result)
        except KeyError :
            result = -1
    
    cv2.destroyAllWindows()