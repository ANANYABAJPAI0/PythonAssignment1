import string

def remove_punctuation(input_string):
    
    punctuation_chars = string.punctuation
    
    
    translator = str.maketrans('', '', punctuation_chars)
    
   
    cleaned_string = input_string.translate(translator)
    
    return cleaned_string


input_string = "Hello, World! This is a sample string with some punctuation."
cleaned_string = remove_punctuation(input_string)

print("String without punctuation:", cleaned_string)
