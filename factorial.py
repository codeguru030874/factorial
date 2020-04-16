def fact(x):
    temp=1 #local variable of function
    if(x==1):
        return 1
    else:
        while(x>=1):
            temp=temp*x
            x=x-1
        return temp

val=int(input("Enter a positive number"))
result=fact(val)#calling function
print("Factorial of ",val,"is: ",result)
