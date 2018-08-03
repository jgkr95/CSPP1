''' Write a python program to find if the given number is a perfect
 cube or not
using guess and check algorithm'''
def main():
    ''' input is captured in s'''
    s_r = int(input())
    n_n = 0
    for i in range(s_r):
        if i**3 == s_r:
            print(str(s_r)+" is a perfect cube")
            break    
    else:
        print(str(s_r)+" is not a perfect cube")
if __name__ == "__main__":
    main()
