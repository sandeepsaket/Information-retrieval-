CS657A : INFORMATION RETRIEVAL
ASSIGNMENT-2

Dependencies used:
python3
gensim.models  
numpy
num2words 
math
pandas
matplotlib

Folders and Files need to download:
	1. Please follow this URL to download pre-trained vectors:
           https://www.cfilt.iitb.ac.in/~diptesh/embeddings/monolingual/non-contextual/
           
        2. The word similarity datasets are available from
           https://drive.google.com/drive/folders/1VovzSE1-zXH0bKCar2M8peL4-62BSlZJ?usp=sharing

        3. Download the language corpora from AI4Bharat. 
           https://indicnlp.ai4bharat.org/corpora/

Note: These downloaded files and folders should be in same directory in which code files are present.     
   	
Files present in the zip folder:

        1. Answer_1.py
        2. Answer_3.py
        3. Makefile - a make file to run whole assignment in one go
	4. README.txt


Description:

1. Answer_1.py : This file contains python code to run the question1 . 
    a. This file let us find the accuracy of each model in each dimension. 
    b. It contains various functions whose working has already been mentioned in comment sections of code.
2. Answer_3.py : This file contains python code to run the question3.
   On successful execution this generates the following text and png files
   1. top_100_charcter_unigram.txt : Top 100  unigram characters
   2. top_100_charcter_bigram.txt  : Top 100  bigram characters
   3. top_100_charcter_trigram.txt : Top 100  trigram characters
   4. top_100_charcter_quadgram.txt: Top 100  quadgram characters
   5. top_100_word_unigram.txt     : Top 100  unigram words
   6. top_100_word_biigram.txt     : Top 100  bigram words
   7. top_100_word_trigram.txt     : Top 100  trigram words
   8. top_100_syllable_unigram.txt : Top 100  unigram syllable
   9. top_100_syllable_bigram.txt  : Top 100  bigram syllable
   10.top_100_syllable_trigram.txt : Top 100  trigram syllable
   11.character_frequency.png      : graph between character frequency Vs Number of characters
   12.word_frequency.png           : graph between word frequency Vs Number of words
   13.syllable_frequency.png       : graph between syllable frequency Vs Number of syllables

3. README.TXT

4. Makefile

Command to run Makefile:

make run 

