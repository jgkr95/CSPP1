'''Write a python program to find the square root of the given number
 using newton raphson'''
def main():
    '''This is newtonraphson method'''
    s_r = int(input())
    epsilon_n = 0.01
    trial_l = s_r/2.0
    while abs(trial_l*trial_l - s_r) >= epsilon_n:
        trial_l = trial_l - (((trial_l**2) - s_r) / (2*trial_l))
    print(str(trial_l))

if __name__ == "__main__":
    main()
