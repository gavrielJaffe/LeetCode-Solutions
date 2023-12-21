
class Solution:
    def reverse(self, x: int) -> int:
        if (x > 0):
            operators = "+"
        elif (x < 0):
            operators = "-"
            
        # Mission if there is "-" operator in the start remvoe it . 
        print('operators', operators)

        str_x = (str(x))[-1::]
        str_x = str(x)
        print(str_x)

        
        # If x has a zero in the end , remvoe the zero from it. 
        if (int(str_x[-1]) == 0):
            print("we have zero in the start ")
            str_x = str(x)[:-1:]


        return str_x[::-1] # Answer should be in int,not str. 





sol = Solution()
ans = sol.reverse(-123)
print('ans', ans)
