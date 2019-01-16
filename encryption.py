import math
s='if man was meant to stay on the ground god would have given us roots'
t=s.replace(' ','')
# t='iffactsdontfittotheorychangethefacts'
t='haveaniceday'
print(len(t))
l=[]
print(math.sqrt(len(t)))
temp=math.sqrt(len(t))
row=int(math.sqrt(len(t)))
if temp>row:
	col=row+1
else:
	col=row	
for x in range(row):
	# print(t[:col])
	l.append(t[:col])
	t=t[col:]
print(l)
i=0
j=0
s=''
while i<col:
	while j<row:
		s+=l[j][i:i+1]
		j+=1
	j=0
	i+=1
	print(s,end=' ')
	s=''	
	