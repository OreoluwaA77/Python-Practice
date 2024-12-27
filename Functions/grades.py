def grade_obtained(mark):
    if 90<mark<100:
        return ("A")
    elif 70<mark<89:
        return ("B")
    elif 50<mark<69:
        return("C")
    elif 30<mark<49:
        return("D")
    elif mark>100:
        return("Invalid")
    elif mark<0:
        return("Invalid")
    else:
        return("FAIL")
    
print(grade_obtained(87))
print(grade_obtained(54))
print(grade_obtained(4))
print(grade_obtained(91))
print(grade_obtained(110))