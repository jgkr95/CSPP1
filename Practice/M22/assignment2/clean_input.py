'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''this is the fucntion to clean the input'''
    alphabets_numbers = 'abcdefghijklmnopqrstuvwxyz0123456789'
    new_string = ''
    for i in string:
        if i in alphabets_numbers:
            new_string += i
    return new_string

def main():
    '''This is main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
