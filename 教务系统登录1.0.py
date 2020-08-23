from selenium import webdriver
from PIL import Image,ImageEnhance
import time
import os
import json
import requests
import base64
from io import BytesIO
from sys import version_info


def logn():

    url = 'http://jwgl.wfmc.edu.cn/'

    driver.get(url)#打开登录页
    time.sleep(1)
    driver.maximize_window()#最大化窗口
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="userAccount"]').send_keys(uesrname)#自动输入用户名
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys(password)#自动输入密码
    time.sleep(2)

    picname = "temp"+".png"
    driver.save_screenshot(picname)#截图
    code =  str(pic_crop(picname))#获得验证码

    driver.find_element_by_xpath('//*[@id="RANDOMCODE"]').send_keys(code)#自动输入验证码
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="ul1"]/li[6]/button').click()
    #time.sleep(2)








def pic_crop(picname):#网页截取验证码并上传平台接口识别返回识别结果
    pic = Image.open(picname)
    box = (1390, 534, 1498, 576)
    pic.crop(box).save("crop.png")
    os.remove(picname)

    img_path = "crop.png"
    img = Image.open(img_path)
    result = identify(uname='', pwd='', img=img)#输入http://www.ttshitu.com/申请的用户名和密码
    os.remove(img_path)
    return result


def identify(uname, pwd,  img):

    img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    if version_info.major >= 3:
        b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]

















if __name__ == "__main__":
    driver = webdriver.Chrome()
    date = time.strftime("%Y-%m-%d", time.localtime())
    uesrname = ''#输入教务系统账号
    password = ''#输入教务系统密码
    logn()
