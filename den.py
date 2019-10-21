def checker(a):
    
    for i in range(3):
        for g in range(3):
            if a[i][g] != (i*4)+g+1 :
                return False
    return True
                
