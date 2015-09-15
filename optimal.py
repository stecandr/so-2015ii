
from sys import argv # Library used for the inline parameter in this program.
from collections import OrderedDict,deque
from copy import copy



# Read pages from file.
input_file = argv[1]
f = open(input_file)
pages= f.read()
 
f.close()
cache_list = OrderedDict()          # List containing the pages in physical memory.
list_visto=[]

# Optimal Page Replacement Algorithm.
def Optimal(pages,tam):
    page_fault=0
    tam_cache=len(cache_list)

    # Insertion of pages to memory and calculation of page faults.
    for page in pages:
        if not cache_list.__contains__(page):
            if tam_cache < tam:
                cache_list[page]=''
                page_fault += 1
	
	return page_fault



op_page_faults = Optimal(pages,50000)
print'Optimal Page Replacement Algorithm Page Faults: ' + str(op_page_faults) 