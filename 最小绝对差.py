'''
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

'''
l1 = [int(i) for i in input().split()]
l1.sort()
l2 = []
l3 = []
if len(l1)<2:
    print('输入有误')
else:



    for i in range(len(l1)-1):

        s1 = l1[i+1]-l1[i]
        l2.append(s1)
    l2.sort()
    r=l2[0]
    for i in range(len(l1) - 1):
        s1 = l1[i + 1] - l1[i]
        if s1 == r:
            l3.append([l1[i],l1[i+1]])

    print(l3)
