'''
你知道行编辑器吗？不知道也没关系，现在我会告诉你：
 1.如果你收到一个

输入
第一行是一个整数T，代表有T组数据。
每组数据的开始时一个字符串，字符串长度小于100，每个字符一定是(
样例输入
3
whli##ilr#e(s#*s)

outcha@putchar(*s=#++)

returnWA##A!!##C

输出
每组数据输出一行经过行编辑器编辑过的字符串，具体可以看样例。

样例输出
while(*s)

putchar(*s++)

returnAC
思路：这种题考查的还是观察规律，通过观察，#字符会删除它和它前边的字符，@字符会删除它前边所有字符
'''

while True:
    n = int(input())
    for i in range(n):
        str1 = input()
        s1 = ''
        for s in str1:

            if s !='@' and s != '#':
                s1 += s
            elif s == '@':
                s1=''
            else:
                s1=s1[:-1]
        print(s1)

    break
