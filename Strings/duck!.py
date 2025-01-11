def finding_bomb (sentence):
    return(sentence.find("bomb","Bomb","BOMB"))

def duck (sentence):
    if finding_bomb(sentence)!= -1:
        return(True)
    else:
        return(False)

def main(sentence):
    if duck(sentence)==True:
        return("DUCK!!!")
    else:
        return("There is no bomb, relax!")
    
print(main("There is a bomb."))