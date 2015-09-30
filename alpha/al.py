#!/usr/bin/python

import sys,re
f = '/home/sp/python/alpha/alpha.txt'
lkup = {'A':   'ALFA',
        'B':   'BRAVO',
        'C':   'CHARLIE',
        'D':   'DELTA',
        'E':   'ECHO',
        'F':   'FOXTROT',
        'G':   'GOLF',
        'H':   'HOTEL',
        'I':   'INDIA',
        'J':   'JULIETT',
        'K':   'KILO',
        'L':   'LIMA',
        'M':   'MIKE',
        'N':   'NOVEMBER',
        'O':   'OSCAR',
        'P':   'PAPA',
        'Q':   'QUEBEC',
        'R':   'ROMEO',
        'S':   'SIERRA',
        'T':   'TANGO',
        'U':   'UNIFORM',
        'V':   'VICTOR',
        'W':   'WHISKEY',
        'X':   'XRAY',
        'Y':   'YANKEE',
        'Z':   'ZULU'}

def alpha(inp):
#    lkup = {i:j for i,j in [k.strip().split() for k in open(f).readlines()]}
#    lkup[' '] = '#'
    out = ' '.join([lkup[i] for i in re.sub('[\W_]+','',inp).upper()])
    return out

if __name__ == '__main__':
    if len(sys.argv) == 1 :
        print('Usage: alpha TEXT')
    else:
        for i in sys.argv[1:]:
            print(alpha(i))
