#Script to try VirHunter on local computer
#https://github.com/jessieren/DeepVirFinder?tab=readme-ov-file

conda init

#this is the main format that you can find on GitHub with with descriptions
python dvf.py [-i INPUT_FA] [-o OUTPUT_DIR] [-l CUTOFF_LEN] [-c CORE_NUM]

#1. Move fasta files into the directory 


#2. Run a test
python dvf.py -i *.fasta -o ~/output 
