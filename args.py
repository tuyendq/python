def sum_all(*args):
    """Sum all arguments"""
    sum = 0
    for n in args:
        sum += n
    return sum

def main():
    number = int(input('Enter an integer: '))
    print('Sum all integer from 0 to {} is: '.format(number), end='')
    print(sum(range(number)))

if __name__ == "__main__":
    main()
