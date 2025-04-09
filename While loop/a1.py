# Natural numbers : 1,2,3,4,5.........n 
# sum of natural numbers
# input from the user

n = int(input("Enter your number : "))
i=1
sum=0
while(i<=n):
  sum = sum+i
  i+=1 # i = i+1

print("The sum of numbers upto", n, "is : ", sum)

# Direct formula : n (n+1)/2
 