import math
from itertools import permutations
def arrangedWays(str=''):
	dict={}
	l=[]
	r=1
	for x in str:
		dict[x]=dict.get(x,0)+1
	for v in dict.values():
		if v>1:
			l.append(v)
	for x in l:
		r*=math.factorial(x)		
	r= int(math.factorial(len(str))/r)
	finallist=[]
	perm=[''.join(x) for x in permutations(str)]
	for x in perm:
		if x not in finallist:
			finallist.append(x) 
	return finallist



s='aabbcadad'
dict={}
for x in s:
	dict[x]=dict.get(x,0)+1
print(dict)
str=''
odd_str=''
for k,v in dict.items():
	if v%2==0:
		# it is even
		str +=k*int((v/2))
	else:
		odd_str += k	
print(str)
print(arrangedWays(str))
l=arrangedWays(str)
for x in l:
	print(x+odd_str+x[::-1])


