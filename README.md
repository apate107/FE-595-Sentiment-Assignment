# FE 595 NLP Assignment
*Sentiment Analysis using "They Fight Crime" data*

**Anand Patel**

I pledge my honor that I have abided by the Stevens Honor System.


## Setup

 To begin, place all the `.txt` files with male and female data scraped from [theyfightcrime.org](https://theyfightcrime.org)
 in the `data/` directory.

## Scripts 

This project contains four scripts:
* `merge_files.py`
* `sort_characters.py`
* `most_common.py`
* `run_all.py`

Each of the first three can be run individually (but in order if running for the first time), or alternatively,
 `run_all.py` will run all of the scripts. Running any one of the first three will write to a file or multiple files
 corresponding to the name of each script (i.e. running `merge_files.py` will generate `male_all.txt` and 
 `female_all.txt`).
 
 The final script `run_all.py` also has a command-line option when running, `-o`, which will open all of the resulting
 text files when the scripts are completed. If this is not included, then the only visual output will be the top male and
 female characters in the standard website format and the resultant files will have to be opened manually within the 
 `output/` directory.
