#sample inputs
l = ['flow', 'flown', 'flowing', 'flock']
l_1 = ['flow', 'flower', 'flowing', 'flown']
l_2 = ['bread', 'cake', 'bowl', 'cup']

def longestCommonPrefix(words_list):
       
        prefix_container = set()
        length_of_words = []
        longest_common_prefix = ""

        for word in words_list:
            length_of_words.append(len(word))
        
        minimum_low = min(length_of_words)  #low - length of word
        
        for i in range(minimum_low):
            for word in words_list:
                prefix_container.add(word[i])
            
            if len(prefix_container) == 1:
                longest_common_prefix += prefix_container.pop()
            else:
                break
            
        return longest_common_prefix


print(longestCommonPrefix(l))
