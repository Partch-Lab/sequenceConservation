 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:45:30 2019


Roshan Ahmed (roahmed)
Kourosh Kouhmareh (kkouhmar)



Program takes in a csv file, converts it to fasta format then aligns using clutal omega. 
The aligned sequence file is passed into the sequence conservation class which assigns an average 
score for each column of the amino acids being compared. The sequences are compared to the first 
sequence in the file. The program writes the final list of all scores to an outfile. 
"""

from subprocess import run 
import pandas as pd
import sys

class sequenceConservation:
    
    """
    Class has list of amino acids sublists. Parses through each column for all 
    sequences and assigns a score based on if amino acid is the same, or in the same list. 
    These scores are summed and this returns an overall conservation score for each index in the 
    sequence. 
    """
    
    aliphaticAA = ['A', 'I', 'L', 'M', 'V']
    aromaticAA = ['F', 'W', 'Y']
    polarAA = ['N', 'C', 'Q', 'S', 'T']
    acidicAA = ['D', 'E']
    basicAA = ['R', 'H', 'K']
    smallAA = ['G']
    kinkyAA = ['P']
    allAA = [aliphaticAA, aromaticAA, polarAA, acidicAA, basicAA, smallAA, kinkyAA]

    def __init__(self):
        self.score = []
        self.compare_sequence = ""
        
        
    def fastaConverter():
        """
        Method converts csv files into Fasta format.
        """
        
        a = pd.read_csv() #name of csv file we are reading
        with open("fastaFile.txt", "w") as textFile: #writing file in fasta format 
            for index, row in a.iterrows():
                textFile.write(">" + (row['Species']) + "\n")
                textFile.write(row['Sequence'] + "\n\n") 

        
    def conservationScore(self, myReader):
        """
        Calculates a conservation score for each index of sequence. 
        Returns list of all conservation scores.
        """
    
        for header, sequence in myReader.readFasta():
            compare_sequence = sequence #first sequence listed in CSV file 
            compareSeq = compare_sequence
            break
                
        for index in range(0, len(compareSeq)):
            compareFlag = True
            count = 0 
            columnScore = 0
            
           
            for header, sequence in myReader.readFasta():
                if compareFlag:
                    compareFlag = False
                    continue
                else: 
                    count = count + 1 
                    char1 = str(compareSeq[index])
                    char2 = str(sequence[index])
                                        
                    if (char1 == char2) and (char1 is not "-"):
                        columnScore += 1
                    elif (str(char1) == "-") or (str(char2) == "-"):
                        pass
                    else: 
                        if (sequenceConservation.checkLists(char1, char2)):
                            columnScore += 0.5
                        else: 
                            pass   
                        
            finalScore = (columnScore/count)
            if char1 == "-":
                pass
            else:
                self.score.append(float(finalScore))
                
        return(self.score)
        
        
    def checkLists(char1, char2):
        """
        Checks to see if amino acids are in the same list.
        """
        
        for subList in sequenceConservation.allAA:
            if char1 and char2 in subList:
                return True 
            else:
                return False
        
class FastAreader:
    ''' 
    Define objects to read FastA files.
    
    instantiation: 
    thisReader = FastAreader ('testTiny.fa')
    usage:
    for head, seq in thisReader.readFasta():
        print (head,seq)
    '''
    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''
        self.fname = fname
            
    def doOpen (self):
        ''' Handle file opens, allowing STDIN.'''
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)
        
    def readFasta (self):
        ''' Read an entire FastA record and return the sequence header/sequence
        '''
        
        header = ''
        sequence = ''
        
        with self.doOpen() as fileH:
            
            header = ''
            sequence = ''
            
            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                line = fileH.readline()
            header = line[1:].rstrip()

            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()

        yield header,sequence
        
        
def main():
    """
    Calls functions and prints returned list of conservation scores to a file.
    """
    
    sequenceConservation.fastaConverter()
    run(["clustalo", "-i", "fastaFile.txt", "-o", "alignedSequences"])    #input and output files for ClustalOmega
    myReader = FastAreader('alignedSequences')                            #aligned sequences from ClustalOmega 
    s = sequenceConservation()
    s.score = s.conservationScore(myReader)
    with open("conservationScores.txt", "w") as textFile:                #writes scores to outfiles 
        count = 0
        for score in s.score:
            count += 1
            textFile.write(str(count) + "\t")
            textFile.write(str(score) + "\n") 
            
    
if __name__ == "__main__":
    main()  
    

    
    
    