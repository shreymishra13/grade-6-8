num1 = 10 #1010
num2 = 4  #0100
    #and  #0000
    #or|  #1110 =>  14 
    #not~ #0101
    
 #1010 ^   #0100
    #xor^ 1110
    
    
    # 1
    # 1<<1
    # 10
    # 1<<3
    #   10 = 2
    #  100 = 4
    # 1000 = 8
    
    # 14>>2
    # 1110>>2
    # 11 = 3
          
          

# print(num1 & num2)
# print(num1 | num2)
# print(~num1)
# print(num1 ^ num2)
print(1<<3)
print(14>>2)
