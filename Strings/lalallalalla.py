def count_syllables (sentence):
    count=0
    for i in range(len(sentence)):
        if sentence[i] in "aeiou":
         count=count+ 1

    print(count)
count_syllables("Hehehehehe")