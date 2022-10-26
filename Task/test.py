from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import pickle
if __name__ == '__main__':
    DIR = './/graph//'
    files = glob(f'{DIR}*.png')
    names = 'SongNames.pickle'
    with open(f'{DIR}{names}', 'rb') as f :
        df = pickle.load(f)
    # print(files)
    df = df.to_numpy()
    print(df)
    img = cv2.imread(files[10])
    # # plt.imshow(img)
    # # plt.show()
    # # print(img.shape)
    h = img.shape[0]
    w = img.shape[1]
    ch = 3
    print(h, w)
    
    images = np.zeros((len(files),h, w, ch))
    # # print(images.shape)
    for n, file in enumerate(files):
        image = cv2.imread(files[n])
        images[n, :, :, :] = image
    
    print(images.shape)