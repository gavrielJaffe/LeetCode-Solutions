from typing import List
from math import log2 

def power_of_two(x:int):
    value =  log2(x)
    temp_value = value / 1
    value = int(value)
    print(f'value:{value},temp_value:{temp_value}')

    if temp_value == value:
        print('They are the same number')
        return value
    else:
        print('They are not the same number')
        return None

def main():
    ans = power_of_two(x=2**25)
    print('ans', ans)

if __name__ == "__main__":
    main()