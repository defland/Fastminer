# coding=utf-8

"""
fsminer v1.0


功能表：

- 控制模块：控制启动、配置、多进程管理挖矿程序
- 交互模块：处理用户交互和控制中心的动态数据展示
- Net模块：处理和后端api的对接，实现用户激活的功能

最小闭环mvp开发：
1、可以用Python启动挖矿程序，配置参数、和停止挖矿程序。

- 从config中读取miners目录的配置文件功能
- 启动挖矿程序功能
- 停止挖矿程序功能
- 用户的钱包地址、等信息写入user-config功能。
-


"""
import os


def start_miners(comm=None,miner_wd=None,log_wd=None,processes=1):
    pass
    # 执行linux命令 -> 启动程序 -> 程序执行ls
    run_comm = 'nohup  ' + comm + " 1>miner.log 2>&1 & "
    # x = os.system(run_comm)
    # print x

    run_shell = lambda run_cmm: os.system(run_comm)
    result = [run_shell(run_comm) for x in range(2)]

    print(result)


def stop_miners():
    pass


def check_miners():
    pass


def miner_config():
    pass


if __name__ == "__main__":

    pass
    start_miners('ping www.baidu.com')
