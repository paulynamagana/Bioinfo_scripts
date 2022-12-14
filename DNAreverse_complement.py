
# define a function for transcription
def DNAreverse_complement(seq):
    seq = seq.upper()
    reverse = seq[::-1]  # convert string into list

    # convert string into list
    l = list(reverse)

    for i in range(len(reverse)):

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

    print("Reverse complement DNA; ", end="")
    for char in l:
        print(char, end="")


if __name__ == "__main__":

    y = input("Input DNA sequence: ")
    DNAreverse_complement(y)
