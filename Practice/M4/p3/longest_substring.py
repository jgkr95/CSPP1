'''Assume s is a string of lower case characters.
Write a program that prints the longest
substring of s in which the letters occur in alphabetical order
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc'''
def main():
    '''This is main method '''
    s_s = input()
    print(s_s)
    max_str = ""
    max_len = 0
    length_s = len(s_s)
    for i in range(length_s):
        if i+1 < length_s:
            if s_s[i] < s_s[i+1]:
                temp_len = 1
                j = i+1
                while j+1 < length_s and s_s[j] <= s_s[j+1]:
                    temp_len = temp_len+1
                    j += 1

                if temp_len > max_len:
                    max_str = s_s[i:j+1]
                    max_len = temp_len
    print(max_str)
if __name__ == "__main__":
    main()
