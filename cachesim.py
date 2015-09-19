#! /usr/bin/python2.7
# encoding=utf8
import sys
from collections import OrderedDict

archivo = sys.argv[1]
algoritmo = sys.argv[2]
n = int(sys.argv[3])

def LRU(wlf,n):
    misses = 0
    hits = 0
    total = 0
    cache = collections.OrderedDict()
    print 'Algoritmo LRU con cache de tamano '+ str(n)
    with open(wlf) as f:
        for line in f:
            if (line in cache):  # HIT
                del cache[line]
                # cache.pop(line)
                cache[line] = ''
                hits += 1
            else: # MISS
                misses += 1
                if len(cache) == n :
                    cache.popitem(last=False)
                cache[line] = ''
    total = hits + misses
    f.close()
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses*100)/(total)),3))+'%'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses*100)/(total-n)),3))+'%'
    with open("log.csv", "a") as output:
        output.write('LRU,'+str(misses)+','+str(n)+'\n')
    output.close()



def OPTIMO(wlf,n):
    pages=[]
    # Read pages from file.
    f = open(wlf)
    pages= f.read().splitlines()
    f.close()
    cache_list = OrderedDict()
    page_fault=0
    count=0
    # Insertion of pages to memory and calculation of page faults.
    for page in pages:
        tam_cache=len(cache_list)
        lista=[]
        count+=1
        if not cache_list.__contains__(page):
            if tam_cache < n:
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
    return page_fault
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(page_fault*100)/(3721736)),3))+'%'
    print 'Miss rate (warm cache): ', ' '+str(round((float(page_fault*100)/(3721736-n)),3))+'%'
    with open("log.csv", "a") as output:
        output.write('OPTIMO,'+str(page_fault)+','+str(n)+'\n')
    output.close()

if algoritmo.upper() == 'LRU':
	LRU(archivo,n)
elif algoritmo.upper() == 'OPTIMO':
	OPTIMO(archivo,n)
else:
	print 'Algoritmo no disponible.'
