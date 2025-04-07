def password_validator (filter):
    count=0
    okay=True
    if len(filter)<7:
            okay=False        
    if " " in filter:
           okay=False
    for i in range (len(filter)):  
        if filter[i] in "0123456789":
            count=count+1
            if count>=1:
                 okay=True
    if okay==True:
        print("valid password")
    elif okay==False:
        print("invalid password")

password_validator("oreisniche123")
password_validator("maya is great")
