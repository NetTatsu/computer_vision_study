import cv2 

class Image :
    def __init__(self, DIR, filename) :
        self.DIR = DIR
        self.filename = filename
        
    def __del__(self) :
        print('delete Image')
        
    def get_image(self, input_type) :
        
        if input_type == 1 :
            cv_type = cv2.IMREAD_GRAYSCALE
        elif input_type == 2:
            cv_type = cv2.IMREAD_COLOR
            
        self.img = cv2.imread(f'{self.DIR}{self.filename}', cv_type)
        
        return self.img

    def print_matInfo(self, title, img) :
        if img.dtype == 'uint8' :
            mat_type = 'CV_8U'
        elif img.dtype == 'int8' :
            mat_type = 'CV_8S'
        elif img.dtype == 'uint16' :
            mat_type = 'CV_16U'
        elif img.dtype == 'int16' :
            mat_type = 'CV_16S'
        elif img.dtype == 'float32' :
            mat_type = 'CV_32F'
        elif img.dtype =='float64' :
            mat_type = 'CV_64F'

        nchannel = 3 if img.ndim == 3 else 1
        
        print('%12s : depth(%s), channels(%s), -> mat_type(%sC%d)' % (title, img.dtype, nchannel, mat_type, nchannel))

    def check_exception(self, gray, color) :
        if gray is None or color is None :
            raise Exception('Error')
    
    def show_img(self, title, img) :
        cv2.imshow(title, img)
    
    def fin_img(self) :
        cv2.waitKey(0)
        
    def set_img__quality(self, num) :
        img = (cv2.IMWRITE_JPEG_QUALITY, num)
        return img

    def set_img_compression(self, num) :
        img = [cv2.IMWRITE_PNG_COMPRESSION, num]
        return img

    def write_img(self, name, write_type = None) :
        if write_type is None :
            cv2.imwrite(f'{self.DIR}{name}', self.img)
            print('Ok')
        else :
            cv2.imwrite(f'{self.DIR}{name}', self.img, write_type)
            print('Ok')