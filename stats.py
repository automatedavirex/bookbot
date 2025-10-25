
from collections import Counter

def word_count(file_contents):
        word_count = len(file_contents.split())
        return word_count

def char_count(file_contents):
        lowercase_contents = file_contents.lower()
        char_frequencies = Counter(lowercase_contents)
        return char_frequencies

def sort_dict(counted_list):
        #sorted_list = counted_list.sort(reverse=True, key=sort_on)
        return sorted_list

#print(f"Character frequencies: {char_frequencies}")