strs   = ["reflower","flow","flight"]
prefix = ['f', 'l']


for word in strs:
    print(word)
    for i in range(len(prefix)):
        print('i', prefix[i])
    for char in range(len(word)):
       print('word[char]', word[char])
       if ((word[char] == prefix[i]) and (char == i)):
          print(f"word[char] == prefix[i] {word[char]}={prefix[i]}")
          print(f"char == i {char}={i}")

# test if the letter form the prefix is in the start of the all of the letters in the strs.
