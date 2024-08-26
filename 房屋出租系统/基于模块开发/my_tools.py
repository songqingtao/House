"""
作者:宋庆涛
日期:2024年08月10日
"""

def read_confirm_select():
    """
    确认用户输入的是(Y/N)，不区分大小写
    如果用户输入的不是Y/N，请反复输入

    :return:
    """
    print('请输入你的选择(Y/N),请选择:',end='')
    while True:
        key=input( )
        if key.lower()=='y' or key.lower()=='n':
            break
        else:
            print('输入有误，请重新输入',end='')
    return key.lower()
