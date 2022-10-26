import numpy as np

def plus(a, b) :
    return a + b

def minus(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def divis(a, b) :
    return a / b 

def p1() :
    a, b = np.array(range(1, 11)), np.array(range(10, 101, 10))
    print(f'plus = {plus(a, b)}')
    print(f'minus = {minus(a, b)}')
    print(f'mul = {mul(a, b)}')
    print(f'divis = {divis(a, b)}')

def p2() :
    a = np.array(range(1, 11)) + np.array(range(10, 101, 10))
    print(a)
    print(f'shape = {a.shape}')
    print(f'size = {a.size}')
    

def p3(insert_type) :
    if insert_type == 1:
        heights = list(input('heights = ').split())
        weights = list(input('weights = ').split())
        bmi = list()
        for i in range(len(heights)) :
            bmi.append((int(weights[i]) / float(heights[i]) ** 2))
        
    elif insert_type == 2:
        heights = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
        weights = np.array([86, 74, 59, 95, 80, 68])
        bmi = weights / (heights ** 2)
    
    
    bmi = np.array(bmi)
    print(heights, '\n', weights)
    print(bmi)
    print(bmi[bmi > 25])

def p4() :
    n_arr = np.array(range(0, 25)).reshape(5, 5)
    
    print(f'1) \n{n_arr}')
    print(f'2) 첫 원소 : {n_arr[0, 0]} \n 마지막 원소 : {n_arr[-1, -1]}')
    print(f'3) \n{n_arr[:2, : ]}')

def p5() :
    arr1 = np.random.rand(3, 3)
    arr2 = np.random.rand(3, 3)
    arr3 = np.random.rand(3, 3)    
    n_arr = np.array([arr1, arr2, arr3])
    
    print(f'1) \n{n_arr}')
    print(f'2) 최댓값 : {n_arr.max()}')
    print(f'3) 최댓값 위치 : {n_arr.argmax() + 1}')
    
if __name__ == '__main__' :
    
    c_t = int(input('10.1 = 1, 10.2 = 2, BMI = 3, 5 x 5 = 4, 3 x 3 x 3 = 5\ninsert = '))
    
    if c_t == 1 :
        p1()
    elif c_t == 2 :
        p2()  
    elif c_t == 3 :
        do_insert = int(input('직접 입력 = 1 , 자동 입력 = 2\ninsert = '))
        p3(do_insert)
    elif c_t == 4 :
        p4()
    elif c_t == 5 :
        p5()
    else :
        print('ERROR')