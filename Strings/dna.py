def dna_to_rna (code):
    new_string=""
    for i in range(len(code)):
        if code[i] == "A":
            new_string=new_string+"U"
        elif code[i] == "T":
            new_string=new_string+"A"
        elif code[i] == "G":
            new_string=new_string +"C"
        elif code [i] == "C":
            new_string=new_string+ "G"
        else:
            new_string=new_string+ code[i]
    print(new_string)

dna_to_rna("ATCGATCGTTACGAAT")