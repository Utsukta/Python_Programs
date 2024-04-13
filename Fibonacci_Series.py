#Program to find fibonacci Series(1st way)
def fibo(n):
    fibo_list=[]
    a,b=0,1
    while len(fibo_list)<n:
        fibo_list.append(a)
        a,b=b,a+b
    return fibo_list
    
c=fibo(5)
print(c)
    
#Program to find fibonacci Series(2nd way)

