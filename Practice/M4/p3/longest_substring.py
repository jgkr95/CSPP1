'''Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc'''
def main():
    '''This is main method '''
    s_s = input()
    m_m = 0
    n_n = ""
    st_st = ""
    # the input string is in s
    length = len(s_s)
    c_c = 0
    for i in range(length-1):
        if ord(s_s[i]) <= ord(s_s[i+1]):
            n_n = n_n + s_s[i]
            c_c = c_c + 1
        else:
            n_n = n_n + s_s[i]
            c_c = c_c+1
            if c_c > m_m:
                m_m = c_c
                st_st = n_n
                n_n = ""
            c_c = 0
    print(st_st)
if __name__ == "__main__":
    main()
