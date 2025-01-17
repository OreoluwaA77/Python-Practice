def letter_count (letter, sentence):
    count=0
    for i in range(len(sentence)):
        if sentence[i]==letter:
            count=count+ 1
    return(count)

print(letter_count("c", "chamber of secrets"))
print(letter_count("a", "edabit"))
print(letter_count("b", "big fat bubble"))
