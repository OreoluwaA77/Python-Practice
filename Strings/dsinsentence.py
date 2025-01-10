def count_d (sentence):
    d=sentence.count("d")
    print(d)

count_d("Welcome to The Thanos World")


def m_to_w (sentence):

    for i in range(len(sentence)):
        if sentence[i]== "M":
            sentence=sentence.replace("M", "W")
    print(sentence)
    
m_to_w("MEET ME IN WARSAW")