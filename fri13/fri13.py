def daysDict():
    "Return dict for matching datetime.date.weekday() to a day"
    return {i: j[:3] for i,j in \
            enumerate([k.ctime() for k in \
            [base + datetime.timedelta(x) for x in range(7)]])}


def friday13():
    fris = {}
    for yr in range(1,9999):
        fris[yr] = [datetime.date(yr,j,13) for j in range(1,13) \
                    if datetime.date(yr,j,13).weekday() == 4]
    return fris

def nextFri13(dt=datetime.date.today()):
    f = friday13()
    out = [i for i in f[dt.year] if i > dt]
    if len(out) > 0: return out[0]
    else: return f[dt.year+1][0]

def next3xYr(dt=datetime.date.today()):
    f = friday13()
    yr = dt.year + 1
    while yr < max(f.keys()):
        if len(f[yr]) == 3: return datetime.date(yr,1,1)
        else: yr += 1
    return "NEVER!!!"

def tripleYr(min=1,max=9998):
    f = friday13()
    return [datetime.date(yr,1,1) for yr in range(min,max+1) if len(f[yr]) == 3]

def doubleYr(min=1,max=9998):
    f = friday13()
    return [datetime.date(yr,1,1) for yr in range(min,max+1) if len(f[yr]) == 2]

def singleYr(min=1,max=9998):
    f = friday13()
    return [datetime.date(yr,1,1) for yr in range(min,max+1) if len(f[yr]) == 1]
