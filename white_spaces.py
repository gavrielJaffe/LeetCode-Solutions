

def remove_spaces(text):
    temp = []
    for i in text:
        if i == " ":
            continue
        else: 
            print(f'{i}')
            temp.append(i)
    new_text = ''
    for i in temp:
        new_text=new_text+i
    return new_text



text = "we are song of Kings"
ans  = remove_spaces(text)
print('ans', ans)