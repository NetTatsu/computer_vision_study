import image as i
import numpy as np
def get_title(img_type) :
    if img_type == 1:
        t1, t2 = 'gray2gray', 'gray2color'
    elif img_type == 2:
        t1, t2 = 'color2gray', 'color2color'
    
    return t1, t2

if __name__ == '__main__': 
    DIR = './/image//'
    
    img_type = int(input('gray = 1 , color = 2\ninsert = '))
    
    if img_type == 1:
        filename = 'read_gray.jpg'
        title1, title2 = get_title(img_type)
        
    elif img_type == 2:
        filename = 'read_color.jpg'
        title1, title2 = get_title(img_type)
        
    img = i.Image(DIR, filename)
    _2gray = img.get_image(1)
    _2color = img.get_image(2)
    
    img.check_exception(_2gray, _2color)
    print('행렬좌표 [100, 100] 화소값')
    print('%s %s' % (title1, _2gray[100, 100]))
    print('%s %s\n' % (title2, _2color[100, 100]))
    
    img.print_matInfo(title1, _2gray)
    img.print_matInfo(title2, _2color)
    arr = np.array(_2color)
    print(arr.shape)
    img.show_img(title1, _2gray)
    img.show_img(title2, _2color)
    img.fin_img()
    
    
    