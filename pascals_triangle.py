from typing import List

def extended_list(lst):
    new_list = []
    for index, element in enumerate((lst)):
        if (index == 0):
            new_list.append(element)
        elif ((index != 0 ) ):
            new_list.append(element+lst[index-1])
        if (index == (len(lst)-1)):
            new_list.append(element)
    return new_list

class Solution:
    def extended_list(lst):
        new_list = []
        for index, element in enumerate((lst)):
            if (index == 0):
                new_list.append(element)
            elif ((index != 0 ) ):
                new_list.append(element+lst[index-1])
            if (index == (len(lst)-1)):
                new_list.append(element)
        return new_list

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :
            return [[1]]

        if numRows == 2 :
            return [[1],[1,1]]
        
        ans = [[1],[1,1]]
        for i in range(2,numRows):
            new_list = extended_list(ans[i-1])
            ans.append(new_list)
        return ans

sol = Solution()
result = sol.generate(5)
print('result',result)















# def extended_list(lst):
#     new_list = []
#     for index, element in enumerate((lst)):
#         print(index,element)
#     # MISSION : FOR THE FIRST INDEX TO THE NEW LIST 
#         if (index == 0):
#             new_list.append(element)
#     # MISSION : SUM UP ALL IN THE BETWEEN 
#         elif ((index != 0 ) ):
#             new_list.append(element+lst[index-1])

#     # MISSION : FOR THE LAST INDEX TO THE NEW LIST 
#         if (index == (len(lst)-1)):
#             new_list.append(element)
#     return new_list

# new_list = extended_list([1,1])
# print('new_list', new_list)
