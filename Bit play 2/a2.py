def OddOccuring(arr):
  res = 0
 
  for element in arr: 
    res = res ^ element
    
    
  return res

arr = []
size = int(input("Enter array size:"))


# (4^4)^4

# 1^2^3^2^4^4^1 = 3

for i in range(0, size):
    num = int(input("Enter your num : "))
    arr.append(num)
    
print(arr)

# print("OddOccuring number is",OddOccuring(arr))





