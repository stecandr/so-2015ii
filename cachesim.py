#! /usr/bin/python2.7
# encoding=utf8
import sys
from collections import OrderedDict

archivo = sys.argv[1]
algoritmo = sys.argv[2]
n = int(sys.argv[3])

def LRU(wlf,n):
    misses = 0
    total = 0
    cache = collections.OrderedDict()
    print 'Algoritmo LRU con cache de tamano '+ str(n)
    with open(wlf) as f:
        for line in f:
            total+=1
            if (line in cache):  # HIT
                del cache[line]
                cache[line] = ''
            else: # MISS
                misses += 1
                if len(cache) == n :
                    cache.popitem(last=False)
                cache[line] = ''
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



def Clock(wlf,n):
    tamCache = n   
    cache = OrderedDict()         
    misses = 0    
    total=0
    with open(wlf) as f:
        pages= f.read().splitlines()
        f.close()
        for page in pages:
            flag=0
            total += 1
            if len(cache) < tamCache:   
                if (page in cache):     
                    cache[page]=1
                else:                   
                    cache[page]=0
                    misses += 1
            else:
                if (page in cache): 
                    if(cache.get(page)==0): 
                        cache[page]=1
                else:
                    for key, value in cache.iteritems():
                        if value == 1 and flag==0:
                            cache.__setitem__(key, 0)
                        if value == 0 and flag==0:
                            flag=1
                            cache.__setitem__(page, 0)

                    if flag==0:
                        print flag
                        cache.popitem() 
                        cache[page]=0
                        misses += 1
    print total
    print misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses*100)/(total)),3))+'%'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses*100)/(total-n)),3))+'%'
    with open("log.csv", "a") as output:
        output.write('Clock,'+str(misses)+','+str(n)+'\n')
    output.close()



def OPTIMO_modificado(wlf,n):
    pages=[]
    # Read pages from file.
    f = open(wlf)
    pages= f.read().splitlines()
    f.close()
    cache_list = OrderedDict()
    page_fault=0
    count=0
    # Insertion of pages to memory and calculation of page faults.
    for linea in pages:
        page=linea
        count+=1
        del pages[0]
        if page not in cache_list:
            if len(cache_list) < n:
                cache_list[page]=''
                page_fault += 1
            else:
                # lista=[pages[x] for x in range(count+1,len(pages))]
                list_inters = set(cache_list).intersection(pages)
                if(len(list_inters)==len(cache_list)):
                    cache_list.popitem()
                    cache_list[page]=''
                    page_fault += 1
                else:
                    lista_comp=set(list_inters).symmetric_difference(cache_list)
                    elem=lista_comp.pop()
                    del cache[elem]
                    cache_list[page]=''
                    page_fault += 1

    print str(count)
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(page_fault*100)/(3721736)),3))+'%'
    print 'Miss rate (warm cache): ', ' '+str(round((float(page_fault*100)/(3721736-n)),3))+'%'
    with open("log.csv", "a") as output:
        output.write('OPTIMO,'+str(page_fault)+','+str(n)+'\n')
    output.close()
    return page_fault



if algoritmo.upper() == 'LRU':
	LRU(archivo,n)
elif algoritmo.upper() == 'OPTIMO':
	OPTIMO(archivo,n)
else:
	print 'Algoritmo no disponible.'
