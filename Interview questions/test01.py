# _*_ coding:utf-8 _*_
__author__ = 'tomtao'
__date__ = '2019/6/18 17:04'

#(1)编程实现对一个元素全为数字的列表，求最大值，最小值
'''
a = [11,222,23,4,12]
print("the max:",max(a))
print("the min:",min(a))
'''

#(2)统计字符串中，各个字符的个数，比如 “hello world”，字符串统计的结果为：h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''a = "hello world"
b = []#用于从a中取出字符
j = 0
print("统计结果为:%s 中各个字符出现的次数如下:"%a)
for i in a:#遍历字符
    if j<len(a):
        if i in b:#遇到重复的字符就跳过
            continue
        else:
            b.append(i)
            if b[j].isalpha():#判断是否为字母
                print b[j],a.count(i)
        j += 1
'''

#(3)编写程序完成一个路劲的组装，先提示用户多次输入路径，最后显示一个完整的路径，比如/home/python/ftp/test
a = 1
ss = ""
while a<5:
    s = input("请输入路径:").strip()
    ss = ss+'/'+s
    a += 1
    print(ss)

