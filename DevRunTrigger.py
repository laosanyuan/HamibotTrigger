import sys
import json
import src.script_runner as runner
from src.github_parameters import GithubParamers
from src.vxpusher import VxPusher
import src.config as config

if __name__ == "__main__":
    args = sys.argv[1:]  # 排除脚本名称

    github_parameters = GithubParamers(args)
    pusher = VxPusher(
        config.user_config['wxpusher_token'], github_parameters.need_report, github_parameters.uid)

    try:
        data = json.loads(github_parameters.paras)
    except json.JSONDecodeError:
        pusher.report(f"解析参数失败，可能是Hamibot参数格式设置错误\n:{github_parameters.paras}")
        sys.exit(1)

    matching_key = next((key for key in data if key.upper()
                        == github_parameters.name.upper()), None)

    if matching_key is not None:
        value = data[matching_key]
        if github_parameters.is_effective(value):
            result = runner.run_dev_script(
                github_parameters.token, value["script"], value["robots"])
            if result.ok:
                print('脚本调用成功')
            else:
                # 调用失败，推送消息
                pusher.report(
                    f"{result.status_code}\n{result.content}", 'Hamibot接口调用异常')
        else:
            print("当前配置没有启用，本次不执行脚本")
    else:
        pusher.report(f"没有获取到 '{github_parameters.name}' 对应的参数，请检查配置是否正确")
