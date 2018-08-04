'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    int_input = int(input())
    m_in = 1
    if int_input == 0:
        print(str(int_input))
    else:    
        if int_input < 0:
            int_in = -1 * int_input
            while int_in > 0:
                rem_i = int_in % 10
                m_in = m_in * rem_i
                int_in = int_in // 10
            m_in = m_in * -1
            print(str(m_in))
            break
        else:
            while int_input > 0:
                rem_i = int_input % 10
                m_in = m_in * rem_i
                int_input = int_input // 10
                print(str(m_in))
                break

if __name__ == "__main__":
    main()
