#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    z = tuple(aTup[i] for i in range(0,len(aTup),2))
    return z	
    

def main():
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += data[j],
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()