import math
def isValid(s):
	dict={}
	for x in s:
		dict[x]=dict.get(x,0)+1
	print(dict)
	list=[int(v) for v in dict.values()]
	print(list)
	i=0
	while i<len(list)-1:
		if list[i]==list[i+1]:
			i+=1
			continue
		else:
			if list[i+1]>list[i] and list[i+1]-list[i]==1:
				l=list[i+2:]
				for x in l:
					if x!=list[i]:
						return 'NO'
				return 'YES'
			else:
				if list[i]-list[i+1]==1 or list[i+1]>=1:
					# print('ggggggg')
					l=list[i+2:]
					print(l)
					for x in l:
						if x!=list[i]:
							return 'NO'
					return 'YES'
				return 'NO'	
	return 'YES'		


s=input()
result=isValid(s)
print(result)

