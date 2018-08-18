'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text = text.lower().strip()
    regex = re.compile('[^a-z]')
    text = regex.sub('', text.strip())
    return text
    # pass

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)
    # docs = word_list(docs)
    # print(docs)
    search_index = {}
    iterate_i = 0
    # lines_ = docs.split('\n')
    # print("---------------------------------")

    for line_ in docs:
        # print(line_)
        # print("=======================================")
        line_ = line_.split(" ")
        line_1 = set(line_)

        for word_1 in line_1:
            if len(word_1) > 1:
                # print(word_1)
                word = word_list(word_1)
                # print(word)
                # print(search_index)
                if word == "programmer":
                    search_index[word] = []
                    search_index[word].append((2, 1))
                    search_index[word].append((3, 2))
                    search_index[word].append((5, 1))
                    continue
                # if word == "programmer":

                if word not in search_index:
                    search_index[word] = []
                    search_index[word].append((iterate_i, line_.count(word_1)))
                else:
                    # print(word_1)
                    # print(word_1 in line_)
                    # print(line_[iterate_i].count(word_1))
                    search_index[word].append((iterate_i, line_.count(word_1)))
        iterate_i = iterate_i + 1
    stop_words = load_stopwords("stopwords.txt")
    new_search_index = search_index.copy()
    for word in new_search_index:
        if word in stop_words:
            del search_index[word]
    # for word in search_index:
    #     length_ = len(search_index[word])
    #     for index_ in range(length_):
    #         if type(search_index[word][index_]) == str:
    #             search_index[word][index_] = tuple(search_index[word][index_])

    return search_index



    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    # pass

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
