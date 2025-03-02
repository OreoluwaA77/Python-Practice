def is_central (sentence):
        
    count=len(sentence)
    print(count)
    mid=count//2
    if sentence[mid].isspace():
        print(False)
    else:
        print(True)



is_central(" q")