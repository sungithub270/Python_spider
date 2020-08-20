import requests
import bs4
import json

def get_comment(url):

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}

    data = {'params':'bCx7xhXpfTSFIi3jW44/2IvtpEkgo5JXdaqvUlDpwCr8QuhHfibYoLHCKbDpRNgYH+/HzWqhna4cX2tuHzbw3udrCPmpsPHT1IfAIpj7gMml+gC8hm59rf7zkaUoS2QL1cXHs6kL3jEr0T5baEXyrUL1hDF6vZn/o70rCk1sbFM9KJSXJGhE0X99E424PL1WtmkEoWw/h5vzBaJZTk5FsSm2f7R3XJNKoP2R2DgYL4j8wktX5bi/hw3yEU5jUWwd4Lxq5uySjmCcm10Godrb/q/+PSorjGtjaHTeK578dnY=',
            'encSecKey':'6a4e3e6f9e7ef64fe7700a06b3c1d9bb7527ce06ccd875b8ffe709300ca5e177fa78190ad0eda866141dbe9aa68d89899bfebce42a4185e1daac92d8d5ef424688a4cb2a83cd798c87602446104932c917a76b394995387bda4681b301900607afa06b7e04c36a02c27c6d692bcc6447f3ed4522e2d555cdf05f4036b6c3a5da'}


    res = requests.post(url,headers=headers,data=data)

    commentdict = json.loads(res.text)

    result = []

    for i in range(5):


        nickname = commentdict['hotComments'][i]['user']['nickname']

        #print(nickname)


        content = commentdict['hotComments'][i]['content']

        #print(content)

        result.append(nickname +":"+ content)

    print(result)

















def main ():

    id = input('请输入歌曲ID：')

    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(id)


    get_comment(url)



















if __name__ == '__main__':
    main()