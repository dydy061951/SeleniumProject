def printHW():
    print("hello,world")

# main if 语句，只有直接执行当前文件的时候才会被执行，如果出现main if，那么只执行main if 上面的语句，下面的不执行
# 所以一般 main if 语句用来对当前文件做单元测试
if __name__=="__main__":
    printHW()