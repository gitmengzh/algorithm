'''
输入一串字符串，然后对其中的元音子母进行反转
eg:  输入  “hello world”  输出 " hollo werld"

时间复杂度过大，LeetCode超时
'''
import time


class Solution:
    def reverseVowels(self, s: str) -> str:
        start_time= time.time()
        vowelList=['a','e','i','o','u','A','E','I','O','U']
        list1 = list(s)
        dict1={}
        list2=[]
        list3=[]
        for i,j in enumerate(s):
            if j in vowelList:
                dict1[i]=j
                list2=list(dict1.keys())
                list3 =reversed(list2)
        for (a,b) in zip(list3,list2):
                list1[a] = dict1[b]
        end_time = time.time()
        print("".join(list1),(end_time-start_time))

s="helloworld"
Test = Solution()
Test.reverseVowels(s)



