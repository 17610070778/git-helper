from abc import ABCMeta, abstractmethod

from requests import Response

from src.com.hsjry.constant.ServiceUrl import *
from src.com.hsjry.util.Fetch import *
import re


class Branch(metaclass=ABCMeta):
    """
    定义一个接口
    """

    @abstractmethod
    def exec(self, url, project, headers, params) -> Response:
        pass


class CreateBranch(Branch):
    def exec(self, url, project, headers, params):
        newBranch = params["new_branch"]
        ret = re.match("(feature|hotfix)/\d{8}", newBranch)
        if None == ret:
            raise RuntimeError("创建的新分支请符合规范 feature/20220508_XX 或 hotfix/20220508_XX")
        originBranch = params["origin"]

        print("项目：%s   基于：%s 分支， 创建 %s  新分支" % (project[0], originBranch, newBranch))
        url = ServiceUrl.createNewBranch.format(url=url, id=project[1], new_branch=newBranch,
                                                origin=params["origin"])
        ret = fetch(url, "POST", headers=headers, data={})
        return ret


class DeleteBranch(Branch):
    def exec(self, url, project, headers, params):
        branch = params["branch"]
        print("项目：%s 删除分支：%s" % (project[0], branch))
        url = ServiceUrl.deleteBranch.format(url=url, id=project[1], branch=branch)
        ret = fetch(url, "DELETE", headers=headers, data={})
        return ret


class ProtectBranch(Branch):
    def exec(self, url, project, headers, params):
        branch = params["branch"]
        print("项目：%s  保护分支：%s" % (project[0], branch))
        url = ServiceUrl.protectBranch.format(url=url, id=project[1], branch=branch)
        ret = fetch(url, "POST", headers=headers, data={})

        return ret


class BranchOptName:
    """
    策略名称
    """
    CREATE = "create"

    DELETE = "delete"

    PROJECT = "protect"
