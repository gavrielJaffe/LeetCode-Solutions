
class Solution:
    def isValid(self, s: str) -> bool:
        
        # All odd numberes of lst length would return False. 
        if len(s) % 2 != 0: 
            return False    

        open_pretheses = {
        "{":"}" ,
        "[":"]" , 
        "(":")" ,
        }
        close_pretheses = {
        "}":"{" ,
        "]":"[" , 
        ")":"(" ,
        }

        stack = []
        for c in s:
            if c in open_pretheses:
                stack.append(c)
                print(f'{c} in pretheres stack{stack}')
            if c not in open_pretheses:
                try:
                    element = stack.pop()
                except IndexError as error:
                    print("index error, Start with closing parentheses could never be a valid")
                    return False
                opset_c  = close_pretheses[c]
                if not element == opset_c:
                    return False
                
        if len(stack) == 0:
            return True

sol = Solution()
test_string = "[]"
res = sol.isValid(test_string)
print('res', res)