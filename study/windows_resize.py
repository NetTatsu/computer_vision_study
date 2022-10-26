import numpy as np, cv2

def resize_window(title, w, h) :
    cv2.resizeWindow(title, w, h)
    
def make_window(title, size_type) :
    if size_type == 1:
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
    elif size_type == 2:
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    
def show_window(title, image) :
    cv2.imshow(title, image)
    
if __name__ == '__main__':
    img_mat = np.zeros((200, 300), np.uint8)
    img_mat.fill(255)
    
    title1, title2 = 'Autosize', 'Normal'
    make_window(title1, 1)
    make_window(title2, 2)
    
    show_window(title1, img_mat)
    show_window(title2, img_mat)
    
    resize_window(title1, 400, 300)
    resize_window(title2, 400, 300)
    cv2.waitKey(0)
    cv2.destroyAllWindows()