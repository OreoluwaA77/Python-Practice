def get_missing_alphabets (sentence):
    new_string=""
    alpahabets="abcdefghijklmnopqrstuvwxyz"
    for i in range (len(alpahabets)):
        if alpahabets[i] in sentence:
            print("")
        elif alpahabets[i] not in sentence:
            new_string=new_string + alpahabets[i]
    print(new_string)


get_missing_alphabets("abs")
get_missing_alphabets("abcdefghijklmnopqrstuvwxyz")
