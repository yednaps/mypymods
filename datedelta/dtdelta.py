#!/usr/bin/python

import datetime, sys

def days2(dat1,dat2=datetime.datetime.now().strftime('%m%d%y')):
    dat1 = datetime.datetime.strptime(dat1,'%m%d%y')
    dat2 = datetime.datetime.strptime(dat2,'%m%d%y')
    return (dat1-dat2).days

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: dtdelta DATE2 [Optional DATE1 - now if not provided]")
    else:
        print(days2(*sys.argv[1:]))
