# from typing import List

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 1 :
#             return [[1]]

#         if numRows == 2 :
#             return [[1],[1,1]]


#         return new_lst

# sol = Solution()
# sol.generate(3)


def extended_list(lst):
    new_list = []
    for index, element in enumerate((lst)):
        print(index,element)
    # MISSION : FOR THE FIRST INDEX TO THE NEW LIST 
        if (index == 0):
            new_list.append(element)
    # MISSION : SUM UP ALL IN THE BETWEEN 
        elif ((index != 0 ) ):
            new_list.append(element+lst[index-1])

    # MISSION : FOR THE LAST INDEX TO THE NEW LIST 
        if (index == (len(lst)-1)):
            new_list.append(element)
    return new_list

new_list = extended_list([1,3,3,1])
print('new_list', new_list)
