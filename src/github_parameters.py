import os


class GithubParamers:
    def __init__(self, args) -> None:
        self.token = args[0]
        self.paras = args[1]
        self.name = args[2]
        self.need_report = False
        self.uid = None
        if len(args) >= 4:
            self.need_report = True
            self.uid = args[3]
        else:
            # 补充获取，防止脚本未更新
            if "WECHAT_UID" in os.environ:
                self.uid = os.environ['WECHAT_UID']
                print(f"更新环境变量uid:{self.uid}")

    def is_effective(self, json_data):
        """判断配置是否启用

        Args:
            json_data (str): 变量配置

        Returns:
            bool: 启用结果
        """
        if "enable" in json_data:
            return json_data["enable"]
        else:
            return True
