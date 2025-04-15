#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:37:32 2022
@author: Natasha Weiner 
"""

import re
import os

#asks the user for a file containing a FASTA nucleotide sequence

#This will print to the screen the numbers of A, G, C and T nucleotides, and any unknowns (N’s).
def DNAComposition(seqContents):
    seqList = list(seqContents)
    ACount = 0
    GCount = 0
    CCount = 0
    TCount = 0
    UnknownCount = 0
    for nuc in seqList:
        if nuc == 'A':
            ACount+= 1
        elif nuc == 'G':
            GCount+=1
        elif nuc == 'C':
            CCount+=1
        elif nuc == 'T':
            TCount+=1
        else:
            UnknownCount+=1
        
    print("Nucleotide Count: \nA: " + str(ACount) + "\nG: " + str(GCount) + "\nC: " + str(CCount) + "\nT: " + str(TCount) + "\nUnkown: " + str(UnknownCount))

#Prints to the screen the percentage of AT in the sequence.
def ATinSeq(seq, seqLength):
    #get a list of all matches
    
    ATMatches = re.findall("AT", seq)
    numbMatches = len(ATMatches)
    percentAT = (numbMatches*2/seqLength) * 100

    print("\'AT\' matches take up " + str(round(percentAT,2)) + "% " + "of the given sequence\n") 
#Prints to the screen the percentage of GC in the sequence.
def GCinSeq(seq, seqLength):
     GCMatches = re.findall("GC", seq)
     numbMatches = len(GCMatches)
     percentGC = (numbMatches*2/seqLength) * 100
     print("\'GC\' matches take up " + str(round(percentGC,2)) + "% " + "of the given sequence\n")
     
#Get complement of DNA 
def complimentFunc(seq):
    DNAComplimentList = list(seq)
    for i in range(len(seq)):
        if DNAComplimentList[i] == 'C':
            DNAComplimentList[i] = 'G'
        elif DNAComplimentList[i] == 'G':
            DNAComplimentList[i] = 'C'
        elif DNAComplimentList[i] == 'A':
            DNAComplimentList[i] = 'T'
        elif DNAComplimentList[i] == 'T':
            DNAComplimentList[i] = 'A'
    DNACompliment = ''.join(DNAComplimentList)
    return DNACompliment

#Prints to the screen the compliment of the DNA sequence.
def DNACompliment(seq):
    DNACompliment = complimentFunc(seq)
    print("The Compliment of the DNA String: " + seq + "\n" + "is: " + DNACompliment)
    return DNACompliment
            
#Prints to the screen the reverse compliment.
def DNAReverseCompliment(seq):
    DNACompliment = complimentFunc(seq)
    DNARevComp = reversed(DNACompliment)
    print("The Compliment of the DNA String: " + seq + "\n" + "is: " + ''.join(DNARevComp))  
    
#Your program should then find the translation (protein sequence) of the 
#nucleotide sequence in that frame. Print the translation to the screen.
def DNATranslation(seq, frame, gencode):

    proteinSeq = ""
    
    #reading frame will determine where you start 
    for x in range(frame-1, len(seq) - 2, 3):
        codon = seq[x:x + 3]
        proteinSeq = proteinSeq + gencode[codon]
    print("DNA Translation of protein sequence in frame: " + str(frame) + "\nseq: " + proteinSeq + "\n")
    
#convert the GenBank formatted sequence into FASTA format.
#Write the FASTA formatted sequence to a file, name of which should include 
#the accession number (i.e. NM_001250672.txt, where NM_001250672 is the accession number).
def ConvertToFasta(GenBankContent):
    
    for line in GenBankContent:
        idInfo= ""
        descInfo = ""
        sequence = ""
        #Parse Accession number
        if line.startswith("ACCESSION"):
            idInfoArray = re.split("ACCESSION   ",line)
            idInfo= str(idInfoArray[1])
            #Create a new file w accession
            f = open(idInfo + ".txt", "w")
            f.write(">" + idInfo)
            print("Accession: " + idInfo)
             
        #parse sequence (SQ)
        sequence = ""
        if line.startswith("ORIGIN"):
            tempLine = GenBankContent.readline()
            tempArray = []
            while tempLine.startswith("     "):
                seqArray = re.split("    ",tempLine)
                seqq= str(seqArray[1])
                #remove all spaces in sequence and numbers
                seqInfo = re.sub("\d", "", seqq)
                temp = seqInfo.replace(" ", "")
                sequence = sequence + str(temp)
                #add all sequences together
                tempLine = GenBankContent.readline()
            f.write(sequence)
            print("Sequence: " + sequence) 
            
#return the positions in the sequence where the enzyme cuts.
def EnzymeCuts(seq, restrictionEnzyme):
    #open restriction enzyme file and parse out the enzymes and their cuts 
    restEnzymeDict = {}
    restEnzymeFile = open("RestrictionEnzymes.txt")
    for line in restEnzymeFile.readlines():
        tempArr = re.split(',', line)
        restEnzymeDict[tempArr[0]] = tempArr[1]
    
    # find cut site     
    all_cuts = []
    cutSite = restEnzymeDict[restrictionEnzyme]
    #find cut position 
    cutPosition = re.search('\'', cutSite)
    #remove '
    cutSite = re.sub("\'","", cutSite)
    #translate to regex 
    cutSite = re.sub("N","[ATGC]", cutSite)
    cutSite = re.sub("R","[AG]", cutSite)
    cutSite = re.sub("Y","[CT]", cutSite)
    cutSite = re.sub("S","[CG]", cutSite)
    cutSite = re.sub("M","[AC]", cutSite)
    cutSite = re.sub("W","[AT]", cutSite)
    cutSite = re.sub("K","[GT]", cutSite)
    temp = repr(cutSite)[1:-1]
    temp = temp.strip('\\n')
    for match in re.finditer(temp, seq): 
        toAppend = str(match.start() + cutPosition.start())
        all_cuts.append(toAppend)
        
    print("The Restriction Enzyme entered " + restrictionEnzyme + " will cut at postitions: " + ', '.join(all_cuts))

#compute the background codon frequencies.
#background_frq(codon) = 100 * N(codon)/ Total_codons
def CodonFrequency(genomeSeq):
    codons = {'ATA': 0, 'ATC': 0, 'ATT': 0, 'ATG': 0,
               'ACA': 0, 'ACC': 0, 'ACG': 0, 'ACT': 0,
               'AAC': 0, 'AAT': 0, 'AAA': 0, 'AAG': 0,
               'AGC': 0, 'AGT': 0, 'AGA': 0, 'AGG': 0,
               'CTA': 0, 'CTC': 0, 'CTG': 0, 'CTT': 0,
               'CCA': 0, 'CCC': 0, 'CCG': 0, 'CCT': 0,
               'CAC': 0, 'CAT': 0, 'CAA': 0, 'CAG': 0,
               'CGA': 0, 'CGC': 0, 'CGG': 0, 'CGT': 0,
               'GTA': 0, 'GTC': 0, 'GTG': 0, 'GTT': 0,
               'GCA': 0, 'GCC': 0, 'GCG': 0, 'GCT': 0,
               'GAC': 0, 'GAT': 0, 'GAA': 0, 'GAG': 0,
               'GGA': 0, 'GGC': 0, 'GGG': 0, 'GGT': 0,
               'TCA': 0, 'TCC': 0, 'TCG': 0, 'TCT': 0,
               'TTC': 0, 'TTT': 0, 'TTA': 0, 'TTG': 0,
               'TAC': 0, 'TAT': 0, 'TAA': 0, 'TAG': 0,
               'TGC': 0, 'TGT': 0, 'TGA': 0, 'TGG': 0}
    
    #Count total codons across all reading frames 
    total = 0
    for x in range(len(genomeSeq) - 2):
        codon = genomeSeq[x:x + 3]
        codons[codon] = codons[codon] + 1
        total = total+1
    
    for x in codons:
        codons[x] = 100*codons[x]/ total
        print("The background frequency of codon " + str(x) + " is: " + str(codons[x]))
        
        
        
def main():

    gencode = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
               'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
               'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
               'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
               'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
               'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
               'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
               'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
               'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
               'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
               'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
               'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
               'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
               'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
               'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
               'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}
    
    fastaNucSeq = input("Please enter the filename of a FASTA nucleotide sequence you wish to work with: ")
    while not os.path.isfile(fastaNucSeq):
        print("File not found, please try again.")
        fastaNucSeq = input("Please enter the filename of a FASTA nucleotide sequence you wish to work with:  ")
    seqFile = open(fastaNucSeq)
    firstLine = seqFile.readline()
    seqContents = seqFile.readlines()
    seqFile.close()
    seq = ""
    for x in seqContents:
        seq = seq + x.replace("\n", "")
    seqLength = len(seq)
    
    #Input Validation: Check to see that the file name entered by the user exists
    #AND that the sequence is in FASTA format *******
    accNumb = re.search("([^\>\s]+)", firstLine)
    if firstLine.startswith('>')== False or (seq == None):
        print("This is not a FASTA Nucleotide Sequence!")
    
    #Question 1     
    menuSelection = str(input("Please Type in your selection from the menu(A,B,C,D,E): \n A. Calculate DNA composition: \n B.Calculate AT content \n C. Calculate AT content: \n D. Compliments \n E. Reverse Compliments ? \n"))
    
    if(menuSelection == 'A'):
        DNAComposition(seq)
    elif(menuSelection == 'B'):
        ATinSeq(seq, seqLength)
    elif(menuSelection == 'C'):
        GCinSeq(seq,seqLength)
    elif(menuSelection == 'D'):
        DNACompliment(seq)
    elif(menuSelection == 'E'):
        DNAReverseCompliment(seq)
        
    #Question 2 
    #prompt the user to select a frame (number 1 through 6). 
    framePick = int(input("Please select a frame (number 1 through 6): "))
    DNATranslation(seq, framePick, gencode)
    
    #Question 3 
    # asks the user for a sequence in GenBank format
    GenBankFile = str(input("Please enter the filename of a sequence in GenBank format: "))
    while not os.path.isfile(GenBankFile):
        print("File not found, please try again.")
        GenBankFile = input("Please enter the filename of a sequence in GenBank format: ")
    namedFile = open(GenBankFile,'r')
    ConvertToFasta(namedFile)
    namedFile.close()
    
    #Question 4 
    #Write a program that asks the user for a file containing a nucleotide 
    #equence AND the name of a restriction enzyme.
    restrictionEnzyme = str(input("Please enter the name of a restriction enzyme: "))
    EnzymeCuts(seq, restrictionEnzyme)
    
    #Question 5 
    
    seqFile = open("genome.txt")
    #get seq from file 
    firstLine = seqFile.readline()
    #account for empty space 
    seqFile.readline()
    seqContents = seqFile.readlines()
    genomeSeq = ""
    
    #put all in one string 
    for x in seqContents:
        genomeSeq = genomeSeq + x.replace("\n", "")
    seqFile.close()
    
    #compute background codon frequencies 
    CodonFrequency(genomeSeq)
    
if __name__=="__main__":
    main()
    

# Prompt user to select from the following menu 

