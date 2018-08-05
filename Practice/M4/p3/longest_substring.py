'''Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc'''
def main():
    '''This is main method '''
    s = input()
    max_str=""
    max_len=0
    for i in range(len(s)): 
        if(i+1 < len(s)): 
            if(s[i]<s[i+1]) : 
                temp_len=1 
                j=i+1       
                while j+1 <len(s) and s[j]<=s[j+1]: 
                        temp_len=temp_len+1

                if(temp_len > max_len): 
                        max_str = s[i:j+1]
    print(max_str)
if __name__ == "__main__":
    main()
