def title_case(s):
    
    words = s.split()
    
    
    title_case_words = [word.capitalize() for word in words]
    
    
    return ' '.join(title_case_words)


input_string = "hello world how are you"
title_cased_string = title_case(input_string)

print("Title cased string:", title_cased_string)
