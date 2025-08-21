'''
Check if a number is prime
'''

'''
What is a Prime Number ?

A Prime No is a Number which is divided by itself and by 1 
Only two factors are there for the prime number 

'''


def is_check_prime(number : int) -> bool:

    if (number <=1):

        return False
    
    elif (number == 2):

        return True
    
    elif (number % 2) == 0 :

        return False
    else:

        for i in range(3,int(number**0.5)+1,2):

            if (number%i) == 0:
                return False
        return True



if __name__ == '__main__':

    number = int(input("Enter the Number:\n"))
    print(f'Given No is a {is_check_prime(number)}')

# def prime_numbers(number : int) -> bool:

#     if (number == 0) or (number == 1):
#         return False
    
#     else:

#         for i in number(2,number+1):

#             if i % 2 != 0:
    
