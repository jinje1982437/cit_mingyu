a,b = input().split()

a = int(a)
b = int(b)

if a-b < 0:
 a = b - a

else:
 a = a - b    
    
print(a)
