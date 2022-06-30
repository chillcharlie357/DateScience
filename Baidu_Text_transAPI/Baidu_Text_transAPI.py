# -*- coding: utf-8 -*-
# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5


# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

# Set your own appid/appkey.


appid = '20220605001238785'
appkey = 'rxl4yPDZgjWm2MznQJwW'

# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`


def get_answer(from_lang, to_lang, query):
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    trans_result = result.get("trans_result")[0].get("dst")
    return trans_result
    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    for i in range(1):
        #ch-1
        from_file = "D:/iCode/2022_Spring/DateScience/TextSimilarityJudge/DataSource/Original/0.txt"
        #en
        to_file = "D:/iCode/2022_Spring/DateScience/TextSimilarityJudge/DataSource/Extended/0out.txt"
        #ch-2
        back_file = "D:/iCode/2022_Spring/DateScience/TextSimilarityJudge/DataSource/Output/0back.txt"
        word_list = []

        with open(to_file, 'w') as w_f:
            w_f.write("")

        with open(from_file, encoding="utf-8") as r_f:
            lines_list = r_f.read()
            lines = lines_list.split("。")
            for line in lines:
                if isinstance(line, str) & (line is not None):
                    translated_words = get_answer("zh", "en", line)
                    if translated_words:
                        with open(to_file, 'a+') as w_f:
                            w_f.write(translated_words+'.\n')

        with open(back_file, 'w') as clear_f:
            clear_f.write("")
        with open(to_file) as read_f:
            lines = read_f.readlines()
            for line in lines:
                if isinstance(line, str) & (line is not None):
                    translated_words = get_answer("en", "zh", line)
                    if translated_words:
                        with open(back_file, 'a+') as write_f:
                            write_f.write(translated_words+'\n')
