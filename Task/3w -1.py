import numpy as np

if __name__ == '__main__':
    # arr = [1.01, 1.7, 2, 1.7, 1.01, 0.3, 0, 0.3]
    # result = list()
    # for i in arr :
    #     if float(i) >= 0 and float(i) <= 1/3 :
    #         r = '00'
    #     elif float(i) > 1/3 and float(i) <= 1 :
    #         r = '01'
    #     elif float(i) > 1 and float(i) <= 5/3 :
    #         r = '10'
    #     elif float(i) > 5/3 and float(i) <= 2 :
    #         r = '11'
    #     result.append(r)
        
    # for i in result :
    #     print(i, end = ' ')
        
    arr = [1.1, 1.6, 2, 1.6, 1.1, 0.3, 0, 0.3]
    result = list()
    
    for i in arr :
        if float(i) >= 0 and float(i) <= 1/7 :
            r = '000'
        elif float(i) > 1/7 and float(i) <= 3/7 :
            r = '001'
        elif float(i) > 3/7 and float(i) <= 5/7 :
            r = '010'
        elif float(i) > 5/7 and float(i) <= 1 :
            r = '011'
        elif float(i) > 1 and float(i) <= 9/7 :
            r = '100'
        elif float(i) > 9/7 and float(i) <= 11/7 :
            r = '101'
        elif float(i) > 11/7 and float(i) <= 13/7 :
            r = '110'
        elif float(i) > 13/7 and float(i) <= 2 :
            r = '111'    
        result.append(r)
        
    for i in result :
        print(i, end = ' ')