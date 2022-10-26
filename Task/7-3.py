import numpy as np, cv2

def calc_histo(image, hsize, ranges=[0, 256]):
    hist = np.zeros((hsize, 1), np.float32)
    gap = ranges[1] / hsize 

    for row in image:
        for pix in row:
            idx = int(pix / gap)
            hist[idx] += 1
    return hist

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]            

    for i, h in enumerate(hist):
        x = int(round(i * gap))                         
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)                 


data = [5, 4, 6, 6,
        2, 1, 6, 4,
        2, 2, 4, 6,
        1, 6, 0, 2]

img = np.reshape(data, (4, 4)).astype(np.uint8)
ranges = [0, 6] 
hist = cv2.calcHist([img], [0], None, [4], ranges)
hist_img = draw_histo(hist)

cv2.imshow('hist_img', hist_img)
cv2.waitKey(0)