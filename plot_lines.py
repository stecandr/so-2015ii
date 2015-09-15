
import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import matplotlib.cm as cm, matplotlib.font_manager as fm
import operator, calendar
import csv
import Gnuplot
# with open('/home/keylis/Dropbox/problemas-proyecto/antiradar_weather.json') as f:
#   json_data = json.load(f)
#   f.close()

csvfile = open('log.csv', 'r')
reader = csv.DictReader( csvfile, fieldnames = ( "algoritmo","miss","cache") )
print reader

data1=[]
data2=[]
data2=[]

for row in reader:
  if row[0]==1:
    value=[]
    value.append(row[1])
    value.append(row[2])
    data1.append(value)
    
  if row[0]==2:
      value=[]
      value.append(row[1])
      value.append(row[2])
      data2.append(value)
 
  if row[0]==3:
      value=[]
      value.append(row[1])
      value.append(row[2])
      data3.append(value)
 

gp = Gnuplot.Gnuplot(persist = 1)
gp('set terminal x11 size 350,225') 
gp('set pointsize 2')
gp('set yrange [0.0:0.05]')
plot1 = Gnuplot.PlotItems.Data(data1, with_="linespoints lt rgb 'black' lw 6 pt 1", title="LRU")
plot2 = Gnuplot.PlotItems.Data(data2, with_="linespoints lt rgb 'blue' lw 6 pt 8", title="Optimo")
plot3 = Gnuplot.PlotItems.Data(data3, with_="linespoints lt rgb 'red' lw 6 pt 4", title="Clock")

gp.plot(plot3,plot2, plot1)

epsFilename='testLines.eps'
gp.hardcopy(epsFilename, terminal = 'postscript', enhanced=1, color=1) #must come after plot() function
gp.reset() 