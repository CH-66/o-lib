# _*_ coding:utf-8 _*_
# @Time : 2025/08/11 
# @Author: ch-66

import os
import sys
import platform


def get_app_icon():
    """
    根据操作系统自动选择合适的图标格式
    macOS使用.icns格式，Windows使用.ico格式，Linux使用.png格式
    
    Returns:
        str: 图标文件路径
    """
    # 获取项目根目录
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 获取当前操作系统
    system = platform.system().lower()
    
    # 根据操作系统选择图标文件
    if system == "darwin":  # macOS
        icon_path = os.path.join(root_dir, "logo.icns")
    elif system == "windows":  # Windows
        icon_path = os.path.join(root_dir, "logo.ico")
    else:  # Linux和其他系统
        icon_path = os.path.join(root_dir, "logo.png")
    
    # 检查图标文件是否存在，如果不存在则使用默认图标
    if not os.path.exists(icon_path):
        # 尝试使用默认的ico图标
        icon_path = os.path.join(root_dir, "logo.ico")
        if not os.path.exists(icon_path):
            # 如果还是不存在，则返回None
            return None
    
    return icon_path