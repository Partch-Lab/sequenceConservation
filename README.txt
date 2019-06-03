Authors: Roshan Ahmed, Kourosh Kouhmareh

Special thanks to Carrie Partch and the Partch Lab at UCSC
The following program allows you to run a b-column analysis of a protein given many sequence. 

-----------------------
REQUIRED INSTALLATIONS 
-----------------------

CLUSTAL OMEGA (http://www.clustal.org/omega/) # sequence alignment
data2bfactor (http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/) # python script that will be used in PyMol
PyMol (https://pymol.org/2/)

(Before you start, make a folder in an easily accessible location that will contain this program, 
sequences, alignment package, and program output files)

***Your folder will need to contain the following before you run the program***

    - sequenceConservation.py
    - clustalo, along with all 4 application extensions 
    - data2bfactor.py (for PyMol)
    - sequence list (see below)
    

-------------------
OBTAINING SEQUENCES 
-------------------

Open a Microsoft Excel Spreadsheet and label Column A as Species and Column B as Sequence

Once you finish your sequence list, save your spreadsheet as a .csv (comma separated values) and save in the 
same folder with your program

***THE PROGRAM WILL COMPARE ALL SEQUENCES TO THE VERY FIRST ENTRY***


-------------------
RUNNING THE PROGRAM
-------------------

Using any IDE, open sequenceConservation

    - Go to Line 50, and type your .csv file name (i.e, ‘proteinBank.csv’)
    - Go to Line 169 and name your output file
    - Go to Line 170 and put that same output file name ( to be read by the FastA reader )
    - Go to Line 173, and give a name to your final text file with all of your b-scores, 
      (this is the file you will be inputting into PyMol)

After running, your folder will now include the following additional files:

- fasta file
- conservation score file 
- aligned sequences file    


-----------------------
PyMol B-Factor Analysis
-----------------------

- Open PyMol and display your protein of interest

- In the PyMol command line, run the following commands in this order 

	> run ~/***location of folder***/data2bfactor.py 
	> select MyChainA, resi 1- # (# of a.a scores in conservationScore file)      
    > data2b_res MyChainA, /location of conservationScores/cScorefilename.txt
    > spectrum b, (color choice), MyChainA, minimum = 0, maximum = 1        ***(sets b-column limits)***
    > set seq_view, 1 (allows you to see the entire polypeptide sequence with each amino acid colored 
        to corresponding b-column score

    
	**for a list of color choices, visit https://pymolwiki.org/index.php/Spectrum** 
        (you could also combine any colors of your choice to create a spectrum, i.e (green_white)


