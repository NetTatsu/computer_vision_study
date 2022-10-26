import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full( shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]            

    for i, h in enumerate(hist):
        x = int(round(i * gap))                         
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)

data = [0, 2, 2, 1,
        1, 2, 3, 2,
        1, 2, 3, 2,
        1, 3, 1, 7]

img = np.reshape(data, (4, 4)).astype(np.uint8)
dst = cv2.equalizeHist(img)

print(img) 
print(dst)