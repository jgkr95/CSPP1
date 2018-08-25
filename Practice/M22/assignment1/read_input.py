'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''Main function read input'''
    number_of_lines = int(input())
    input_lines = []
    for _ in range(number_of_lines):
        input_lines.append(input())
    for line in range(number_of_lines):
        print(str(input_lines[line]))

if __name__ == '__main__':
    main()
