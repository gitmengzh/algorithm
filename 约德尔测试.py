'''
兰博和提莫闲聊之后，回归到了他们的正题，约德尔人的未来。

说起约德尔人的未来，黑默丁格曾经提出了一个约德尔测试，将约德尔人的历史的每个阶段都用一个字符表达出来。(包括可写字符,不包括空格。)。然后将这个字符串转化为一个01串。转化规则是如果这个字符如果是字母或者数字，
这个字符变为1,其它变为0。然后将这个01串和黑默丁格观测星空得到的01串做比较，得到一个相似率。相似率越高,则约德尔的未来越光明。

请问:相似率为多少？

输入:
每组输入数据为两行，第一行为有关约德尔人历史的字符串，第二行是黑默丁格观测星空得到的字符串。
(两个字符串的长度相等,字符串长度不小于1且不超过1000。)
样例输入:
@!%12dgsa
010111100
输出:
输出一行，在这一行输出相似率。用百分数表示。(相似率为相同字符的个数/总个数,精确到百分号小数点后两位。printf("%%");输出一个%。)
样例输出
66.67%
'''
#答案 test.py
s1 = input()
s2 = input()
i = 0
j=0
for str1 in s1:

    if str1.isdigit() or str1.isalpha():
        if s2[i].isalpha() or s2[i].isdigit():
            j += 1
        i+=1
    else:
        if not (s2[i].isalpha() or s2[i].isdigit()):
            j+=1
        i+=1


print(str(round((j/len(s1)),2)*100)+'%')
print("%.2f%%" % ((j/len(s1)) * 100))



ch = input()
x = []
count= 0
for i in  ch:
    if i.isdigit() is True or i.isalpha() is True:
        x.append('1')
    else:
        x.append('0')
num = list(input())
for i ,j in zip(num,x):
    if i == j:
        count +=1
print("%.2f%%"%(count/float(len(ch))*100))