#要想运行所有的用例，要借用框架来执行
import unittest

# main 主函数
if __name__ == '__main__':
    # defaultTestLoader 默认测试用例加载器：用于寻找符合一定规则的测试用例
    # discover 寻早，发现
    # pattern='*Test.py 执行以任意字符串开头Test为结尾的.py文件
    suite=unittest.defaultTestLoader.discover("./day_5/",pattern='*Test.py')
    #执行suite中的所有测试用例
    # TextTestRunner 文本测试用例运行器，可以运行所有的测试用例，完后返回文本日志
    # TextTestRunner 开头字母是大写的，所以它是一个类，需要实例化对象后再调用 run 方法
    unittest.TextTestRunner().run(suite)