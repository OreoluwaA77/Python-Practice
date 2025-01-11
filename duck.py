def finding_bomb (sentence):
    return(sentence.find("bomb"))

def duck (sentence):
    sentence=sentence.lower()
    if finding_bomb(sentence)!= -1:
        return(True)
    else:
        return(False)

def main(sentence):
    if duck(sentence)==True:
        return("DUCK!!!")
    else:
        return("There is no bomb, relax!")
    
print(main("There is a BOMB."))