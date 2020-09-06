# Use list comprehension and "any" built-in function to print prime numbers in range(2,1000) 

def main():
    prime_numbers = []
    for i in range(2,1000):
        if any([i % j == 0 for j in range(2,i-1)]): # use list comprehension and any function
            continue
        else:
            prime_numbers.append(i)

    print(prime_numbers)


if __name__ == "__main__":
    main()