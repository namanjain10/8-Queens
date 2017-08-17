from  functions_queen import *

arr = []
count = 8

for i in range (0,8) :
    arr.append([])
    for j in range (0,8) :
        arr[i].append(0)

q = process(arr,0,1)

if q == 1 :
    print ('final chess board standings are')
    printarr(arr)
    
else :
    print ("oops!!")