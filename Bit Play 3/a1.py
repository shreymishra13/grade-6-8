def swapUsingBitWiseOperator(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("After swapping: a =",a,"and b =",b)

def swapUsingArithmetic(a,b):
  a=a+b
  b=a-b
  a=a-b
  print("After swapping: a =",a,"and b =",b)

swapUsingArithmetic(10,20)
  