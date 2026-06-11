""" 
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 25 ; it is also an odd square.

The first 5 square numbers are: 1,2,4,9,16  and the sum of the odd squares is 1+9+25 = 35.

Among the first 870 thousand square numbers, what is the sum of all the odd squares?

"""
def sum_of_odd_squares(limit: int):
        ''' This function takes a integer and returns the sum of all the odd squares up to that integer. '''
        square_nums = []

        for i in range(limit + 1):
            square_nums.append(i**2)

        print(len(square_nums))

        total = 0
        for num in square_nums:
            if num % 2 > 0:
                total += num

        return total

print(sum_of_odd_squares(870000))

