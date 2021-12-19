list = input().split()

a = int (list[0])
b = int (list[1])

print(a*(b%10))
print (a*((b%100)%10))
print (a*(b//100))
print (a*b)