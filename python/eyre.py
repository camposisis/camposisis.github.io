# there is a package called nltk. load it for this file.
import nltk

def open_file_and_get_text(filename):
    #given a filename , open it.
    with open(filename, 'r') as our_file:
        #takes the fileand reads the text. Stores it.
        text = our_file.read()
    return text

def clean_tokens(words):
    #given some tokens lowercase them all

#create an empty list called clean_words
    clean_words = []

#loop over every word item in the words list
    for word in words:
    #make each word lowercase and append it to the new list.
        clean_words.append(word.lower())
    return clean_words

#set a variable filename for where our file is.
filename = "eyre.txt"

text = open_file_and_get_text(filename)

# Print the first 99 characters of the text.
print(text[0:100])

#take a long string and break it into words.
words = nltk.word_tokenize(text)
print(words[0:100])


clean_words = clean_tokens(words)
# print out first 30 words of our clean tokens
print(clean_words[0:30])
words_counts = nltk.FreqDist(clean_words)
print(words_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he','she', 'jane', 'tony'])

#lowercase matters! computers are stupid.
if "The!" != "the":
    print("Does case matter?")
