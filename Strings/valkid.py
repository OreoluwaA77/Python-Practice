def valid (password):
    for i in range (len(password)):
        if not password.isalnum():
            print("invalid password")
        elif password.isspace():
            print("invalid password")
        elif password(len)