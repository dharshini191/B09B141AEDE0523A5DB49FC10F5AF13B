num=7
factorial=1
if num<0:
    print("Sorry,Factorial does not exit for negative numbers")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    for i in (1,num + 1):
       factorial =factorial*i
    print("the factorial of",num,"is",factorial)
  
      