import numpy as np, cv2

ch0 = np.zeros((2, 4), np.uint8) + np.arange(1, 9).reshape(2, 4)
ch1 = np.ones((2, 4), np.uint8) * np.arange(10, 90, 10).reshape(2, 4)
ch2 = np.zeros((2, 4), np.uint8) + np.arange(11, 19).reshape(2, 4)

list_bgr = [ch0, ch1, ch2]
merge_bgr = cv2.merge(list_bgr)
split_bgr = cv2.split(merge_bgr)
print('list_bgr', np.array(list_bgr).shape)
print('split_bgr 행렬 형태', np.array(split_bgr).shape)
print('merge_bgr 행렬 형태', merge_bgr.shape)
print('[ch0] = \n%s' % ch0)
print('[ch1] = \n%s' % ch1)
print('[ch2] = \n%s' % ch2)
print('[merge_bgr] = \n%s' % merge_bgr)

print('[split_bgr[0]] = \n%s' % split_bgr[0])
print('[split_bgr[1]] = \n%s' % split_bgr[1])
print('[split_bgr[2]] = \n%s' % split_bgr[2])


# print(ch0)
