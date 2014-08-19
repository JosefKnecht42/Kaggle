import os
import sys
import difflib
from test import outstanding_bugs


def get_MeanElement(data,sum):
    index = 0
    msum = 0
    for value in data:
        msum += value
        if msum > sum/2:
            return index
        index += 1 

def shift_Values(data,index):
    if index > 14:
        delta = index - 14
        for i in range(1, delta + 1):
            del data[0]
            data.append(-1)
    if index < 14:
        delta = 14 - index;
        for i in range(1, delta + 1):
            del data[-1]
            data.append(0)
    return data

def normalize_Data(data):
    msum = sum(data)
    for i in range(0,len(data)):
        data[i] = data[i]/float(msum)
    return data

def balance_row_col(filein,fileout,test = True):
    infile = open(filein)
    outfile = open(fileout,'w')
    h1 = []
    if not test: 
        h1.append('label')
    for i in range(1,29):
        h1.append('row'+str(i))
    for i in range(1,29):
        h1.append('col'+str(i))
    outfile.write(','.join(h1)+'\n')
    print h1
    lines = infile.readlines()
    counter = 0;
    for line in lines:
        counter += 1
        if counter==1:
            continue
        bits = line.split(',')
        if test:
            bits.insert(0,"0")
        bits = [int(i) for i in bits]
        rowsum = bits[1:29]
        colsum = bits[29:57]
        label = bits[0]
        
        csum = sum(colsum)
        cindex = get_MeanElement(colsum, csum)
        colsum = shift_Values(colsum,cindex)
        colsum = normalize_Data(colsum)
        
        rsum = sum(rowsum)
        rindex = get_MeanElement(rowsum, rsum)
        rowsum = shift_Values(rowsum,rindex)
        rowsum = normalize_Data(rowsum)
    
        rowsum = map(str, rowsum)
        colsum = map(str, colsum)
        if not test:
            outfile.write(str(label)+',')
        outfile.write(','.join(rowsum)+',')
        outfile.write(','.join(colsum)+'\n')
        print counter
    outfile.close()
    infile.close()

def calc_row_col_sums(filein,fileout,test = True):
    infile = open(filein)
    outfile = open(fileout,'w')
    h1 = []
    if not test: 
        h1.append('label')
    for i in range(1,29):
        h1.append('row'+str(i))
    for i in range(1,29):
        h1.append('col'+str(i))
    outfile.write(','.join(h1)+'\n')
    print h1
    lines = infile.readlines()
    counter = 0;
    for line in lines:
        colsum = []
        rowsum = []
        counter += 1
        if counter==1:
            continue
        bits = line.split(',')
        if test:
            bits.insert(0,"0")
        bits = [int(i) for i in bits]
        label = bits[0]
        for j in range(0,28):
            a = j*28+1
            b = j*28+28
            if b > 784:
                print b
            rowsum.append(sum(bits[a:b]))
            mcol = 0
            for i in range(0,28):
                a = j+i*28
                if a > 784:
                    print a
                mcol += bits[j+i*28]
            colsum.append(mcol)
        rowsum = map(str, rowsum)
        colsum = map(str, colsum)
        if not test:
            outfile.write(str(label)+',')
        outfile.write(','.join(rowsum)+',')
        outfile.write(','.join(colsum)+'\n')
        print counter
    outfile.close()
    infile.close()

if __name__ == '__main__':
    #calc_row_col_sums('data/test.csv','data/test.prep.csv', test= True)
    balance_row_col('data/train.prep.csv','data/train.prep.bal.csv', test= False)
