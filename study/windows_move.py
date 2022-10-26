import numpy as np, cv2

def make_window(title, size_type) :
    if size_type == 1 :
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    elif size_type == 2 :
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        
def move_window(title, w, h) :
    cv2.moveWindow(title, w, h)
    

def show_window(title, image) :
    cv2.imshow(title, image)
    
if __name__ == '__main__':
    img_mat = np.zeros((200, 400), np.uint8)
    img_mat[:] = 200
    
    title1, title2 = 'Position1', 'Position2'
    # default :  title1 = Autosize, title2 = Normal
    make_window(title1, 1)
    make_window(title2, 2)
    
    move_window(title1, 150, 150)
    move_window(title2, 400, 50)
    
    show_window(title1, img_mat)
    show_window(title2, img_mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    