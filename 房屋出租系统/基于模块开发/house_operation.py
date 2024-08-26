
from my_tools import *
houses_list = [
    {
        "id": 1,
        "name": "tim",
        "phone": "113",
        "address": "海淀",
        "rent": 800,
        "state": "未出租"
    }
]

id_counter=1

def find_by_id(find_id):
    for house in houses_list:
        if house['id']==find_id:
            return house


def add_house():
    print('添加房屋'.center(32, '='))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("租金："))
    state = input("状态：")
    global id_counter
    id_counter+=1
    house={
        "id":id_counter,
        "name":name,
        "phone":phone,
        "address":address,
        "rent":rent,
        "state":state
    }
    houses_list.append(house)
    print('添加房屋成功'.center(32, '='))

def exit_sys():

    choice=read_confirm_select()
    if choice =='y':
        return True
    else:
        False


def find_house():

    print('查找房屋信息'.center(32, '='))

    pass




def del_house():
    print('删除房屋信息'.center(32, '='))
    del_id=int(input("请输入要删除的房屋编号(-1退出)："))
    if del_id==-1:
        print('退出删除房屋信息'.center(32, '='))
        return
    # while True:
    #     key=input('请输入你的选择(Y/N),请选择:')
    #     if key.lower()=='y' or key.lower()=='n':
    #         break
    choice=read_confirm_select()


    if choice=='y':
        house=find_by_id(del_id)
        if house:
            houses_list.remove(house)
            print('删除房屋成功'.center(32, '='))
        else:
            print('房屋编号不存在,删除失败...')
    else:
        print('房屋编号不存在,删除失败...'.center(32, '='))














def list_houses():

    print('房屋列表'.center(60,'='))

    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（未出租/已出租）")
    for house in houses_list:
        for value in house.values():
            print(value, end='\t\t')
        print()
    print('房屋列表显示完毕'.center(60, '='))









def main_menu():
    """

    :return:
    """
    print()
    print('房屋出租系统菜单'.center(32, '='))
    print('\t\t\t1 新增房源')
    print('\t\t\t2 查找房屋')
    print('\t\t\t3 删除房屋信息')
    print('\t\t\t4 修改房屋信息')
    print('\t\t\t5 房屋列表')
    print('\t\t\t6 退出')




