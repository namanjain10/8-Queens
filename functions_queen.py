def horizontal (arr,x,y) : 
    q = 0
    for i in range (0,8) :
        if i == y :
            
            if i < 7 :
                i += 1
            elif i == 7 :
                break
        #arr[x][i] = 'X'
        if arr[x][i] == 1 :
            q = 1
            break
    
    return q

def vertical (arr,x,y) :
    
    q = 0
    for i in range (0,8) :
        if i == x :
            
            if i < 7 :
                i += 1
            elif i == 7 :
                break
                
        if arr[i][y] == 1 :
            q =1
            break
    return q
 
def diagonal (arr,x,y) :
    q = 0
    i = x
    j = y
    
    while i < 7 and j < 7 :
        
        if arr[i+1][j+1] == 1 :
            q = 1
            return q
                
        i += 1
        j += 1
    
    i = x
    j = y
        
    while i < 7 and j > 0 :
    
        if arr[i+1][j-1] == 1 :
            q = 1
            return q
        
        i += 1
        j = j - 1

    i = x
    j = y
        
    while i > 0 and j < 7 :
        
        if arr[i-1][j+1] == 1 :
        
            q = 1
            return q
        
        i = i - 1
        j += 1
    
    i = x
    j = y
        
    while i > 0 and j > 0 :
        
        if arr[i-1][j-1] == 1 :
            q = 1
            return q
        
        i = i - 1
        j = j - 1
    
    return q
    
def printarr (arr) :        
    
    for i in range (0,8) :
        for j in range (0,8) :
            print (arr[i][j],end = ' | ')
        print ()    
        print ('------------------------------')
        
def search (arr,x,y) :
    t = -1
    for i in range (y,8) :
        
        if horizontal(arr,x,i) == 0 :
            
            if vertical(arr,x,i) == 0 :
    
                if diagonal(arr,x,i) == 0 :
                    t = i
                    break
    return t

def process (arr,x,y) :
    j = search(arr,x,y)
    
    if j == -1 :
        return -1
    
    else :
        arr[x][j] = 1
        print ('putting value at x = ', x, 'j = ', j)
        printarr(arr)
        
        if x < 7 :
            q = process(arr,x+1,0)
            
            if q == -1 :
                arr[x][j] = 0
                print ('removing value at x = ', x, 'j = ', j)
                printarr(arr)
                
                if j == 7 :

                    return -1
                
                else :
                    return process(arr,x,j+1)
                
            else :
                return 1
            
        elif x == 7 :
            print ('putting value at x = ', x, 'j = ', j)
            arr[x][j] == 1
            return 1