import image as i

if __name__ == '__main__':  
    DIR = './/image//'
    filename = 'read_color.jpg'
    
    im = i.Image(DIR, filename)
    img = im.get_image(2)
    
    params_jpg = im.set_img__quality(10)
    params_png = im.set_img_compression(9)
    
    im.write_img('write_test1.jpg')
    im.write_img('write_test2.jpg', params_jpg)
    im.write_img('write_test3.png', params_png)
    im.write_img('write_test4.bmp')