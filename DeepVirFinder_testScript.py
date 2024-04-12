#Script to try VirHunter on local computer
#https://github.com/jessieren/DeepVirFinder?tab=readme-ov-file

conda init

#this is the main format that you can find on GitHub with with descriptions
python dvf.py [-i INPUT_FA] [-o OUTPUT_DIR] [-l CUTOFF_LEN] [-c CORE_NUM]


#1. Unzip/conver fastq.gz files to fasta files
seqtk seq -a input.fastq.gz > output.fasta
#test: it works!
seqtk seq -a 10_S2_R1_001.fastq.gz > 10_S2_R1_001.fasta


#2. Move sequence files into the directory. Do I have to do this?

To move a file from one directory to another using the terminal, you can use the mv command. Here's how you can move an input.fasta file to a different directory:
bash
Copy code
mv /Users/elizabethlombardi/Desktop/Research/UNM/Herbarium RNA work/Sequence data/10_S2_R1_001.fasta /Users/elizabethlombardi/DeepVirFinder


#3. Run a test
python dvf.py -i *.fasta -o ~/output 

#test it out
python dvf.py -i 10_S2_R1_001.fasta -o ~/output 

python dvf.py -i 10_S2_R1_001.fasta -o ./test/ -l 300

#That works (or it's a new error because I didn't finish installing dependencies, perhaps). Teh fasta files need to be in the DeepVirFinder folder to get it to work, I think
