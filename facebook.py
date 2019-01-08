# 3
# 3 1
# 1 100 1
# 5 2
# 19 12 3 4 17
# 5 3
# 23 45 11 77 18

# 100 1
# 19 12 17
# 77 18
# from sys import argv
def deletefriend(friendlist=[],popularity=[]):
	# print('called')
	if friendlist==None or popularity==None:
		return []
	deletedfrnd=False
	maxdlt=frndlist[1]
	count=0
	j=0
	p_len=len(popularity)-1
	while j<len(popularity)-1:
		checked=False
		if popularity[j]<popularity[j+1]:
			# popularity[j]=-1
			popularity.remove(popularity[j])
			deletedfrnd=True
			checked=True
			count+=1
		if maxdlt == count:
			break
		if checked:
			j=0
			continue	
		j+=1	
	if not deletedfrnd:
		return popularity[:(len(popularity)-maxdlt)]
	# print(popularity)	
	return popularity

t=int(input("enter no of test cases"))
result=[]
k=0
while k<t:
	print(k)
	frndlist=[int(i) for i in input().split(' ')]
	popularity=[int(z) for z in input().split(' ')]
	# print(frndlist)
	# print(popularity)
	op=deletefriend(frndlist,popularity)
	result.append(op)
	k+=1
# print(result)
# print(len(result))	
for x in result:
	print(x[0:])
	print()					