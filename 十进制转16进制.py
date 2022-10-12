import os
os.system("cls")

decimal_num = int(input("请输入十进制数N："))
process_num = int(bin(decimal_num),2)
temp_num = hex(process_num)
output_display = temp_num[2:]
print("对应的十六进制数是：{}".format(output_display))