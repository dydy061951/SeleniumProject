#读取csv文件
#1.导入csv包，csv是python语言内置的包，所以直接import导入即可
import csv

#2.想要读取文件的信息，首先要知道文件的存放路径
#字符串前面加一个字符r,表示反斜杠是普通字符，不看做转义字符
path=r"D:\DY\PycharmProjects\SeleniumProject\data\member_info.csv"

#3.要想读文件的内容，首先要通过路径打开文件
# 打开文件的关键字为 open
file=open(path,'r')  #打开文件，为只读方式，接收返回给一个变量

#4.通过csv代码库，读取csv格式的内容
data_table=csv.reader(file)    #csv读取打开的文件，返回个数据列表

#5.遍历data_table,分别打印出来每一行数据
for row in data_table:
    print(row)