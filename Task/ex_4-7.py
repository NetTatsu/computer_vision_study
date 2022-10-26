import numpy as np, cv2

def first() :
    
    image = np.zeros((300, 400, 3), np.uint8)
    image[:] = (255, 255, 255)

    pt1, pt2 = (50, 130), (200, 300)

    cv2.line(image, pt1, (100, 200), (255, 0, 0)) # 색상, 선의 굵기[default값 존재]
    cv2.line(image, pt2, pt1, (100, 100, 100), 3) # 좌표가 하나라서 에러
    cv2.rectangle(image, pt1, pt2, (255, 0, 255)) # 문제없음 직사각형 그림
    cv2.rectangle(image, pt1, pt2, (0, 0, 255)) # 문제없음 직사각형 그림

    title = 'Line & Rectangle'
    cv2.namedWindow(title)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
