import urllib.request
import urllib.parse
import json

content = input("请输入要翻译的内容:")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

date = {}
date["i"] = content
date["from"] = "AUTO"
date["to"] = "AUTO"
date["smartresult"] = "dict"
date["client"] = "fanyideskweb"
date["salt"] = "15971398878642"
date["sign"] = "c61e84f93be8c5789dbe2bd66830c682"
date["lts"] = "1597139887864"
date["bv"] = "9ef72dd6d1b2c04a72be6b706029503a"
date["doctype"] = "json"
date["version"] = "2.1"
date["keyfrom"] = "fanyi.web"
date["action"] = "FY_BY_CLICKBUTTION"

date = urllib.parse.urlencode(date).encode("utf-8")


response = urllib.request.urlopen(url,date)


html = response.read().decode("utf-8")


target = json.loads(html)
print("翻译结果:%s" % target["translateResult"][0][0]["tgt"])
