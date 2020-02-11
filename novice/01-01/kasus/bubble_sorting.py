#!/usr/bin/python

def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
Angka=[1,6,53,62,9,13,76,99]
BubbleSort(Angka)
print(Angka)