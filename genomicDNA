# Natasha Weiner 

# #Print out contents to screen
# print(file1Contents)

#
#     def __init__(self):
#         pass


# Open the File
genomicDNA = open("genomic_dna.txt")
sequences = open("sequences.txt")
accessionNumbers = open("accessionNumbers.txt")

# Read in file contents
genomicDNAContents = genomicDNA.read()
sequencesContents = sequences.read()
accessionNumbersContents = accessionNumbers.read()

Attached is a file called genomic_dna.txt. It contains a DNA sequence that is comprised of two
# exons and an intron. The first exon runs from the start of the sequence to the 63 bp, and the
# second exon runs from the 91 bp to the end of the sequence. Write a program that will print out
# to files the coding and non-coding regions of the sequence
DNAtoList = list(genomicDNAContents)
exon1 = "";
intron = "";
exon2 = "";
DNAlen = len(genomicDNAContents)
for i in range(DNAlen):
    if (i < 62):
        exon1 = exon1 + DNAtoList[i]
    elif (i >= 62 and i < 90):
        intron = intron + DNAtoList[i]
    elif (i >= 90):
        exon2 = exon2 + DNAtoList[i]

exon1 = exon1 + "\n"
with open('coding.txt', 'a') as f:
    f.write(exon1)
    f.write(exon2)
with open('non_coding.txt', 'a') as f:
    f.write(intron)

exontotal = (len(exon1) + len(exon2))
codingPercentage = (100 * float(exontotal) / float(DNAlen))
noncodingPercentage = (100 * float(len(intron)) / float(DNAlen))
print("Coding: " + str(codingPercentage) + "  NonCoding: " + str(noncodingPercentage))

 Attached is a file called sequences.txt, it contains 3 sequences (one sequence per line). Also
# attached is a file called AccessionNumbers.txt. Write a program that reads in those files and
# produces 3 separate FATSA files. Each accession number in the AccessionNumbers.txt file
# corresponds to a sequence in the sequences.txt file.
seqList = sequencesContents.splitlines()
accNumbList = accessionNumbersContents.splitlines()
for i in range(len(seqList)):
    text = ">" + accNumbList[i] + "\n" + seqList[i]
    text = filter(str.isalnum, text)
    f = open(accNumbList[i] + ".txt", "w+")
    f.write(text.upper())
    f.close

# Write a program that checks to see if two DNA sequences given as input by the user are reverse
# compliments of one another.
DNA1 = raw_input("Please enter a DNA String")
DNA2 = raw_input("Please enter another DNA String")
DNA1toList = list(DNA1)

for i in range(len(DNA1)):
    if DNA1toList[i] == 'c':
        DNA1toList[i] = 'g'
    elif DNA1toList[i] == 'g':
        DNA1toList[i] = 'c'
    elif DNA1toList[i] == 'a':
        DNA1toList[i] = 't'
    elif DNA1toList[i] == 't':
        DNA1toList[i] = 'a'
DNA1 = ''.join(reversed(DNA1toList))
if DNA1 == DNA2:
    print("The entered strings of DNA are reverse compliments " + DNA1 + " " + DNA2)
else:
    print("The entered strings of DNA are NOT reverse compliments" + DNA1 + " " + DNA2)
# Q5
# Write a program to read a file, and then print its lines in reverse order, the last line first. You can
# use the sequence.txt file (attached) to test your program with.
seqList.reverse()

for i in range(len(seqList)):
    print(seqList[i])

# Write a program that will predict the size of a population of organisms. The program should ask
# for the starting number of organisms, their average daily population increase (as a percentage),
# and the number of days they will multiply. For example, a population might begin with two
# organisms, have an average daily increase of 50 percent, and will be allowed to multiply for
# seven days. The program should use a for loop to display the size of the population for each day.
numbOfOrganisms = 0
averageIncrease = -1
numbOfDaysMul = 0
while numbOfOrganisms <= 1:
    numbOfOrganisms = int(input("Enter the number of organisms: "))
    if (numbOfOrganisms < 2):
        print("Invalid input. Please enter a number equal to or above 2")
while averageIncrease < 0:
    averageIncrease = float(input("Enter the average daily population increase by %: "))
    if averageIncrease < 0:
        print("Invalid input. Please enter a non negative value")
while numbOfDaysMul <= 1:
    numbOfDaysMul = int(input("Enter the number of days they will multiply: "))
    if numbOfDaysMul <= 1:
        print("Invalid input. Please enter a value greater than 1")

print("Day            Organisms")
print("___________________________")
for i in range(int(numbOfDaysMul)):
    print(str(i + 1) + "                    " + str(float(numbOfOrganisms)))
    numbOfOrganisms = float(numbOfOrganisms) * ((float(averageIncrease) * .01) + 1)

# Write a program that takes user entered lines from the keyboard and stores them in an array.
# When the user enters "quit", the program prints out all the lines sorted

inputQuit = True
listOfInputs = []
while inputQuit == True:
    input = raw_input("Enter a string")
    if input == "quit":
        inputQuit = False
    else:
        listOfInputs.append(input)

newListofInputs = list(listOfInputs)
# listOfInputs.sort()
# print(listOfInputs)

# Now modify the program so it tells you how many lines have been entered, and then prints out
# only lines 2, 3, and 4.
numOfLinesEntered = len(newListofInputs)

print("Lines 2, 3 and 4 entered: " + newListofInputs[1] + " " + newListofInputs[2] + " " + newListofInputs[3] + " ")

# Ask the user for a list of sequence lengths, separated by whitespace (Example: 100 123 45
# Store the sequence lengths as one string in a variable, then:
# a) Split that string and create an array from it (each number being an element of the array)
# b) Use a for loop to get the sum of all sequence lengths.
# c) Print the average.

seqLengths = raw_input("Enter a list of sequence lengths, seperated by whitespace")
listOfSeqLength = seqLengths.split()
print(listOfSeqLength)
total = 0
for i in range(len(listOfSeqLength)):
    total = total + int(listOfSeqLength[i])

print("The average of the sequences entered is " + str(float(total) / float(len(listOfSeqLength))))

# Write a program that asks the user to enter the number of calories and fat grams in a food item.
# The program should display the percentage of the calories that come from fat. One gram of fat
# has 9 calories, therefore:
totalCal = raw_input("Enter the number of calories in a food item: ")
fatgrams = raw_input("Enter the fat grams in a food item: ")
calFromFat = int(fatgrams) * 9
print(calFromFat)
percentage = (100 * float(calFromFat) / float(totalCal))
print("The percentage of the calories that come from fat are " + str(percentage) + "%")

if (percentage < 30.0):
    print("Also! This food item is low fat!")

# close files
genomicDNA.close()
sequences.close()
accessionNumbers.close()
