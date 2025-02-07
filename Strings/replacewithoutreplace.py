sentence="Hello World"
new_string=""
for i in range(len(sentence)):
    if sentence[i] in "aeiou":
        new_string=new_string+"?"
    else:
        new_string=new_string+sentence[i]
print(new_string)
