import math
'''
n = int(input())
for m in range(n):
    s = input()
    rlt = 1
    sdi = 0
    for i in range(len(s)):
        t = s[i]
        s0 = s[i:]
        n = 0
        for j in s0:
            if t > j:
                n += 1
        rlt += math.factorial(len(s) - i - 1) * n
    print(rlt)

'''

import time
start_time = time.time()
a=0
b=0
c=0
for a in range(1001):
    for b in range(1001):
        c=1000-a-b
        if  a**2 +b**2 == c**2 and a+b>c :
             print("a b c:，%d %d %d" % (a,b,c))

end_time= time.time()

print("time:%d" % (end_time-start_time))
