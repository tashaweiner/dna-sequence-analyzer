#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group Project:
    Natasha Weiner 
    
"""


#Specify input
#A line beginning with a ">" is the header line for the next sequence -
# All lines after the header contain sequence data. - 
#There will be any number of sequences per file. - 
#Sequences may be split over many lines. - 
#Sequence data may be upper or lower case. - 
#Sequence data may contain white space, which should be ignored.
#Specify Output

import re

def reverse_complement(seq):
    #print(seq)
    mapping = str.maketrans('ATCG', 'TAGC')
    #print(seq.translate(mapping)[::-1])
    return seq.translate(mapping)[::-1]


#Main ORF function to account for ORFs 1-6
def ORF(FASTAEntries, startCodon, stopCodon, frame, getReverseComp):
    #print(FASTAEntries)
    #Maps 
    ORFDict = {}
    ORFARRAY = []

    #loop through all FASTA Entries 
    for x in FASTAEntries:
  
        sequence = FASTAEntries[x]
        
        #if ORF 4-6 reverse the sequence 
        if(getReverseComp is True):
            sequence = reverse_complement(sequence)
        #print(sequence)
        #print(sequence)
        #ORF 1 starts at 0 index  
        updatedORF = []
        
        for i in range(frame, len(sequence) - 2, 3):
            codon = sequence[i:i + 3]
            updatedORF.append(str(codon))
        #print(updatedORF)
        ORFDict[x] = updatedORF 
        ORFToPrint = [] 
        
        #now check for start codon and cut at stop codon
         #ORFARRAY = []
        hasStartCodon = False;
        for untilStop in range(0, len(ORFDict[x])):
            
            if hasStartCodon == True:
                ORFToPrint.append(str(ORFDict[x][untilStop]))
                if ORFDict[x][untilStop] == stopCodon[0] or ORFDict[x][untilStop] == stopCodon[1] or ORFDict[x][untilStop] == stopCodon[2]:
                    ORFToPrint.append(str(ORFDict[x][untilStop]))
                    break;
            else:            
                if ORFDict[x][untilStop] == startCodon:
                    hasStartCodon = True
                    ORFToPrint.append(str(ORFDict[x][untilStop]))
            
                    
        ORFARRAY.append(ORFToPrint)
        #print("here" + ORFToPrint)
    #print("ORFARRAY")
    #print(ORFARRAY)    
    return ORFARRAY
        #if temp[0] == startCodon:
    
#Format output        
def whatToPrint(FASTAEntries, readingFrame, readingFrameNumb, numberOfBases):
    if numberOfBases < 50:
        numberOfBases = 50
    count = 0
    for x in FASTAEntries:
        
        if not readingFrame[count] == []:
            if len(readingFrame[count] * 3) > numberOfBases:
                print(">" + x +  " | " + "FRAME = " + str(readingFrameNumb) + " POS = " + " LEN = "+ str(len(readingFrame[count])*3) +"\n" + ' '.join(readingFrame[count]))  
        count = count + 1

def main():

    #parse input  
    sequencesFile = open("sequence.fasta")
    content = sequencesFile.read()
    arrayline = []
    arrayline = content.split('>')
    count=0
    #map sequence name to sequence 
    FASTAEntries = {}

    for x in arrayline:
        tempArray = []
        temp = x.replace("\n", " ")
        arrayline[count] = temp
        count = count + 1
        tempArray = temp.split(None, 1)
        if  tempArray :
            FASTAEntries[tempArray[0]] = tempArray[1].replace(" ", "")
            
    #Start Codon 
    startCodon = "ATG"
    #Stop Codon
    stopCodon = ["TAG", "TAA", "TGA"]
    
    #prompt the user to enter number of bases to search for 
    numberOfBases = int(input("Please enter the minimum ORF to search for (the default is 50 bases so it must be over this): \n"))
    getReverseComp = False;
    #Frames 1 - 3
    readingFrame1 = ORF(FASTAEntries, startCodon, stopCodon,0, getReverseComp)
    #print(readingFrame1)
    whatToPrint(FASTAEntries, readingFrame1, 1, numberOfBases)
    
    readingFrame2 = ORF(FASTAEntries, startCodon, stopCodon,1, getReverseComp)    
    whatToPrint(FASTAEntries, readingFrame2, 2, numberOfBases)
    
    readingFrame3 = ORF(FASTAEntries, startCodon, stopCodon,2, getReverseComp)
    whatToPrint(FASTAEntries, readingFrame3, 3, numberOfBases)

    #make this marker true so we get reverse compliment in the function call
    getReverseComp = True;
    
    #Frames 4-6 
    readingFrame4 = ORF(FASTAEntries, startCodon, stopCodon,0, getReverseComp)
    whatToPrint(FASTAEntries, readingFrame4, 4, numberOfBases)

    readingFrame5 = ORF(FASTAEntries, startCodon, stopCodon,1, getReverseComp)
    whatToPrint(FASTAEntries, readingFrame5, 5, numberOfBases)

    readingFrame6 = ORF(FASTAEntries, startCodon, stopCodon,2, getReverseComp)
    whatToPrint(FASTAEntries, readingFrame6, 6, numberOfBases)

    
#    for line in content:
#        dna_sequence = ""
#        firstLine = ""
#        if line.startswith(">"):
#            firstLine = line
#            FASTAEntries[line] = ""
#            print(line.rstrip())
#        else:
#            dna_sequence += line.rstrip() 
#        FASTAEntries[firstLine]= dna_sequence

if __name__=="__main__":
    main()
    
