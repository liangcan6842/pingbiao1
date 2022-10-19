import datetime
import logging
import os.path
import sys
from os import path

def get_logger(log_name):  # 封装日志操作，在最后调用
    logger = logging.getLogger(log_name)  # 创建日志器
    sh = logging.StreamHandler(sys.stdout)  # 创建控制台处理器
    sh.setFormatter(logging.Formatter('%(asctime)s|%(levelname)s|%(message)s'))  # 格式器
    logger.addHandler(sh)  # 将日志信息显示到控制台

    log_path = path.abspath(path.dirname(__file__) + '/../../../NVRLog')  # 文本log，当前项目下创建NVRlog文件夹，可自定义

    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_path = os.path.join(log_path, '%s.log' % log_name)
    if not os.path.exists(log_path):
        open(log_path, 'w')  # 进入log路径，写入信息

    fh = logging.FileHandler(log_path)  # 创建文本处理器
    fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(filename)s[%(lineno)d] - %(message)s'))  # 格式器
    logger.addHandler(fh)
    logger.setLevel(20)  # logger等级
    return logger


run_time = 'runtime_' + str(datetime.datetime.now().strftime("%Y%m%d"))  # 构建日志runtime_xxx.log的名称
debugLogger = get_logger(log_name=run_time)  # 往后直接用debugLogger调用日志模块