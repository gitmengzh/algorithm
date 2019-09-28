
try:
	list1 = [abs(int(i)) for i in input().split(' ')]
	if list1[0]+list1[1]<=list1[2] and (list1[2]-list1[0]-list1[1])%2==0:
		print('yes')
	else:
		print('yes')
except:
	print("input error!")