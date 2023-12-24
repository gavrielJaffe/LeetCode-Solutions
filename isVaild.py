def remove(lst):
    prehntsis = { "(":")" , ")":"(" , "[" : "]" , "]":"[" ,"{": "}", "}": "{" }
    print('lst', lst)
    print('********************************************************')
    if (len(lst) == 0):
        return True

    # Remove key.
    key = lst.pop(0)


    # Remove value,by the index
    value = prehntsis[key]
    index = lst.index(value)
    lst.pop(index)
    print(f'You entered {index}, which is not a in list number.')

    # sent the new list back 
    return lst


class Solution:
    def isValid(self, s: str) -> bool:
        print(s)
        lst = []

        # Build the lst from s
        for i in range(len(s)):
            lst.append(s[i])
        
        # All odd numberes of lst length would return False. 
        if len(lst) % 2 != 0: 
            print("we have odd numbers of lst")
            return False    
        
        print(int(len(s)/2)+1)
        # run the remove function,Get the new list.
        for i in range(len(s)):
            lst = remove(lst)
            if lst == True:
                return True
        return False
    

sol = Solution()
test_string = '(]'
res = sol.isValid(test_string)
print('')

print('res', res)