def print_attribute( xpath ):
  print( "You have selected:" )
  for i,el in enumerate(sel.xpath( xpath ).extract()):
  	print( "%d) %s" % (i+1, el) )
      
def how_many_elements( xpath ):
  print( "You've selected %d elements" % len(sel.xpath( xpath )) )

def preview( xpath ):
  els = sel.xpath( xpath ).extract()
  n = len(els)
  for i,el in enumerate( els[:min(4,n)]):
    print( "Element %d: %s" % (i+1,el) )

