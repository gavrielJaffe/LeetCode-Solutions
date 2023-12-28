from typing import List
# There is a two list of words , you need to find the word in the list. 

a = ["Apple", "Banana", "Orange", "Grape", "Cherry"]
b = ["Banana", "Grape","Kiwi","Cherry","Mango"] # Cherry    


def find_words(a:List,b:List):
    words_in_list = []
    for i in range(len(a)):
        print('test for the word:', a[i])
        for j in range(len(b)):
            print('test on:', b[j])
            if a[i]==b[j]:
                print(f'{a[i]}={b[j]}')
                words_in_list.append(a[i])
                b.pop(j)
                break
    return words_in_list 

words_in_list = find_words(a,b)
print('words_in_list', words_in_list)



