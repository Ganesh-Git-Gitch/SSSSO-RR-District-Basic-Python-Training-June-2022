import add 
import multiple as ml
import sys
a=[]
r=input().split(" ")
y=r[0]
x=r[1]
for j in x:
    if(j.isdigit()==True):
        a.append(int(j))
l=len(a)
with open("output.txt",'w') as sys.stdout:
    if(l<4 or l>4):
        print("You are entered less than or greater than 4 input numbers")
    else:
        k=a[0]
        m=a[1]
        n=a[2]
        p=a[3]
        if(y=="add"):
            f=add.add(k,m,n,p)
            if(f==False):
                print("You are entered all odd numbers")
            else:
                print("The addition of numbers are: ",f)
        elif(y=="multiply"):
            h=ml.multiply(k,m,n,p)
            if(h==False):
                print("You are entered all odd numbers")
            else:
                print("The multiplication of numbers are: ",h)
        else:
            print("Incorrect input")



        
    
    
