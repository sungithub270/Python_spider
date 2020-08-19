import urllib.request
import json
import time
import pickle
import csv
import codecs
import xlwt
import random

def data_write_csv(file_name, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")



#  将数据写入新文件
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
        
    f.save(file_path) #保存文件

def text_save(filename, data):#filename为写入TXT文件的路径，data为要写入数据列表.
    file = open(filename,"a")
    for i in range(len(data)):
        s = str(data[i]).replace('[',"").replace(']',"")#去除[],这两行按数据不同，可以选择
        s = s.replace("’","").replace(',',"") +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 




i=10

wang = []


while i>0:

    

    time.sleep(1)
    iplist = ["182.32.250.138:9999","123.54.45.145:9999","113.194.28.165:9999","113.194.28.165:9999"]
    proxy_support = urllib.request.ProxyHandler({"http":random.choice(iplist)})
    opener =urllib.request.build_opener(proxy_support)
    opener.addheaders = [("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")]
    urllib.request.install_opener(opener)

    response=urllib.request.urlopen("https://v1.alapi.cn/api/dog")
    dog = response.read()
    dog = dog.decode("utf-8")
    
    target = json.loads(dog)
    temp = target["data"]["content"]
    
    print(temp)
   


    wang.append(temp)

    i-=1




text_save("ffdog.txt",wang)



"""
file = open("fdog.txt","a")

for i in range(len(wang)):
    s = str(wang[i]).replace("[","").replace("]","")
    s = s.replace("'"," ").replace(",","")
    file.write(s+"\n")

file.close()
print("保存成功")


"""
