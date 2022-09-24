#导入相关模块
import os
import time

os.system('cls')
#清屏
def cleanup():
    os.system("cls")

#十进制到二进制
def decimal_to_binary():
    input_number = input("输入一个十进制数字:")
    try:
        process_num = int(input_number)
        output_number = bin(process_num)
        print(output_number)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")
        

#二进制到十进制
def binary_to_decimal():
    input_number = input("输入一个二进制数字:")
    try:
        process_num = int(input_number,2)
        print(process_num)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")
#八进制到二进制
def octal_to_binary():
    input_number = input("输入一个八进制数:")
    try:
        process_num = int(input_number,8)
        output_number = bin(process_num)
        print(output_number)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")

#二进制到八进制
def binary_to_octal():
    input_number = input("输入一个二进制数：")
    try:
        process_num = int(input_number,2)
        output_number = oct(process_num)
        print(output_number)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")

#二进制到16进制
def binary_to_Hexadecimal():
    input_number = input("输入一个二进制数：")
    try:
        process_num = int(input_number,2)
        output_number = hex(process_num)
        print(output_number)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")

#16进制到二进制
def Hexadecimal_to_binary():
    input_number = input("输入一个16进制数:")
    try:
        process_num = int(input_number,16)
        output_number = bin(process_num)
        print(output_number)
        #input('按任意键结束')
    except ValueError:
        print("请重新输入，程序将关闭")
        time.sleep(2)
        os.system("exit")

#while True:
print("请选择你要用的功能")
print("A.十进制转二进制\nB.二进制转十进制\nC.8进制转二进制\nD.二进制转8进制\nE.二进制转16进制\nF.16进制转二进制")
user_choice = input("你的选择是：")
if user_choice == 'A' or user_choice == 'a':
    decimal_to_binary()
elif user_choice == 'B' or user_choice == 'b':
    binary_to_decimal()
elif user_choice == 'C' or user_choice == 'c':
    octal_to_binary()
elif user_choice == 'D' or user_choice == 'd':
    binary_to_octal()
elif user_choice == 'E' or user_choice == 'e':
    binary_to_Hexadecimal()
elif user_choice == 'F' or user_choice == 'f':
    Hexadecimal_to_binary()
else:
    print("请重新选择，程序将关闭")
    time.sleep(2)
    os.system("exit")
