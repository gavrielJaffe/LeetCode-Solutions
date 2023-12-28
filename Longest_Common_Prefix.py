from typing import List
""""
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""

"""

# strs = ["flower","flowa","flight"]
# strs = ["dog","racecar","car"]
strs = ["cir","car"]


def find_prefix_first(strs,letter,postion_letter):
    common_prefix = ''
    counter = 0
    postion_tw = postion_letter
    test_word = letter

    # print(test_word,postion_tw)
    

    for word in strs:
        for j in range(len(word)):
            if test_word == word[j] and( postion_tw == j):
                print('there is a match in the words', test_word , word[j])
                counter  +=1  

    # Test if the letter is in all of the other words
    if counter == len(strs):
        common_prefix = common_prefix+test_word

    return common_prefix

def containes(lst,letter,postion_letter):
    print(lst,letter,postion_letter)
    text = find_prefix_first(lst,letter,postion_letter)
    return text

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_text = ""
        for i in range(len(strs[0])):
            postion_letter = i
            letter = strs[0][i]
            # print(postion_letter,letter)
            text = containes(strs[1:],letter,postion_letter)
            # print('text = anser from the containes', text)
            if text == '':
                break
            new_text = new_text + text
        # print('new text:',new_text)
        return new_text
    
sol = Solution()
ans=sol.longestCommonPrefix(strs)
print('ans:', ans)

