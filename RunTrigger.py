import sys
import requests


def run(token, script, robots):
    url = f"https://api.hamibot.com/v1/scripts/{script}/run"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        robots
    }
    response = requests.post(url, headers=headers, json=data)

    print("HTTP 状态码:", response.status_code)
    print("响应内容:", response.text)


if __name__ == "__main__":
    args = sys.argv[1:]  # 排除脚本名称
    token = args[0]
    script = args[1]
    robots = args[2]

    run(token, script, robots)
