"""Count words in file."""

def word_count(file):

    # inputs: given file full of words 
    # output: a printed accounting of how many times each word occurs within the file

    # open the text file in variable
    phrase = open(file)

    # create empty dictionary container held by a meaningfully named variable that can be returned
    words_in_sentence = {}


    for line in phrase:
        #strip the white space at the end of each line .rstrip()
        line = line.rstrip()
        # delimiter is space between words -(" ")
        sentence = line.split(" ")

        # iterate over words in file to access each word
        for word in sentence:
            # steps to clean up punctuation, each word individually
            word = word.rstrip("?")
            word = word.rstrip(".")
            word = word.strip(",")
            # for word in phrase:
            # dictionary[word] = dictionary.get(word, 0) + 1
            words_in_sentence[word] = words_in_sentence.get(word, 0) + 1

    # unpack dictionary
    for word, count in words_in_sentence.items():
        #print out the words and strings using an f string -> (f"{word} {count}"")
        print(f"{word} {count}")

word_count("test.txt")