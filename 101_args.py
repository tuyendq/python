# Two types of arguments: positional and keyword arguments

import sys

def sum_all(*args):
    """Sum all arguments. 
    An example of arbitrary argument.
    * [asterisk] means convert all arguments into a tuple.
    """
    sum = 0
    for n in args:
        sum += n
    return sum

def main():
    print(f'Example to print out arguments')
    for i in range(0, len(sys.argv)):
        print(f'Argument {i}: {sys.argv[i]}')

    number = int(input('Enter an integer: '))
    print('Sum all integer from 0 to {} is: '.format(number), end='')
    print(sum(range(number)))

if __name__ == "__main__":
    main()
