# define a function for transcription
def DNAcomplement(seq):
    seq = seq.upper() #convert to uppercase
    # convert string into list
    l = list(seq)


    for i in range(len(seq)):

        if (l[i] == "T"):
            l[i] = "A"

        elif (l[i] == "G"):
            l[i] = "C"

        elif (l[i] == "C"):
            l[i] = "G"

        elif (l[i] == "A"):
            l[i] = "T"

        else:
            print("Invalid")

    print("Complement DNA; ", end="")
    for char in l:
        print(char, end="")


if __name__ == "__main__":

    y = input("Input DNA sequence: ")
    DNAcomplement(y)
