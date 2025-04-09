from math import sqrt


num = int(input("Enter your number : "))
flag = True
for j in range(num1, num2):
    for i in range(2, int(sqrt(num))):
        if(num%i==0):
           flag=False
           break
   

   
    

if(flag==True):
    print(num ," is prime")
else:
    print(num, " is composite")
        
        
# TC = O(n)


        



















number=int(input("Enter your number \n"))
if number>1:
  for i in range(2,int(sqrt(number))+1):
    if(number%i==0):
      print(number, " is not prime")
      break
  else:    
    print(number, " is prime")
else:
  print(number, "is not prime")
  