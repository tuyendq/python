# Working with strings
# String is a built-in data type (others are int, float, bool, list, etc.)
# String is a sequence of characters (each character is a string of length 1)
import string

# string attributes
print(string.ascii_lowercase)
print(string.punctuation)


print("this is a string")

if type("this is a string") is str:
    print("yes")
else:
    print("no")

str1 = "This is a string"  # using double quote
str2 = 'This is a string, too'  # using single quote
str3 = """Yet another string, too
        spreading multi lines
        """  # using triple quote

# string concatenation
str4 = str1 + " " + str2 + " " + str3

# string methods
print(str4.upper())
print(str4.lower())
print(str4.title())
print(str4.capitalize())
print(str4.swapcase())
print(str4.replace("string", "STRING"))
print(str4.split())
print(str4.splitlines())
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
print(str4.find("string"))
print(str4.rfind("string"))
print(str4.count("string"))
print(str4.startswith("This"))
print(str4.endswith("too"))
print(str4.isalnum())
print(str4.isalpha())
print(str4.isdigit())
print(str4.islower())
print(str4.isupper())
print(str4.istitle())
print(str4.isspace())
print(str4.isidentifier())
print(str4.isprintable())
print(str4.isascii())
print(str4.isdecimal())
print(str4.isnumeric())
print(str4.join("123"))
print(str4.zfill(50))
print(str4.center(50))
print(str4.ljust(50))
print(str4.rjust(50))
print(str4.expandtabs(50))
print(str4.partition("string"))
print(str4.rpartition("string"))
print(str4.split("string"))
print(str4.rsplit("string"))
print(str4.splitlines())
print(str4.splitlines(True))
print(str4.splitlines(False))
print(str4.splitlines(1))
print(str4.splitlines(0))
print(str4.splitlines(2))
print(str4.splitlines(3))
print(str4.splitlines(4))

