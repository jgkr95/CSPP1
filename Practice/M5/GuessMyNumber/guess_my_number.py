'''Guess My Number Exercise'''
def main():
    '''guess my number'''
    mid_n = 50
    high_n = 100
    low_n = 0
    input_n = 'l'
    print("Guess any anumber between 0-99")
    while input_n != 'c':
        print(mid_n)
        print("Enter 'h' if guess is too high,")
        print("'l' if its too low.'c' to indicate I guessed correctly")
        input_n = input()
        if input_n == 'h':
            high_n = mid_n
            mid_n = (high_n + low_n) // 2
        elif input_n == 'l':
            low_n = mid_n
            mid_n = (high_n + low_n) // 2
    print('your guess number is :', mid_n)
if __name__ == "__main__":
    main()
