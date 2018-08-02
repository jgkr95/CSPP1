'''Assume s is a string of lower case characters.
# Write a program that prints the number of times the string
'bob' occurs in s. For example, if s = 'azcbobobegghakl', then
 your program should print
 Number of times bob occurs is: 2'''

def main():
    ''' This is the main mehtod '''
    st_sub = input()
    str_2 = "bob"
    count_bob = 0
    length_sub = len(st_sub)
    # the input string is in s
    # remove pass and start your code here
    for i in range(length_sub-2):
        if str_2 == str(st_sub[i]+st_sub[i+1]+st_sub[i+2]):
            count_bob = count_bob+1
            i = i+2
    print(count_bob)
if __name__ == "__main__":
    main()
