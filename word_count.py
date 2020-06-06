# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")


def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500, hash_function_2)

    # This block of code will read a file one word at a time and
    # put the word in `w`. It should be left as starter code.

    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                # Convert all words to lowercase prior to insertion
                w = w.lower()
                # If the word is already in the hash map, pass the value with a new updated count
                if ht.contains_key(w):
                    count = ht.get(w) + 1
                    ht.put(w, count)
                else:
                    # Otherwise, create a new entry in the hashmap
                    ht.put(w, 1)

    # Add all of the words to the keys set
    for bucket in ht.get_buckets():
        # Iterate through each bucket/linked list
        curr = bucket.head
        while curr is not None:
            # Add the keys as a tuple
            keys.add((curr.key, curr.value))
            curr = curr.next

    # Cast the set as a list
    all_words = list(keys)
    # Sort the words according to their value in the tuple
    all_words.sort(key=lambda word: word[1])
    slice_val = (number * -1 - 1)
    top_wds = all_words[:slice_val:-1]

    return top_wds
