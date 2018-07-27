# File: 阶乘.py
# 这是一个用来计算阶乘的小程序
def main():
    print('这是一个用来进行阶乘计算的程序')
    n = eval(input('请输入需要阶乘的数字:'))
    fact = 1
    for factor in  range(2 , n+1):
        fact = fact * factor
    print('阶乘', n , '的值是', fact)
    input('按 <Enter> 退出')
main()
