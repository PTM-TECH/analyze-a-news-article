#import regular expression module 
# -> helps remove punctuations and extract clean words.
import re

# dummy while loop for testing
i = 0
while i < 1:
    break

#function to count specific word
def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0
    # conversion both text and search_word to lowercase for case-insensitive matching
    text = text.lower()
    search_word = search_word.lower()
    
    #format to remove punctuation and extract words only
    words = re.findall(r'\b\w+\b', text)
    
    count = words.count(search_word)
    return count
    
def identify_most_common_word(text):
    if not text:
        return None
    # conversion to lowercase for case-insensitive matching
    text = text.lower()
    #format to remove punctuation and extract clean words
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return None
    #initialize empty dictionary to store word counts
    word_count = {}
    
    #loop through each word
    for word in words:
        if word in word_count:
            word_count[word] += 1 #if word exists increment count
        else:
            word_count[word] = 1 #add word to dictionary
            
    #Identify most common word/with highest count
    most_common_word = max(word_count, key = word_count.get)
    return most_common_word

def calculate_average_word_length(text):
    if not text:
        return 0
    #extract words only
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return 0
    
    #initialize variable to store total number of characters
    total_length = 0
    
    #loop through each word
    for word in words:
        total_length += len(word) # add length to each word
        
    average = total_length / len(words)
    return average

def count_paragraphs(text):
    #if text is empty or only spaces, return 1
    if not text:
        return 1
    
    #split text into blocks separated by empty lines
    paragraphs = text.strip().split("\n\n")
    return len(paragraphs)

def count_sentences(text):
    if not text:
        return 1
    #find all sentence-ending punctuation marks
    sentences = re.findall(r'[.!?]+', text)
    return len(sentences)

