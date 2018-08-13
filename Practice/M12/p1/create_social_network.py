# '''
#     Assignment-1 Create Social Network
# '''

# def create_social_network(data):
#     '''
#         The data argument passed to the function is a string
#         It represents simple social network data
#         In this social network data there are people following other people

#         Here is an example social network data string:
#         John follows Bryant,Debra,Walter
#         Bryant follows Olive,Ollie,Freda,Mercedes
#         Mercedes follows Walter,Robin,Bryant
#         Olive follows John,Ollie

#         The string has multiple lines and each line represents one person
#         The first word of each line is the name of the person
#         The second word is follows that separates the person from the followers
#         After the second word is a list of people separated by ,

#         create_social_network function should split the string on lines
#         then extract the person and the followers by splitting each line
#         finally add the person and the followers to a dictionary and
#         return the dictionary

#         Caution: watch out for trailing spaces while splitting the string.
#         It may cause your test cases to fail although your output may be right

#         Error handling case:
#         Return a empty dictionary if the string format of the data is invalid
#         Empty dictionary is not None, it is a dictionary with no keys
#     '''

#     # remove the pass below and start writing your code
    
#     import re


#     aDict = {}
#     # l = len(data)
#     #for i in range(l):
#     if "follows" not in data:
#         return aDict
#     data = data.strip().split('\n')

#     for element in data:
#         k, v = element.split(" follows ")
#         # print("k=",k)
#         #print("v=",type(v),v)
#         #v=v.split(',')
#         # print(v)
#         v = re.split(',',v)
#         if k not in aDict:
#             aDict[k] = v
#         else:
#             aDict[k].append(v)
#         # print(aDict)
#     return aDict

# def main():
#     '''
#         handling testcase input and printing output
#     '''
#     string = ''
#     lines = int(input())
#     for i in range(lines):
#         i += 1
#         string += input()
#         string += '\n'

#     print(create_social_network(string))

# if __name__ == "__main__":
#     main()
'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    if "follows" in data:
        f_list = data.splitlines()
        frd_l = []
        # print(f_list)
        for i in f_list:
            k = i.split(" follows ")
            # z= k[0].split(",")
            frd_l.append(k)
        frd_dict = {}
        for i in frd_l:
            frd_dict[i[0]] = i[1].split(",")
        return frd_dict
    return {}
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string))

if __name__ == "__main__":
    main()
