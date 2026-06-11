'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def is_multiple(limit:int, num_1:int, num_2:int):
    """
    Function takes 3 integers, one number to find sum below (limit) and two numbers to find multiples of below the limit
    """
    mulitples = []
    for i in range(limit):
        if i % num_1 == 0 or i % num_2 == 0:
            mulitples.append(i)

    total = 0
    for num in mulitples:
        total += num 
    return total 


print(is_multiple(1000,3,5))
