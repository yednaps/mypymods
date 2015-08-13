#!/usr/bin/python

import datetime, sys

def days2(dat1,dat2):
    dat1 = datetime.datetime.strptime(dat1,'%m%d%y')
    if dat2:
        dat2 = datetime.datetime.strptime(dat2,'%m%d%y')
    else:
        dat2 = datetime.datetime.now()
    return (dat1-dat2).days

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: dtdelta DATE2 [Optional DATE1 - now if not provided]")
    elif len(sys.argv) == 2:
        print(days2(sys.argv[1],None))
    else:
        print(days2(sys.argv[1],sys.argv[2]))
