# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr, i):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if i<len(aStr):
        if char == aStr[i]:
            return True                      
        else:
            return isIn(char, aStr, i+1)
    return False
   

def main():
    data = input()
    data = data.split()
    i = 0
    print(isIn((data[0]), data[1],i))


if __name__== "__main__":
    main()