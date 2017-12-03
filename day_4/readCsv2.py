'''
1.之前的 readcsv 不能被其他的测试用例调用，所以应该给这段代码封装到一个方法里
2.每个测试用例的路径path不同，所以path应该要作为参数传入到方法内
4.打开一个文件但是并没有关闭，最终可能会造成内存泄露
'''
import csv
import os

def read(filename):
    #所有重复的代码均应放到方法里
    current_file_path = os.path.dirname(__file__) #获取当前文件的系统目录
    # 我们真正想要的路径是csv文件的路径     replace: 改变路径的方法
    csvpath = current_file_path.replace("day_4", "data/"+filename)
    #file=open(csvpath,"r")
    #with语句是一个代码块，代码块中的内容都要进行缩进
    #with代码块可以自动关闭with中声明的变量file
    #因为file文件一旦被关闭，里面的数据也会随着消失，所以要单独声明一个列表result来保存里面的数据
    result=[]  #声明一个列表，接收遍历出来返回的值
    with open(csvpath,"r")as file: #打开一个文件并命名为file
        data_table=csv.reader(file)
        for row in data_table:
            result.append(row)    #append: 列表追加内容的方法
        return result
    #如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能正常运行，那么file.close()也不能执行，这是文件仍然不能关闭
    #file.close()
    #应该用 with...as... 语句实现文件的关闭,with代码块可以自动关闭with中声明的变量file

if __name__ == '__main__':
    # read(r"D:\DY\PycharmProjects\SeleniumProject\data\member_info.csv")
    #3.path这个路径是个绝对路径，每个人放置配置文件的位置不统一，所以应该在代码中，通过当前代码文件的路径，根据相对位置，找到csv文件
    #首先找到当前文件路径，导入os包
    # os是操作系统,path是路径,dir是directory目录,__file__是python的内置变量，指的是当前文件
    # current_file_path=os.path.dirname(__file__)   #获取当前文件的系统目录
    # print(current_file_path)
    #我们真正想要的路径是csv文件的路径     replace: 改变路径的方法
    # csvpath=current_file_path.replace("day_4","data/member_info.csv")
    # print(csvpath)
    member_info=read("member_info.csv")
    print(member_info)
    # for roww in member_info:
    #     print(roww[0])

    #5.读数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值，方便进一步的调用
