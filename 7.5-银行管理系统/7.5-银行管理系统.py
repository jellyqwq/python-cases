import random
#bug
"""
Exception ignored in: <function Bank.__del__ at 0x000001F474FD16C0>
TypeError: Bank.__del__() missing 1 required positional argument: 'del_options'
"""


class Bank():
    __ad_account = 'admin'
    __ad_password = '123456'
    
    # 对象被释放时的显示
    def __del__(self, del_options=''):
        self.del_options = del_options
        if self.del_options == False:
            print('管理员密码错误,进入系统失败')
        else:
            print('系统已退出')
    
    # 对象创建时的操作
    def __init__(self, ad_account='', ad_password=''):
        self.ad_account = ad_account
        self.ad_password = ad_password
        if self.ad_account == self.__ad_account and self.ad_password == self.__ad_password:
            self.switch = True
            print('进入系统成功')
        else:
            self.switch = False
            self.__del__(del_options=False)
    
    #暂时先用类内部的列表
    #类属性
    li_name = []            #名字
    li_id_number =[]        #身份证
    li_phonenumber = []     #电话号码
    li_account = []         #账号
    li_password = []        #密码
    li_money = []           #钱
    __count = 2             #定义私有属性账户密码容错次数
    __mistake_password_count = {}         #定义私有属性账户冻结计数字典{账号:密码错误次数}


    # 定义开户方法
    def open_account(self,name='',id_number='', phonenumber='', money='', password=''):
        #当任何一个信息缺少时都不可开户
        if name == '' or id_number == '' or phonenumber == '' or money == '' or password == '':
            print('请输入完整的信息')
        else:
            self.li_name.append(name)                   #存名字
            self.li_id_number.append(id_number)         #存身份证
            self.li_phonenumber.append(phonenumber)     #存电话号码
            self.li_password.append(password)           #存密码
            self.li_money.append(money)                 #预存的钱

            while True:
                #生成随机的6位数整数
                temp_account = str(random.randint(100000,999999))
                #如果这个6位数的账户不在账号列表中
                if temp_account not in self.li_account:
                    #向账号列表写入该账号
                    self.li_account.append(temp_account)
                    print('您的账户是:%s' % temp_account)
                    #写入完成后退出循环
                    break
                #生成6位数的账号在账号列表中已存在
                else:
                    #继续执行循环获取6位数的账号
                    continue

