
class PersonalCenterPage:
    #网页是基于浏览器打开的，所以不能在一个页面创建浏览器
    #应该把浏览器的使用权，传进来就可以了
    def __init__(self,driver):
        self.driver=driver

    title="我的会员中心 - 道e坊商城 - Powered by Haidao"
