import math
def mySqrt(x):
    res = 1
    for i in range(20):
        temp = res
        res = temp - (temp**2 - x)/(2 * temp)
    return math.floor(res)
    


answer = mySqrt(8)
print('answer', answer)