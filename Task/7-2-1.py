import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)
m2 = np.full((3, 6), 50, np.uint8)

m_mask = np.zeros(m1.shape, np.uint8)
m_mask[:, 3:] = 1

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1, m2, mask = m_mask)

print('add1 = ', m_add1,'\n add2= ',  m_add2)