import requests


def run(token, script, robots, type_str):
    print(f"script:{script}")
    print(f"robots:{robots}")

    url = f"https://api.hamibot.com/v1/{type_str}/{script}/run"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "robots": robots
    }
    response = requests.post(url, headers=headers, json=data)

    print("HTTP 状态码:", response.status_code)
    print("响应内容:", response.text)
    return response


def run_script(token, script, robots):
    """运行发布脚本

    Args:
        token (_type_): _description_
        script (_type_): _description_
        robots (_type_): _description_
    """
    return run(token, script, robots, 'scripts')


def run_dev_script(token, script, robots):
    """运行调试脚本

    Args:
        token (_type_): _description_
        script (_type_): _description_
        robots (_type_): _description_
    """
    return run(token, script, robots, 'devscripts')
