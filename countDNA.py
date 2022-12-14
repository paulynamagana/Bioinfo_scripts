def countDNA(str):

    str = str.upper()
    countA = str.count("A")
    countC = str.count("C")
    countT = str.count("T")
    countG = str.count("G")
    total = len(str)
    print("DNA length : {}" .format(total))
    print("Total of A, C, G, T: {} {} {} {}".format(
        countA, countC, countG, countT))


if __name__ == "__main__":

    y = input("Input DNA sequence: ")
    countDNA(y)
