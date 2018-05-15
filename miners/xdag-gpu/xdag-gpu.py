# -*- coding:utf-8 -*-

import subprocess
import sys
import socket
import signal
import json
import threading
import select
import Queue
import time
import re

g_queue = Queue.Queue()


class my_miner:
    miner = None
    turn_off = False
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    def start_miner(self, params):
        cmd = './xdag-gpu ' + params + ' 2>&1'
        self.miner = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        poller = select.poll()
        READ_ONLY = ( select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
        poller.register(self.miner.stdout, READ_ONLY)
        while True:
            try:
                if self.turn_off: break
                events = poller.poll(1000)
                if len(events) > 0:
                    line = self.miner.stdout.readline()
                    ret = self.parse_hash(line)
                    if not ret: continue
                    g_queue.put(ret)
            except Exception as e:
                print e.message

    def parse_hash(self, line):
        print line
        ansi_line = self.ansi_escape.sub('', line)
        if ansi_line.find('Speed') > 0:
            log_stats = ansi_line.split()[5:]
            ret = []
            for i in range(len(log_stats)/2):
                idx = 2*i+1
                ret.append(1024*int(float(log_stats[idx])))
            return dict(result = ret)
        return None

    def stop(self):
        self.turn_off = True
        time.sleep(1)
        self.miner.kill()

class my_server:
    thr = None
    soc = None
    def init(self):
        self.thr = threading.Thread(target=self.read_write)
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        address = ('127.0.0.1', 3333)
        self.soc.bind(address)
        self.soc.listen(5)

    def read_write(self):
        while True:
            ss, addr = self.soc.accept()
            try:
                ss.settimeout(5)
                buf = "{}"
                if not g_queue.empty():
                    buf = json.dumps(g_queue.get())
                ra = ss.recv(512)
                ss.send(buf)
                ss.close()
            except Exception as e:
                print e.message
        self.soc.close()
    def run(self):
        self.thr.daemon = True
        self.thr.start()

    def stop(self):
        self.thr.do_run = False
        self.soc.close()


svr = my_server()
svr.init()
svr.run()

miner = my_miner()


def handler(a, b):
    svr.stop()
    miner.stop()

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGINT, handler)

miner.start_miner(' '.join(sys.argv[1:]))


