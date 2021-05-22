 

x1 = y1 = z1 = 0

for _ in range(int(input())):
    x, y, z = map(int, input().split())
    
    x1 += x
    y1 += y
    z1 += z
    
if(x1 == 0 and y1 == 0 and z1 == 0):
    print("YES")
else:
    print("NO")