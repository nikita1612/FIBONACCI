x = int(input("no.of.terms"))
n1=0
n2=1
count=0
if x == 1:
    print(n1)
elif(x>1):
    while count<x:
        print("Fibonacci series are:",n1)
        a = n1+n2
        n1=n2
        n2=a
        count+=1
        
    
    
