import re
import urllib
import pickle
# from googletrans import Translator
# translator = Translator(service_urls=['translate.google.cn'])
from translate import BaiDuTranslateWeb
baidutranlate = BaiDuTranslateWeb()

def load_dict():
    dicts = {}
    with open('data/clean/names.pkl', 'rb') as fin:
        dicts['name'] = pickle.load(fin)
    with open('data/clean/keywords.pkl', 'rb') as fin:
        dicts['keyword'] = pickle.load(fin)
    return dicts

dicts = load_dict()
# common = dicts['name'] & dicts['keyword']
# dicts['name'] = dicts['name'] - common
# dicts['keyword'] = dicts['keyword'] - common
# with open('data/clean/names.pkl', 'wb') as fout:
#     pickle.dump(dicts['name'], fout)
# with open('data/clean/keywords.pkl', 'wb') as fout:
#     pickle.dump(dicts['keyword'], fout)
# print(dicts['name'] & dicts['keyword'])

def prepocessing(ori):
    # Return: Continue?, text, 'name'/'keyword'/None
    # 1. 任意语言转英文
    # text = translator.translate(text, src='auto', dest='en').text
    text = baidutranlate.run(ori)
    # 2. 转小写
    text = text.lower()
    # 3. 查表
    for key in dicts:
        if key == 'name':
            temp = text.split()
            if ori != text and len(temp) == 2:
                temp = '%s %s' % (temp[1], temp[0])
                if temp in dicts[key]:
                    return False, temp, key
        if text in dicts[key]:
            return False, text, key
    return True, text, None

if __name__ == "__main__":
    while True:
        print(prepocessing(input()))
