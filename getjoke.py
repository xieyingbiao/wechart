# -- coding:utf-8 --
import requests
from random import choice

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}
def getjoke():
    '''
    获取一段笑话
    :return:
    '''
    user_url = ' https://www.mxnzp.com/api/jokes/list/random'
    resp = requests.get(user_url, headers=headers)
    every_msg=choice(resp.json().get('data')).get('content')
    return every_msg
if __name__ == '__main__':
    print(getjoke())

