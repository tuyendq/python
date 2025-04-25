# Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath( './*' ) )

# Print out the number
print( "The number of elements you selected was:", how_many_kids )

# Now you know the trick! In xpath, you can use the XPath string './*' to direct to the children of the currently selected element!