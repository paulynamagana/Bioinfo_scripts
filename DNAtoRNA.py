# define a function for transcription
def DNAtoRNA(seq):

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
            l[i] = "U"

        else:
            print("Invalid")

    print("Translated DNA; ", end="")
    for char in l:
        print(char, end="")


if __name__ == "__main__":

    y = input("Input DNA sequence: ")
    DNAtoRNA(y)
