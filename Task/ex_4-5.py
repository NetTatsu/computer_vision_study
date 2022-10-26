import numpy as np, cv2

def first() :
    
    image = np.zeros((300, 400), np.uint8)
    image[:] = 100 # 밝기 100으로 조정

    title = '4-5-1' 
    title2 = '4-5-2'
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
    cv2.moveWindow(title, 100, 200) # x 좌표 = 100, y 좌표 = 200 만큼 윈도우의 위치를 이동
    cv2.imshow(title, image)
    cv2.imshow(title2, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def second() :
    image = np.zeros((400, 600, 3), np.uint8) # 3채널 컬러 영상 생성
    image[:] = (255, 255, 255)
    pt1, pt2 = (50, 100), (200, 300)
    
    cv2.line(image, pt1, pt2, (0, 255, 0), 5) # (50, 100)좌표에서 시작하여 (200, 300)좌표에서 종료, (0, 255, 0)은 색상[BGR순서]을 가르키는데 Green 색상의 굵기가 5인 선을 그린다
    cv2.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv2.LINE_4, 1)  #(200, 300)좌표에서 시작하여 (300, 400)좌표에서 종료, 색상은 Red로 4방향 연결선을 그린다
    cv2.imshow('Line & Rectangle', image) # 윈도우 title = Line & Rectangle
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__' :
    second()