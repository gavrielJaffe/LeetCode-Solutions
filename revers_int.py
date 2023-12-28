
# class Solution:
#     def reverse(self, x: int) -> int:
#         str_x  = str(x)
#         print(str_x)

#         # Test for zero in the end . 
#         if (int(str_x[-1]) == 0):
#             print('********************************************************')
#             print("last possition is 0 ")
#             print(len(str_x))
#             print("befor" , str_x)
#             str_x = str_x[:len(str_x)-1:]
#             print("after", str_x)

#         # Posstive number 
#         if (x > 0):
#             print("it a posstive number")
            
#             return str_x[::-1]

#         # Nagtive number 
#         elif (x < 0):
#             print("negative number  - ")
#             str_x  = str(x)[1::]
#             return str_x[::-1]

#         return None 

# sol = Solution()
# ans = sol.reverse(1202)
# print('ans', ans)



# def bits_range(val):
#     if -2147483648 < val < 2147483647:
#         return val
#     else:
#         return 0

# class Solution:

#     def reverse_value(self, x: int) -> int:
#         str_x  = str(x)

#         # Test for zero in the end . 
#         if (int(str_x[-1]) == 0):
#             str_x = str_x[:len(str_x)-1:]
#             # print('remove the zero')
            
#         # Posstive number 
#         if (x > 0):
#             print("it a posstive number")
#             res  = str_x[::-1]
#             # print(res)
#             return int(res)

#         # Nagtive number 
#         elif (x < 0):
#             print("negative number  - ")
#             str_x  = str(x)[1::]
#             res =  str_x[::-1]
#             return int(res)  * -1 

#     def reverse(self, x: int):
#         val = sol.reverse_value(x)
#         new_val = bits_range(val)
#         return new_val
        
# sol = Solution()
# val = sol.reverse(120)
# print('val', val)





def bits_range(val):
    if val == None:
        return 0 

    if -2147483648 < val < 2147483647:
        return val
    else:
        return 0

class Solution:

    def reverse_value(self, x: int) -> int:
        str_x  = str(x)
        # Test for zero in the end . 
        if (int(str_x[-1]) == 0):
            str_x = str_x[:len(str_x)-1:]
            
        # Posstive number 
        if (x > 0):
            res  = str_x[::-1]
            return int(res)

        # Nagtive number 
        elif (x < 0):
            str_x  = str(x)[1::]
            res =  str_x[::-1]
            return int(res)  * -1 

    def reverse(self, x: int):
        if x == None:
            return 0 
        val = sol.reverse_value(x)
        new_val = bits_range(val)
        return new_val
        
sol = Solution()
val = sol.reverse(0)
print('val', val)
