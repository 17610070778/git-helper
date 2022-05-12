from abc import ABCMeta, abstractmethod
from conf.Config import *

from src.com.hsjry.service.branch.Branch import *
from src.com.hsjry.service.mr.MR import MROptName, CreateMR, MR
from src.com.hsjry.service.tag.Tag import TagOptName, CreateTag, Tag
from src.com.hsjry.service.build.Build import *
import time


class Strategy(metaclass=ABCMeta):
    """
    接口类
    """

    @abstractmethod
    def getName(self):
        """
        返回当前策略的名字
        """
        pass

    @abstractmethod
    def run(self, *args):
        """
        策略的执行方法
        :param args:
        :return:
        """
        pass


class BranchStrategy(Strategy):
    """
    分支操作策略
    """

    def __init__(self) -> None:
        """
        初始化分支策略
        """
        map = dict()
        map[BranchOptName.CREATE] = CreateBranch()
        map[BranchOptName.DELETE] = DeleteBranch()
        map[BranchOptName.PROJECT] = ProtectBranch()
        self.__branchMap = map

    def getName(self):
        """
        返回当前策略的名字
        """
        return str(StrategyName.BRANCH)

    def run(self, *args):
        # 获取配置
        config = getConfig()
        projectIds = config.get("project-ids")
        params = args[0]
        # 获取策略
        branch: Branch = self.__branchMap.setdefault(params["opt"])

        for project in projectIds.items():
            ret = branch.exec(config.get("git-url"), project, getHeaders(config.get("token")), params)
            if ret.status_code != 201:
                print("warning：  %s" % ret.text)


class MRStrategy(Strategy):
    """
    合并策略
    """

    def __init__(self) -> None:
        """
        初始mr策略
        """
        map = dict()
        map[MROptName.CREATE] = CreateMR()
        self.__mrMap = map

    def getName(self):
        """
        返回当前策略的名字
        """
        return StrategyName.MR

    def run(self, *args):
        # 获取配置
        config = getConfig()
        projectIds = config.get("project-ids")
        params = args[0]
        # 获取策略
        mr: MR = self.__mrMap.setdefault(params["opt"])

        for project in projectIds.items():
            ret = mr.exec(config.get("git-url"), project, getHeaders(config.get("token")), params)
            if ret.status_code != 201:
                print("warning：  %s" % ret.text)


class TagStrategy(Strategy):
    """
    tag策略
    """

    def __init__(self) -> None:
        """
        初始mr策略
        """
        map = dict()
        map[TagOptName.CREATE] = CreateTag()
        self.__tagMap = map

    def getName(self):
        """
        返回当前策略的名字
        """
        return StrategyName.TAG

    def run(self, *args):
        # 获取配置
        config = getConfig()
        projectIds = config.get("project-ids")
        params = args[0]
        # 获取策略
        tag: Tag = self.__tagMap.setdefault(params["opt"])

        for project in projectIds.items():
            ret = tag.exec(config.get("git-url"), project, getHeaders(config.get("token")), params)
            if ret.status_code != 201:
                print("warning：  %s" % ret.text)


class BuildStrategy(Strategy):
    """
    build 打包策略
    """

    def __init__(self) -> None:
        """
        初始build策略
        """
        map = dict()
        map[BuildOptName.BUILD] = BuildJar()
        self.__tagMap = map

    def getName(self):
        """
        返回当前策略的名字
        """
        return StrategyName.BUILD

    def run(self, *args):
        # 创建文件夹
        rootPath = os.path.join(os.path.abspath("/"), "build-package")
        if not os.path.exists(rootPath):
            os.mkdir(rootPath)

        # 获取配置
        config = getConfig()
        projectRepositorys = config.get("project-repository")
        params = args[0]
        # 获取策略
        build: Build = self.__tagMap.setdefault(params["opt"])

        build.build(rootPath, projectRepositorys, params)


class StrategyName:
    """
    策略名称
    """
    BRANCH = "branch"

    TAG = "tag"

    MR = "mr"

    BUILD = "build"
