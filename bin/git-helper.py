import os
import sys

sys.path.append(os.path.abspath(os.path.abspath("..")))
from src.com.hsjry.boot.BootStrap import *

if __name__ == '__main__':
    print("start...")
    args = sys.argv
    if len(args) < 2:
        raise RuntimeError("请输入要执行的命令  如 branch xx、 tag xx、 mr xxx等")
    args.pop(0)
    strategy = args.pop(0)

    params = dict()
    for i in args:
        ele = i.split("=")
        params[ele[0]] = ele[1]
    cost1 = time.time()

    init().getStrategy(strategy).run(params)

    cost2 = time.time()
    print("耗时：%s 分 %s 秒" % (int(((cost2 - cost1) / 60)), ((cost2 - cost1) % 60)))
