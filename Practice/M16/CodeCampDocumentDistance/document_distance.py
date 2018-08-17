'''
    Document Distance - A detailed description is given in the PDF
'''
import re, collections, math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    similarity_cos = 0
    dict1 = dict1.strip().lower()
    dict2 = dict2.strip().lower()
    dict1 = dict1.split(' ')
    dict2 = dict2.split(' ')
    regex = re.compile('[^a-z]')
    dict1 = [regex.sub('', word.strip()) for word in dict1]
    dict2 = [regex.sub('', word.strip()) for word in dict2]
    # print(sorted(dict1))
    # print("--------------------------------")
    # print(dict2)
    # print(dict1==dict2)
    stopwords = load_stopwords("stopwords.txt")
    # freq1 = {}
    # freq2 = {}
    freq = {}
    dict1_ = []
    dict2_ = []
    for word in dict1:
        if word not in stopwords:
            dict1_.append(word)
    for word in dict2:
        if word not in stopwords:
            dict2_.append(word)
    for word in dict1_:
        if len(word) > 0:
            if word not in freq:
                freq[word]=[0,0]
            freq[word][0] += 1
    for word in dict2_:
        if len(word) > 0:
            if word not in freq:
                freq[word]=[0,0]
            freq[word][1] += 1
    # print(freq)
    # temp = freq.copy()
    # for word in temp:
    #     if word in stopwords:
    #         # print(word)
    #         del freq[word]
            # print(word)
            # temp.append(word)
    # print(sorted(l),"---------------------")
    # for word in temp:
    #     del freq[word]
    # print("frequncies",sorted(freq))

    numerator1 = 0
    for word in freq:
        numerator1 += (freq[word][0] * freq[word][1])
    # print(numerator1)
    sum_square1 = 0
    sum_square2 = 0
    for word in freq:
        sum_square1 += freq[word][0]**2
        sum_square2 += freq[word][1]**2
    denominator = math.sqrt(sum_square1*sum_square2)
    similarity_cos = numerator1/denominator
    # freq1=collections.Counter(dict1)
    # freq2=collections.Counter(dict2)
    # # print(freq1)
    # # print(freq2)
    

    # f1 = list(freq1.values())
    # f2 = list(freq2.values())
    # # n = min(len(f1),len(f2))
    # # print(f1,"----------------",f2)
    # # numerator = 0
    # square_f1 = 0
    # square_f2 = 0
    # # # sqrt_f1 = 0.0
    # # # sqrt_f2 = 0.0
    # # for i in range(n):
    # #     numerator += f1[i] * f2[i]
    # # # print(numerator)
    # for i in range(len(f1)):
    #     # print(f1[i])
    #     square_f1 = square_f1 + f1[i]**2
    # # sqrt_f1 = math.sqrt(square_f1)
    
    # for i in range(len(f2)):
    #     # print(f2[i])
    #     # print(square_f2 = square_f2 * int(f2[i]**2))
    #     # print(i,square_f2)
    #     square_f2 = square_f2 + (f2[i]**2)
        
    # # sqrt_f2 = math.sqrt(square_f2)
    # # print(square_f1,square_f2)
    # similarity_cos = (numerator1/math.sqrt(square_f1*square_f2))
    # # if similarity_cos < 0.01:
    # #     return round(similarity_cos,2)
    # # return round(similarity_cos,1)
    return similarity_cos


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords.append(line.strip())
    # print(stopwords)
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))
    # print(similarity("We've been showing you a lot of great tools in computation. We've introduced simple data objects.", "We've been showing you a lot of great tools in computation. We've introduced simple data objects."))
    

if __name__ == '__main__':
    main()