# importance:冻结的步骤单独出一个方法
    
    # 定义查询功能方法
    def inquiry(self, inquiry_account='', inquiry_password=''):
        #判断账号是否在账号列表中
        if inquiry_account not in self.li_account:
            print('该账户不存在')
        else:
            # 获取账户的账号索引
            inquiry_account_index = self.li_account.index(inquiry_account)
            # 当账户处在冻结字典中
            if self.li_account[inquiry_account_index] in self.__mistake_password_count.keys():
                #如果该账户冻结计数为零,则进行下面的操作
                if self.__mistake_password_count[inquiry_account] == 1:
                    print('错误次数过多,账户%s已冻结' % inquiry_account)
                # 冻结字典中已存在该账户,且未冻结
                else:
                    self.__mistake_password_count[inquiry_account] -= 1
                    print('密码错误,还有%d次机会' % self.__mistake_password_count[inquiry_account])
            # 当账号和密码都对上时
            elif inquiry_password == self.li_password[inquiry_account_index]:
                # 当该账户存在冻结次数且未被冻结时
                if self.li_account[inquiry_account_index] in self.__mistake_password_count.keys() and self.__mistake_password_count[inquiry_account] > 0:
                    # 从冻结字典中删除该成功进入的账户
                    self.__mistake_password_count.pop(inquiry_account)
                    print('账户%s还有%s元' % (self.li_account[inquiry_account_index],self.li_money[inquiry_account_index]))
                else:
                    print('账户%s还有%s元' % (self.li_account[inquiry_account_index],self.li_money[inquiry_account_index]))
            # 账号对不上密码时,触发账号冻结计数,若该输错密码的账号不在冻结计数字典内,则向字典中添加
            elif self.li_account[inquiry_account_index] not in self.__mistake_password_count.keys():
                self.__mistake_password_count[inquiry_account] = self.__count
                print('密码错误,还有%d次机会' % self.__mistake_password_count[inquiry_account])
            # 容错
            else:
                pass

    # 定义取款方法
    def withdraw(self):
        #判断账号是否在账号列表中
        if inquiry_account not in self.li_account:
            print('该账户不存在')
        else:
            # 获取账户的账号索引
            inquiry_account_index = self.li_account.index(inquiry_account)
            # 当账户处在冻结字典中
            if self.li_account[inquiry_account_index] in self.__mistake_password_count.keys():
                #如果该账户冻结计数为零,则进行下面的操作
                if self.__mistake_password_count[inquiry_account] == 1:
                    print('错误次数过多,账户%s已冻结' % inquiry_account)
                # 冻结字典中已存在该账户,且未冻结
                else:
                    self.__mistake_password_count[inquiry_account] -= 1
                    print('密码错误,还有%d次机会' % self.__mistake_password_count[inquiry_account])
            # 当账号和密码都对上时
            elif inquiry_password == self.li_password[inquiry_account_index]:
                # 当该账户存在冻结次数且未被冻结时
                if self.li_account[inquiry_account_index] in self.__mistake_password_count.keys() and self.__mistake_password_count[inquiry_account] > 0:
                    # 从冻结字典中删除该成功进入的账户
                    self.__mistake_password_count.pop(inquiry_account)
                    print('账户%s还有%s元' % (self.li_account[inquiry_account_index],self.li_money[inquiry_account_index]))
                else:
                    print('账户%s还有%s元' % (self.li_account[inquiry_account_index],self.li_money[inquiry_account_index]))
            # 账号对不上密码时,触发账号冻结计数,若该输错密码的账号不在冻结计数字典内,则向字典中添加
            elif self.li_account[inquiry_account_index] not in self.__mistake_password_count.keys():
                self.__mistake_password_count[inquiry_account] = self.__count
                print('密码错误,还有%d次机会' % self.__mistake_password_count[inquiry_account])
            # 容错
            else:
                pass
    #存款
    #转账
    #锁定

    #解锁
    
    #存盘

    #退出
    def bank_quit(self, ad_account='', ad_password=''):
        if ad_account == self.__ad_account and ad_password == self.__ad_password:
            return True
        else:
            return False
    
#交互操作
while True:
    ad_account = input('请输入管理员账户:')
    ad_password = input('请输入管理员密码:')
    bank = Bank(ad_account=ad_account, ad_password=ad_password)   #实例化对象
    break

while bank.switch:
    print('1.开户')
    print('2.查询')
    print('3.取款')
    print('4.存款')
    print('5.转账')
    print('6.锁定')
    print('7.解锁')
    print('8.存盘')
    print('9.退出')
    choice = input('请输入操作:')
    
    #开户
    if choice == '1':
        print('进入开户系统,输入/b退出')
        while True:
            name = input('请输入姓名:')
            if name == '/b':
                break
            id_number = input('请输入身份证号:')
            if id_number == '/b':
                break
            phonenumber = input('请输入电话号码:')
            if phonenumber == '/b':
                break
            money = input('请输入预存金额:')
            if money == '/b':
                break
            password = input('请输入密码:')
            if password == '/b':
                break
            bank.open_account(name=name, id_number=id_number, phonenumber=phonenumber, money=money, password=password)
    
    #查询
    elif choice == '2':
        print('进入查询系统,输入/b退出')
        while True:
            inquiry_account = input('请输入卡号:')
            if inquiry_account == '/b':
                break
            inquiry_password = input('请输入密码:')
            if inquiry_password == '/b':
                break
            else:
                bank.inquiry(inquiry_account=inquiry_account, inquiry_password=inquiry_password)

    #退出
    elif choice == '9':
        ad_account = input('请输入管理员账户:')
        ad_password = input('请输入管理员密码:')
        back_value = bank.bank_quit(ad_account=ad_account, ad_password=ad_password)
        if back_value == True:
            break
        elif back_value == False:
            continue

    #容错
    else:
        pass