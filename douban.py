import requests
import bs4
import pandas as pd


def openurl(url):

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
    response = requests.get(url,headers=headers)

    return response





def get_movie(response):


    soup = bs4.BeautifulSoup(response.text,"html.parser")

    #电影名

    movies = []
    targets = soup.find_all("div",class_="hd")
    for each in targets:

        try:

            movies.append(each.a.span.text + '\n')







        except:
            continue





    return movies

def get_mark(response):
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 评分

    mark = []
    targets = soup.find_all("span", class_="rating_num")
    for each in targets:

        try:
            mark.append(each.text)





        except:
            continue

    return mark




def main():

    host = "https://movie.douban.com/top250?start="

    movies = []
    mark = []

    for i in range(10):


        url_num = str(25*i)

        url = host + url_num

        response = openurl(url)



        movies.extend(get_movie(response))

        mark.extend(get_mark(response))
        

        pf = pd.DataFrame(movies,columns=['电影'])
        pf.to_csv('movie250.csv',index=False,encoding='utf_8_sig')

        pf = pd.DataFrame(mark, columns=['评分'])
        pf.to_csv('mark250.csv', index=False, encoding='utf_8_sig')

        csv_1 = pd.read_csv('movie250.csv')
        csv_2 = pd.read_csv('mark250.csv')
        out_csv = pd.concat([csv_1, csv_2], axis=1)
        out_csv.to_csv("top250.csv", index=False,encoding='utf_8_sig')






if __name__ == "__main__":
    main()