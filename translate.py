import requests
import execjs
import json
 
class BaiDuTranslateWeb:
    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            "Cookie": "BAIDUID=ACF8E605F83A0D40EAA235D9BD95E96F:FG=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        self.data = {
            "from": "zh",
            "to": "en",
            "query": None,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": None,
            "token": "a8ab2451768e817c9cb2ef81e92ec784"
        }
 
    def get_baidu_sign(self):
        with open("baidusign.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", self.input)
            return sign
 
    def run(self, text):
        self.input = text
        self.get_baidu_sign()
        self.data["query"] = self.input
        self.data["sign"] = self.get_baidu_sign()
        response = requests.post(url=self.url,data=self.data,headers=self.headers)
        self.result_strs = response.content.decode()
        result_dict = json.loads(self.result_strs)
        if 'trans_result' in result_dict:
            result_dict = result_dict['trans_result']['data'][0] if len(result_dict['trans_result']['data']) > 0 else None
            result_dict = result_dict['result'][0] if len(result_dict['result']) > 0 else None
            result = result_dict[1] if len(result_dict) > 1 else None
            return result
        else:
            return None

if __name__ == '__main__':
    while True:
        baidutranlate = BaiDuTranslateWeb()
        text = input()
        print(baidutranlate.run(text))
        text = input()
        print(baidutranlate.run(text))