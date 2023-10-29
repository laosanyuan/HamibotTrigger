import requests


class VxPusher:
    def __init__(self, token, need_report, uid) -> None:
        self.token = token
        self.need_report = need_report
        self.uid = uid

    def report(self, content: str, title='脚本执行失败'):
        if self.need_report:
            webapi = 'http://wxpusher.zjiecode.com/api/send/message'
            data = {
                "appToken": self.token,
                "content": content,
                "summary": title,  # 该参数可选，默认为 msg 的前10个字符
                "contentType": 1,
                "uids": [self.uid, ],
            }
            result = requests.post(url=webapi, json=data)

            print("--- 发送运行错误报告 ---")
            print(f"{title}:{content}")
        else:
            print('没有配置Vxpusher uid，不发送报告')
            print(f"{title}:{content}")
