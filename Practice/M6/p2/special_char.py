'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''Read string from the input, store it in variable str_input.'''
    str_input = input()
    len_str = len(str_input)
    i_i = 0
    while i_i < len_str:
        if  str_input[i_i] in "!@#$%^&*":
            print(" ", end="")
        else:
            print(str_input[i_i], end="")
        i_i = i_i+1

if __name__ == "__main__":
    main()
