#!/usr/bin/python

import datetime, sys

def days2(dat):
    dat = datetime.datetime.strptime(dat,'%m%d%y')
    now = datetime.datetime.now()
    return (dat-now).days

if __name__ == "__main__":
    print days2(sys.argv[1])
