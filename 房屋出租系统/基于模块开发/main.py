"""
作者:宋庆涛
日期:2024年08月09日
"""

from house_operation import *


def main():
    while True:
        main_menu()
        key=input("请输入您的选择(1-6):")
        if key in ['1','2','3','4','5','6']:
            if key=='1':
                add_house()
            elif key=='2':
                print('输入了2-后面我们会处理逻辑')
            elif key=='3':
                del_house()
            elif key=='4':
                print('输入了4-后面我们会处理逻辑')
            elif key=='5':
                list_houses()
            elif key=='6':
                if exit_sys():
                    break

        else:
            print("输入有误，请重新输入")


if __name__ == '__main__':
    main()
    print('您退出了程序欢迎下次使用')


