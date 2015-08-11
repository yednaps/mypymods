

def asciihisto(inpList,maxRows=10,tw=3,prt=True,xlabels=False,ylabels=False):
    '''ASCII Histogram generator'''
    # find max and use to gen scale factor based on maxRows
    maxN = sorted(inpList, key=lambda x: x[1])[-1][1]
    scaleFactor = float(maxRows)/maxN
    # also generate step for y-axis labels
    step = int(1/scaleFactor)

    # build bars for each data point
    outdata = [[x]+[i for i in (maxRows - int(scaleFactor * y)) * ' ' +
               int(scaleFactor * y) * '#'] for x,y in inpList]

    # transpose columns to rows
    zipout = zip(*outdata)

    if ylabels:
        # join columns in each row, adding y-axis label and |, exclude x-axis labels
        strout = [str(maxN-h*step)+ (6-len(str(maxN-h*step)))*' ' + '|\t'+'\t'.join(i)
                  for h,i in enumerate(zipout[1:])]
    else:
        strout = ['\t|\t'+'\t'.join(i)
                  for h,i in enumerate(zipout[1:])]

    if xlabels:
        # add in x-axis line and labels
        strout = strout + [6*' '+(len(zipout[0])+1)*tw*'-'] + [6*' '+'\t'+'\t'.join([str(i) for i in zipout[0]])]
    else:
        strout = strout + [3*' '+ '+' +(len(zipout[0])+1)*tw*'-']

    if prt:
        for i in strout:
            print(i.expandtabs(tw))

    return strout
