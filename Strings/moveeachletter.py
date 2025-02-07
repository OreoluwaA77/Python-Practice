sentence="I want peace"
new_string=""
for i in range (len(sentence)):
    new_sentence_digit=(ord(sentence[i])+1)
    new_sentence_word=(chr(new_sentence_digit))
    new_string=new_string+new_sentence_word
print(new_string)

