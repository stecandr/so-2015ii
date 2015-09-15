#! /usr/bin/python2.7
# encoding=utf8
import sys

archivo = sys.argv[1]
algoritmo = sys.argv[2]
n = int(sys.argv[3])

def LRU(wlf,n):
	misses = 0
	hits = 0
	total = 0
	cache = {}
	print 'Algoritmo LRU con cache de tamano'+ str(n)
	with open(wlf) as f:
		for line in f:
			if (line in cache):  # HIT
				del cache[line]
				cache[line] = ''
				hits = hits + 1
			else: # MISS
				misses = misses + 1
				cache[line] = ''
				if len(cache) > n :
					cache.popitem()
	total = hits + misses
	f.close()
	print "Resultados: "
	print "Miss rate: ", '              '+str(round((float(misses)/(total)),3))+'%'
	print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(total-n)),3))+'%'
	with open("log.csv", "a") as output:
		output.write('LRU,'+str(misses)+','+str(n)+'\n')
	output.close()



def OPTIMO(wlf,n):
	misses = 0
	hits = 0
	total = 0
	cache = {}
	print 'Algoritmo OPTIMO con cache de tamano '+ str(n)
	with open(wlf)as f:
		for line in f:
			if (line in cache): # HIT
				hits = hits + 1
			else: # MISS
				misses = misses + 1
				cache[line] = ''
				if len(cache) > n :
					cache.popitem(last=False)
	total = hits + misses
	f.close()
	print "Resultados: "
	print "Miss rate: ", '              '+str(round((float(misses)/(total)),3))+'%'
	print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(total-n)),3))+'%'
	with open("log.csv", "a") as output:
		output.write('OPTIMO,'+str(misses)+','+str(n)+'\n')
	output.close()

def CLOCK(wlf,n):
	misses = 0
	hits = 0
	total = 0
	cache = {}
	print 'Algoritmo CLOCK con cache de tamano '+ str(n)
	with open(wlf) as f:
		i=0
		referenced =[]
		for line in f:
			if (line in cache): # HIT
				hits = hits + 1
				cache[line] = True
			else: # MISS
				misses = misses + 1
				cache[line] = ''
				if len(cache) > n :
					cache.popitem()
        clock=0

        for element in referenced:
            if element==True:
                misses = misses + 1
                clock = (clock + 1) % n; #for clarity
	total = hits + misses
	f.close()
	print "Resultados: "
	print "Miss rate: ", '              '+str(round((float(misses)/(total)),3))+'%'
	print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(total-n)),3))+'%'
	with open("log.csv", "a") as output:
		output.write('CLOCK,'+str(misses)+','+str(n)+'\n')
	output.close()

if algoritmo.upper() == 'LRU':
	LRU(archivo,n)
elif algoritmo.upper() == 'OPTIMO':
	OPTIMO(archivo,n)
elif algoritmo.upper() == 'CLOCK':
	CLOCK(archivo,n)
else:
	print 'Algoritmo no disponible.'
