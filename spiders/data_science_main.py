import requests
if __name__ == '__main__':
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    #step_1:指定url:封装到字典中
    url = 'http://www.sogou.com/web'
    keyword = input('enter a word:')
    #step_2:发起请求,请求的url是携带参数的，且对参数进行了处理
    param = {
        'query': keyword
    }
    reponse = requests.get(url = url,params=param,headers=headers)
    #get方法返回一个响应对象
    #step_3:获取响应数据,text返回的是字符串形式的响应数据
    page_text = reponse.text
    print(page_text)
    #step_4:持久化存储
    filename = keyword + '.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")