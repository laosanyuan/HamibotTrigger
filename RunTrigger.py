import sys
import requests
import json


def run(token, script, robots):
    print(f"script:{script}")
    print(f"robots:{robots}")

    url = f"https://api.hamibot.com/v1/scripts/{script}/run"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "robots" : robots
    }
    response = requests.post(url, headers=headers, json=data)

    print("HTTP 状态码:", response.status_code)
    print("响应内容:", response.text)


if __name__ == "__main__":
    args = sys.argv[1:]  # 排除脚本名称
    token =  args[0]
    paras = args[1]
    name = args[2]

    try:
        data = json.loads(paras)
    except json.JSONDecodeError:
        print("解析参数失败，可能是Hamibot参数格式设置错误")
        sys.exit(1)

    matching_key = next((key for key in data if key.upper() == name), None)

    if matching_key is not None:
        value = data[matching_key]
        run(token, value["script"], value["robots"])
    else:
        print(f"没有获取到 '{name}' 对应的参数")