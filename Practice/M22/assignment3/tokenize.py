'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def clean_words(text):
    '''cleaning words'''
    # text = text.split(" ")
    # regex = re.compile('[^a-z]')
    # text = regex.sub('', text.strip())
    regex = re.compile('[^a-zA-Z0-9]')
    text = [regex.sub(' ', word.strip()) for word in text]
    return text


def tokenize(string):
    '''tokenise function'''
    cleaned_string = []
    for line in string:
        cleaned_string.append(clean_words(line))
    # print(cleaned_string)
    dict_string = {}
    for line in cleaned_string:
        # print(line)
        for word in line:
            # print(word,'-')
            word = word.replace(" ", "")
            # i = re.sub(' +',' ',word)
            if word.strip() not in dict_string:
                dict_string[word] = 1
            else:
                dict_string[word] += 1

    return dict_string
def main():
    '''main function'''
    number_of_lines = int(input())
    input_lines = []
    for _ in range(number_of_lines):
        input_lines.append(input().split(" "))
    # print(input_lines)
    print(tokenize(input_lines))

if __name__ == '__main__':
    main()
