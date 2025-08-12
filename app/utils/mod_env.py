# _*_ coding:utf-8 _*_
# Copyright (C) 2024-2024 shiyi0x7f,Inc.All Rights Reserved
# @Time : 2024/12/4 下午9:52
# @Author: shiyi0x7f
from dotenv import load_dotenv
import os
def get_env():
    """
    获取应用程序环境变量
    
    Returns:
        str: 环境名称，统一返回小写字符串
    """
    try:
        load_dotenv()
        env = os.getenv('APP_ENV')
        if env and isinstance(env, str):
            return env.lower()
        return "prod"  # 默认返回生产环境
    except Exception:
        return "prod"  # 出现异常时返回默认生产环境
if __name__ == '__main__':
    env = get_env()
    print(env)