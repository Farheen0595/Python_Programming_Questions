'''
Reverse a string
'''

def reverse_string(string: str) -> str:

    '''Reverse a string using a for loop.
    '''
    string_reversed = ''

    for i in string:

        string_reversed = i + string_reversed

    return string_reversed


if __name__ == '__main__':
    test_string = 'Hello, World!'
    print(reverse_string(test_string))




# def reverse_string(string : str) -> str:

#     string_reversed = ''

#     for i in range(len(string)-1,-1,-1):

#         string_reversed += string[i]

#     return string_reversed


# if __name__ == '__main__':
#     test_string = 'Hello,World!'
#     print(reverse_string(test_string))
