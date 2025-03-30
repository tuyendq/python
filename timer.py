from contextlib import contextmanager

@contextmanager
def timer():
    """
    A context manager that measures the execution time of a block of code.

    Yields:
        None

    Usage:
        with timer():
            # Code to be timed goes here

    The execution time is printed to the console upon exiting the context manager.
    """
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")

def copyfile(src, dst):
    """
    Copies the contents of a source file to a destination file.

    Args:
        src (str): The path to the source file.
        dst (str): The path to the destination file.

    Returns:
        None
    """
    with open(src, 'r') as src_file:
        with open(dst, 'w') as dst_file:
            dst_file.write(src_file.read())

def main():
    """
    The main function of the program.

    This function demonstrates the usage of the `timer` context manager.
    It simulates a time-consuming operation by sleeping for 2 seconds.
    """
    import time
    with timer():
        # Simulate a time-consuming operation
        time.sleep(2)
    print("Done!")

    with timer():
        copyfile("test17.txt", "test18.txt")
    print("Done!")

if __name__ == "__main__":
    """
    Entry point of the program.

    This code block is executed when the script is run directly (not imported as a module).
    It calls the `main` function to demonstrate the usage of the `timer` context manager.
    """
    main()