def is_anagram(sentence,word):
    total_sentence=0
    for i in range(len(sentence)):
            total_sentence=total_sentence+(ord(sentence[i]))

    total_word=0
    for i in range(len(word)):
            total_word=total_word+(ord(word[i]))

    if total_sentence==total_word:
        print("True")
    else:
          print("False")

is_anagram("sentence", "sentence")
is_anagram("sentence","word")
is_anagram("i love school", "school love i")