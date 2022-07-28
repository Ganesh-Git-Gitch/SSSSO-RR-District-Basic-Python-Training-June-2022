def multiply(a,b,c,d):
    if(a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0):
        return False
    else:
        s=1
        k=[a,b,c,d]
        for i in range(len(k)):
            if(k[i]%2==0):
                s=s*k[i]
        return s

