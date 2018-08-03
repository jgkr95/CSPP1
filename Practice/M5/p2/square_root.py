'''Write a python program to find the square root of the given number
using approximation method'''
def main():
    '''This is main method'''
    s_r = int(input())
    ep_n = 0.01
    g_s = 0.0
    i_n = 0.1
    while abs(g_s**2 - s_r) >= ep_n and g_s <= s_r:
        g_s += i_n
    if g_s**2 - s_r >= ep_n:
        print('')
    else:
        print(g_s)

if __name__ == "__main__":
    main()
