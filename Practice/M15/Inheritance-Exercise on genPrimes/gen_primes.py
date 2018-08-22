#define the gen_primes function here
def genPrimes():
    i = 2
    while True:
        c = 0
        for j in range(2, i//2 + 1):
            if i % j == 0:
                c += 1
        if c == 0:
            yield i
            # break
        i = i + 1

def main():
    data=int(input())
    # l=data.split()
    # a=int(l[0])
    # b=int(l[1])
    primeGenerator = genPrimes()
    for i in range(data):       
        print(primeGenerator.__next__())
    
if __name__== "__main__":
    main()
