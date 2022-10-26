import numpy as np, cv2

img = cv2.imread('.//image//sum_test.jpg', cv2.IMREAD_COLOR)

if img is None :
    raise Exception('영상파일 읽기 오류 발생')

mask = np.zeros(img.shape[:2], np.uint8)
mask[60: 160, 20:120] = 255

sum_value = cv2.sumElems(img) # 채널별 합 - 튜플로 반환
mean_value1 = cv2.mean(img) # 채널별 평균 - 튜플로 반환
mean_value2 = cv2.mean(img, mask)

print('sum_value 자료형 : ', type(sum_value), type(sum_value[0]))
print('[sum_value] = ', sum_value)
print('[mean_value1] = ', mean_value1)
print('[mean_value2] = ', mean_value2)

print()

# 평균, 표준편차 결과 저장

mean, stddev = cv2.meanStdDev(img)
mean2, stddev2 = cv2.meanStdDev(img, mask = mask)
print('mean 자료형 = ', type(mean), type(mean[0][0]))
print('[mean] = ', mean.flatten())
print('[stddev] = ', stddev.flatten())
print()

print('[mean2] = ', mean2.flatten())
print('[stddev2] = ', stddev2.flatten())
print()

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)