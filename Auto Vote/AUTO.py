import sys
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
import os

#重启函数
def restart_program():
  """Restarts the current program.
  Note: this function does not return. Any cleanup action (like
  saving data) must be done before calling this function."""
  print('ready to restart program......')
  python = sys.executable
  os.execl(python, python, *sys.argv)

#调整好chromedriver的位置
driver = webdriver.Chrome("D:\project\Python\chromedriver.exe")
sleep_time_2 = random.randint(0,1)
sleep_time_3 = random.randint(5,8)
driver.get("https://form.southcn.com/form-pc/index.html#/vote/62c7e9b63e500c063c056f5c/6342ca9dc04ff864c6066033")
#根据网速调整等待时间
time.sleep(10)
if driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[3]/button/span'):
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[3]/button/span').click()
    os.system("cls")
    print("如果有机器人验证请验证")
    print("请在{}秒内完成验证".format(sleep_time_3))
    time.sleep(sleep_time_3)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/label[2]/span[2]').click()
    time.sleep(sleep_time_2)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/button/span').click()
    time.sleep(sleep_time_2)
while True:
  #重启等待时间按情况来定
  #time.sleep(sleep_time_3)
  os.system("cls")
  restart_program()