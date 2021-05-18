s = input()

zeros = 0
ones = 0
for i in range(len(s)):
    if(s[i] == "0"):
        zeros += 1
        if(ones < 7):
            ones = 0
    else:
        ones += 1
        if(zeros < 7):
            zeros = 0
    	
if (zeros >= 7 or ones >= 7):
	print("YES")
else:
	print("NO")