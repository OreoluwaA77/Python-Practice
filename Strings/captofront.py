def cap_to_front (sentence):
    new_string_caps=""
    new_string_lower=""
    for i in range (len(sentence)):
        letters=sentence[i]
        if letters.isupper():
            new_string_caps=new_string_caps+letters        
        elif letters.islower():
            new_string_lower=new_string_lower+letters
    new_string=new_string_caps+new_string_lower
    print(new_string)

cap_to_front("heLLo")
