# usename.py
#   Simple  string pricessing program to generate usernaes.
#   这是一个简单的字符串处理程序，用于生成用户名。

def main():
    # 打印改程序生成计算机用户名 ‘\n’为输出跳过产生一个空白行。
    print('This program generates computter usernames.\n')
    # 等待用户输入名字
    fiest = input('please enter your first name(all lowercase): ')
    # 等待用户输入姓氏
    last = input('please enter your last name(all lowercase): ')
    # 对用户输入进行切片并打印
    uname = fiest[0] + last[:7]
    #输入字串符unanme结果
    print('your username is:',uname)

main()
