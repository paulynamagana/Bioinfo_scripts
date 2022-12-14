# define a function for transcription
def DNAreverse(seq):

    reverse = seq[::-1]# convert string into list

    print("Reverse DNA; ", end="")
    print(reverse, end="")


if __name__ == "__main__":

    y = input("Input DNA sequence: ")
    DNAreverse(y)
