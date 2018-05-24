# coding: utf-8


"""
v1.0
Miner controller

function:

1) 维护挖矿程序列表
2) 启动、停止挖矿程序



"""

import os
import json


# 配置文件管理


def read_miner_config():
    load_info_dict = json.load(open("../config/miner-info.json"))
    print(type(load_info_dict))


def write_miner_config(info_dict={}):

    print(json.dump(info_dict, open(
        "../config/miner-info.json", "w"), ensure_ascii=False))


# 挖矿管理
def start_miners(miner_type=None, addr=None, worker_name=None, processes=1):
    pass
    # 执行linux命令 -> 启动程序 -> 程序执行ls
    run_comm = 'nohup  ' + comm + " 1>miner.log 2>&1 & "
    # x = os.system(run_comm)
    # print x

    def run_shell(run_cmm): return os.system(run_comm)
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
    # write_miner_config()
    read_miner_config()
    start_miners(miner_type="BTM", addr=r"dfajkldflae",
                 worker_name="test", processes=1)
