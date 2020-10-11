def add_two_numbers(a, b):
    '''
    The function takes in 2 numbers and prints their sum
    
    Args:
        a,b : two real numbers
    '''
    sum = a + b
    print(sum)


def subtract_two_numbers(a, b):
    """
    The function takes in 2 numbers and prints their difference

    Args:
        a,b : two real numbers
    """

    diff = a - b
    if b > a:
        diff = b - a
    print(diff)


add_two_numbers(5, 2)  # expected result 7
subtract_two_numbers(5, 2)  # expected result 3
