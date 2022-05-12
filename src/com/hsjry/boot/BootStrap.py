from src.com.hsjry.strategy.Strategy import *


class BootStrap:
    """
    启动引导类
    """

    def __init__(self, strategyList: Strategy = []):
        """
        初始化策略
        :param strategyList:
        """
        self.__gitStrategyDict = {}
        for strategy in strategyList:
            self.__gitStrategyDict[strategy.getName()] = strategy

    def getStrategy(self, strategyName: str) -> Strategy:
        """
        获取策略
        :param strategyName:
        :return:
        """
        strategy = self.__gitStrategyDict.setdefault(strategyName)
        if None == strategy:
            raise RuntimeError(strategyName + " 参数非法，不存在的命令!!!")
        return strategy


def init() -> BootStrap:
    branchStrategy = BranchStrategy()
    tagStrategy = TagStrategy()
    mrStrategy = MRStrategy()
    buildStrategy = BuildStrategy()

    lis = [branchStrategy, tagStrategy, mrStrategy, buildStrategy]
    return BootStrap(lis)
