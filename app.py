# _*_ coding:utf-8 _*_
# Copyright (C) 2024-2024 shiyi0x7f,Inc.All Rights Reserved
# @Time : 2024/12/4 下午9:19
# @Author: shiyi0x7f
from PyQt5.QtWidgets import QApplication
from app.utils import setup_logger
from app.common.config import cfg
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from app.views.main_window import Window
from app.common.icons import get_app_icon
import sys
import os
from loguru import logger


def ensure_directories():
    """确保必要的目录存在"""
    # 确保下载目录存在
    download_dir = cfg.downloadFolder.value
    if not os.path.isabs(download_dir):
        # 如果是相对路径，则转换为绝对路径
        download_dir = os.path.abspath(download_dir)
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)


if __name__ == '__main__':
    setup_logger()
    # 确保必要的目录存在
    ensure_directories()
    if cfg.get(cfg.dpiScale) == "Auto":
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(
            Qt.AA_EnableHighDpiScaling)
    else:
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(
            cfg.get(cfg.dpiScale))
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    # create application
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    # create main window
    w = Window()
    # 根据操作系统自动选择合适的图标格式
    icon_path = get_app_icon()
    if icon_path and os.path.exists(icon_path):
        w.setWindowIcon(QIcon(icon_path))
    else:
        # 如果无法找到合适的图标文件，则使用默认的资源文件图标
        w.setWindowIcon(QIcon(":/image/ICO"))
    w.show()

    sys.exit(app.exec_())