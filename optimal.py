
from sys import argv # Library used for the inline parameter in this program.
from collections import OrderedDict,deque
from copy import copy


pages=[]
# Read pages from file.
input_file = argv[1]
f = open(input_file)
pages= f.read().splitlines()
f.close()
cache_list = OrderedDict()          # List containing the pages in physical memory.


# Optimal Page Replacement Algorithm.
def Optimal(pages,tam):
    page_fault=0
    count=0
    # Insertion of pages to memory and calculation of page faults.
    for page in pages:
        tam_cache=len(cache_list)
        lista=[]
        count+=1
        if not cache_list.__contains__(page):
            if tam_cache < tam:
                cache_list[page]=''
                page_fault += 1
            else:
                lista=[pages[x] for x in range(count+1,len(pages))]
                list_inters = set(lista).intersection(cache_list)
                if(len(list_inters)==len(cache_list)):
                    cache_list.popitem()
                    cache_list[page]=''
                    page_fault += 1
                else:
                    lista_comp=set(list_inters).symmetric_difference(cache_list)
                    elem=lista_comp.pop()
                    cache_list.__delitem__(elem)
                    cache_list[page]=''
                    page_fault += 1
                    print "continue"
   
    return page_fault
  

op_page_faults = Optimal(pages,50000)
print'Optimal Page Replacement Algorithm Page Faults: ' + str(op_page_faults) 