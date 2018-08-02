''' Assume s is a string of lower case characters. '''
#that counts up the number of vowels contained in the string s
#Number of vowels: 5

def main():
    '''This is the main method'''
    st_vo = raw_input()
    vowels = 0
    for i in st_vo:
        if i in ("a", "e", "i", "o", "u"):
            vowels = vowels+1
    print(vowels)

if __name__ == "__main__":
    main()
