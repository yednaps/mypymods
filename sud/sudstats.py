#!/usr/bin/python

# script to summarize sudoku results csv
import sys,datetime
from pytag import asciihisto

try:
    file = open(sys.argv[1],'r')
except:
    print('no file given')

def tosec(inp):
    h,m,s = map(int, inp.split(':'))
    return h*3600 + 60*m + s

def stats(inp):
    avg = str(datetime.timedelta(seconds=sum([i[1] for i in inp])/len(inp)))
    rank = sorted(inp, key=lambda x: x[1])
    best = (rank[0][0],str(datetime.timedelta(seconds=rank[0][1])))
    worst = (rank[-1][0],str(datetime.timedelta(seconds=rank[-1][1])))
    return (best,worst,avg,rank)
    
dic = {l: [] for l in 'emhf'}
level = {'e': 'Easy',
         'm': 'Medium',
         'h': 'Hard',
         'f': 'Fiendish'}

tottime = {'e': 0,
           'm': 0,
           'h': 0,
           'f': 0}

all = [(y, (x,tosec(z))) for x,y,z in [i.split(',') for i in file.readlines()]]

for gl, gs in all: 
    dic[gl].append(gs)
    tottime[gl] += gs[1]

print('Statistics for sud')
#print('Overall:')
for lev in 'emhf':
    if tottime[lev] > 0:
	    print('{}:\t{:>8} (n={:2d})'.format(level[lev],datetime.timedelta(seconds=tottime[lev]),len(dic[lev])))
print('Total:\t{} (n={:2d})'.format(datetime.timedelta(seconds=sum(tottime.values())),len(all)))

for lev in [i for i in 'emhf' if i in dic]:
    if len(dic[lev]) > 0:
        s = stats(dic[lev])
        print('\n'+'='*78)
        print('Level {}\nbest:\t{} on {}\nworst:\t{} on {}\navg:\t{}\n'.format(\
              level[lev],s[0][1],s[0][0],s[1][1],s[1][0],s[2]))
        #print('Top 10 Overall Scores:')
        histo = asciihisto(dic[lev][-15:],maxRows=9,prt=False)
        for i,j in enumerate(s[3][:10]):
            print('{:2d}. {} on {}'.format(i+1,str(datetime.timedelta(seconds=j[1])),j[0]) + histo[i].expandtabs(3))
        #print('')
        #asciihisto(dic[lev])
