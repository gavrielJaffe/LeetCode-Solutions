def remove(lst):
    parenthesis = { "(":")" , ")":"(" , "[" : "]" , "]":"[" ,"{": "}", "}": "{" }
    print('lst', lst)
    print('********************************************************')
    if (len(lst) == 0):
        return True

    # Remove key.
    key = lst.pop(0)

    try:
        # Remove value,by the index
        value = parenthesis[key]
        index = lst.index(value)
        lst.pop(index)
        print(f'You entered {index}, which is not a in list number.')
    except ValueError as ve:
        print(f've',{ve})
        return False

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
            elif lst == False:
                break
        return False
    

sol = Solution()
test_string = '([)]' # res need to be false
res = sol.isValid(test_string)
print('')

print('res', res)