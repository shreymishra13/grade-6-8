def isEvenOdd(n):
  if(n ^ 1 == n + 1 ):
    return True
  else:
    return False


def isEvenOddUsingAnd(n):
    if(n&1==1):
        return False
    else:
        return True     

number = int(input("Enter your number: "))
if isEvenOddUsingAnd(number):
  print(number, "is even")

else:
  print(number, "is odd")