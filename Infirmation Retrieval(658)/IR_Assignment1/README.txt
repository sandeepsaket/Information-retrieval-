ASSIGNMENT 1(INFORMATION RETRIEVAL)

Dependencies used: python3, ntlk, pickle, pandas, numpy, num2words, math, sys,
os, time, string modules.

Folders and Files attached: 
	1. Please follow this URL to download english-corpora.zip:
    • https://www.cse.iitk.ac.in/users/arnabb/ir/english/
      NOTE – Please download and extract above zip file and put “english-corpora” folder in current working directory.
      
   	2. Answer_1
	A) Answer_1.py

   	3. Answer_2
	A) Answer_2_Boolean_Retrieval_Model.py
	B) Answer_2_TF_IDF.py
	C) Answer_2_BM_25.py

	4. Answer_3
	A) query_file.txt
	B) ground_truth.txt

	5. Answer_4
	A) Boolean.txt
	B) TFIDF.txt
	C) BM25.txt

	6. Answer_5
	A) Makefile
	B) README.txt


Description:
I. Answer_1.py lets you do the cleaning, processing of data and also helps to
arrange data in a structured way using nltk and num2words python module. Answer_1.py generate pickle files as filed_index.pickle, norm_dict.pickle, overall_words.pickle and post_dict.pickle with the help of pickle python module.

There are different file structures of pickle files generated as shown below.
	norm_dict: {idx : norm_value}
	post_dict: {‘word’ : [(idx, #words in idx)]}
	overall_words: {idx : [tokens]}
	filed_index: {idx: (filename, #words in file)}

Commands to run: python3 Answer_1.py or python Answer_1.py
NOTE – Please excute Answer_1.py to generate above pickle files if not dumped in current working directory.

II. Answer_2 consists of 3 python files in which all 3 models have been implemented in respected python files. Each model takes “query_file.txt” from command line as an argument and returns “*.txt” corresponding to each model with comma separated format. 

Python modules used in these implementations are numpy, pandas, os, sys, math, time and string.

Commands in make file will look like these to run each model: 
	a) python3 Answer_2_Boolean_Retrieval_Model.py query_file.txt
	b) python3 Answer_2_TF_IDF.py query_file.txt
	c) python3 Answer_2_BM_25.py query_file.txt



III. This Answer contains 2 manually written files with .txt format. File 1(query_file.txt) contains <QueryID, Query> with tab separation. File 2(ground_truth.txt) contains <QueryID, Iteration, DocID(top 10), Relevance> with comma separation. “ground_truth.txt” file has been created using manual documentation search, all 3 model result outputs to create the building block for my implemented models.

IV. Answer_4 contains 3 model generated files with .txt format named as Boolean.txt, TFIDF.txt, and BM25.txt with top 5 document search. These files are the result of each query running in each model.

V. Answer_5 contains makefile which runs all 3 models in one click. It also contains README.txt which helps to understand this assignment.

Command to run Makefile:
make run ARGS=”query_file_name.txt”
