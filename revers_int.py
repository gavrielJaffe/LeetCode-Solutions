
class Solution:
    def reverse(self, x: int) -> int:
        str_x  = str(x)
        print(str_x)

        # Test for zero in the end . 
        if (int(str_x[-1]) == 0):
            print('********************************************************')
            print("last possition is 0 ")
            print(len(str_x))
            print("befor" , str_x)
            str_x = str_x[:len(str_x)-1:]
            print("after", str_x)

        # Posstive number 
        if (x > 0):
            print("it a posstive number")
            
            return str_x[::-1]

        # Nagtive number 
        elif (x < 0):
            print("negative number  - ")
            str_x  = str(x)[1::]
            return str_x[::-1]

        return None 





sol = Solution()
ans = sol.reverse(1202)
print('ans', ans)
