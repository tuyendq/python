import contextlib
import time

@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

@contextlib.contextmanager
def my_context():
  print("hello")
  yield 42
  print("goodbye")

with my_context() as foo:
  print("foo is {}".format(foo))


@contextlib.contextmanager
def database(url):
  # set up database connection
  db = postgres.connect(url)
  yield db
  # teardown database connection
  db.disconnect()

url = "https://datacamp.com/data"
with database(url) as my_db:
  course_list = my_db.execute(
    "SELECT * FROM courses"
  )


# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)



@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('test.txt') as my_file:
  print(my_file.read())



if __name__ == "__main__":
  with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)

def main():
  pass