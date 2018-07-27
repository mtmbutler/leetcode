#class Solution:
def reverse(x):
    """
    :type x: int
    :rtype: int

    Given a signed int, returns an int with the digits reversed.
    """
    # Create a string of x
    x_str = str(x)

    # Create a list of x's digits
    dig_list = []
    for char in x_str:
        dig_list.append(char)

    # Control for negative numbers
    if dig_list[0] == '-':
        dig_list = dig_list[1:]
        neg = True
    else:
        neg = False

    # Create a return string and load it with x's digits in reverse order
    ret_str = ''
    for i in range(len(dig_list)):
        ret_str += dig_list[len(dig_list) - 1 - i]

    # Add negative sign if necessary
    if neg:
        ret_str = '-' + ret_str

    # Return the reversed number, conditional on overflow
    if float(ret_str) > 2**31 or float(ret_str) < -1*2**31:
        return 0
    else:
        return int(ret_str)

if __name__ == '__main__':
    num_to_reverse = 123
    print('Reversing {}: {}'.format(num_to_reverse, reverse(num_to_reverse)))