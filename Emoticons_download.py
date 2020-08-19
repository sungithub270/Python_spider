import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()

    print(url)



    return html


def find_filename(url):

    html = url_open(url).decode("utf-8")

    filename_is = []

    alll = html.find('<div class="jss3"><img src=')

    a = html.find("alt",alll,alll+255) + 5
    b = html.find("的表情包",alll,alll+255) - 1

    filename_is.append(html[a:b])

    for each in filename_is:
        print(each)

    return filename_is






def find_imgs(url):

    html = url_open(url).decode("utf-8")

    img_addrs = []

    a = html.find('<div class="jss3"><img src=') + 28
    b = html.find("alt",a) - 2


    img_addrs.append(html[a:b])

    for each in img_addrs:
        print(each)


    return img_addrs


def save_imgs(folder,img_addrs):



   for each in img_addrs:

       name = str(find_filename(page_url)).replace("[","").replace("]","").replace("'","")


       
       filename = name + ".gif"
       with open(filename,"wb") as f:
           img = url_open(each)
           f.write(img)


    
    













def download(folder="bqb",pages=int(input("请输入要爬取的数量："))):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://www.dbbqb.com/detail/"


    for i in range(pages):

        page_num = pages - i 

        global page_url
        page_url = url + str(page_num) + ".html"

        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)
    

    
if __name__ == "__main__":
    download()
