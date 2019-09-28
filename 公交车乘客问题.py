'''
一个公交车经过n个站点，乘客从前门上车，从后门下车。

现在统计了在第i个站，下车人数a[i]，以及上车人数b[i]。


问公交车运行时候车上最多有多少乘客

输入:
第一行读入一个整数n(1 <= n <= 100)，表示有n个站点

接下来n行，每行两个数值，分别表示在第i个站点下车人数和上车人数

样例输入:
4
0 3
2 5
4 2
4 0

输出
每组输出车上最多的乘客数目
样例输出:
6

while True:
    n =int(input())
    maxnum=0
    num =0

    for m in range(n):
        l1 = [int(i) for i in input().split(' ')]
        num = num+l1[1]-l1[0]
        if num>maxnum:
            maxnum=num
    print(maxnum)'''

while 1:
    n = int(input())
    s,o = 0,0
    for i in range(n):
        a,b = map(int, input().split())
        s += b-a
        if s > o:
             o = s
    print(o)
    break


