import urllib.request
import random


url = "http://myip.kkcha.com/"

iplist = ["182.32.250.138:9999","123.54.45.145:9999","113.194.28.165:9999","113.194.28.165:9999"]

proxy_support = urllib.request.ProxyHandler({"http":random.choice(iplist)})

opener =urllib.request.build_opener(proxy_support)
opener.addheaders = [("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")]
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)


html = response.read().decode("utf-8")

print(html)
