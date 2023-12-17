
missing_int = [1,2,3,9,5,6,7,8]

def find_missing_int(lst):
    sum_in_list = sum(lst)
    non_Missing_Sum = 0
    for i in range(1,len(lst)+2):
        non_Missing_Sum = non_Missing_Sum + i 

    print(f'non_Missing_Sum',non_Missing_Sum)
    print(f'sum_in_list',sum_in_list)
    return non_Missing_Sum - sum_in_list

print(find_missing_int(missing_int))