# There are about 200 built-in modules: os, collections, logging, subprocess,...
# Python Module Index: https://docs.python.org/3/py-modindex.html

import os
print(f"Data type: {type(os)}")
# help(os)

# Using an os function: getcwd()
print(os.getcwd())

# Changing directory
os.chdir()

# Import a specific function
from os import getcwd

# Import multiple functions 
from os import getcwd, chdir

# Module's attributes
# Get local environment attribute
os.environ


