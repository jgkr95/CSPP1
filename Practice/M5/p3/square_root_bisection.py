'''Write a python program to find the square root of the given number
 using approximation method'''
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''this is bisection'''
    s_r = int(input())
    epsilon_n = 0.01
    low_o = 0.0
    high_h = s_r
    avg_g = (high_h + low_o)/2.0
    while abs(avg_g ** 2 - s_r) >= epsilon_n:
        if avg_g ** 2 < s_r:
            low_o = avg_g
        else:
            high_h = avg_g
        avg_g = (high_h + low_o)/2.0
    print(avg_g)

if __name__ == "__main__":
    main()
