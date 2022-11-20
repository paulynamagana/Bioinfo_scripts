class countDNA(str):

    def __new__(self, s):
        #
        return str.__new__(self, s.upper())

    # function to coun bases and total length
    def count_bases(self):
        countA = self.count("A")
        countC = self.count("C")
        countT = self.count("T")
        countG = self.count("G")
        total = len(self)
        print("DNA length : {}" .format(total))
        print("Total of A, C, G, T: {} {} {} {}".format(
            countA, countC, countG, countT))


dna = input("DNA sequence: ")
x = countDNA(dna)
x.count_bases()
