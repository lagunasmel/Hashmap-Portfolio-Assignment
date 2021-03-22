# Word Counter

**Word Counter** is a terminal-based app that accepts an input file, computes the number of times each word was used in the file, and returns the top 10 words and associated counts for each word as a list of tuples.

In order to count each word, a hash map is created for each word and linked lists are used to iterate through the buckets.


## Sample run

    python3 word_count.py alice.txt
    

## Sample results

    [('the', 1644), ('and', 872), ('to', 729), ('a', 632), ('she', 541), 
    ('it', 530), ('of', 514), ('said', 462), ('i', 408), ('alice', 386)]




