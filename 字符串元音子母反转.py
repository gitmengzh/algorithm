'''
输入一串字符串，然后对其中的元音子母进行反转
eg:  输入  “hello world”  输出 " hollo werld"
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelList=['a','e','i','o','u','A','E','I','O','U']
        list1 = [str(a) for a in s]
        dict1={}
        for i,j in enumerate(s):
            if j in vowelList:
                dict1[i]=j
                list2=list(dict1.keys())
                list3 =reversed(list2)
                for (a,b) in zip(list3,list2):
                    list1[a] = dict1[b]

        print("".join(list1))
s="helloworld"
Test = Solution()
Test.reverseVowels(s)



