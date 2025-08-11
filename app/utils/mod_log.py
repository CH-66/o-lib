# _*_ coding:utf-8 _*_
# Copyright (C) 2024-2024 shiyi0x7f,Inc.All Rights Reserved
# @Time : 2024/12/4 下午9:49
# @Author: shiyi0x7f
from loguru import logger
try:
    from .mod_env import get_env
except ImportError:
    from mod_env import get_env
import sys
import os

def setup_logger():
    env = get_env()  # 默认为生产环境
    # 清空默认的日志处理器
    logger.remove()
    # 根据环境设置不同的日志配置
    if env == 'DEV':
        # 开发环境：输出到控制台和文件
        logger.add(sys.stdout, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
        # 使用跨平台路径处理方法设置日志文件路径
        log_file_path = os.path.join(os.path.expanduser('~'), '.olib', 'app_debug.log')
        # 确保日志目录存在
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logger.add(log_file_path, level="DEBUG", rotation="1 MB", retention="10 days", compression="zip")
    elif env == 'PROD':
        # 生产环境：只输出到控制台
        logger.add(sys.stdout, level="INFO", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    else:
        # 默认处理方式
        logger.add(sys.stdout, level="DEBUG", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    logger.info(f"current env: {env}")
    # 可以根据需要配置更多的处理器，比如发送邮件、记录到数据库等
if __name__ == '__main__':
    setup_logger()