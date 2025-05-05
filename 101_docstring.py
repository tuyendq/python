def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and covert text to lowercase."""
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring using dunder __doc__ method
print(clean_string.__doc__)

# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))