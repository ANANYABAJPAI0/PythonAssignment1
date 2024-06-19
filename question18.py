from collections import Counter

def are_anagrams(str1, str2):
    
    
    
    if len(str1) != len(str2):
        return False
    
    
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)
    
    
    if count_str1 == count_str2:
        return True
    else:
        return False

string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
