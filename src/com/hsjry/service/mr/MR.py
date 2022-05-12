from abc import ABCMeta, abstractmethod

from requests import Response

from src.com.hsjry.constant.ServiceUrl import ServiceUrl
from src.com.hsjry.util.Fetch import fetch


class MR(metaclass=ABCMeta):
    """
    定义一个接口
    """

    @abstractmethod
    def exec(self, url, project, headers, params) -> Response:
        pass


class CreateMR(MR):

    def exec(self, url, project, headers, params):
        sourceBranch = params["source_branch"]
        targetBranch = params["target_branch"]
        title = params["title"]
        print("项目：%s  分支：%s ->  %s 发起合并" % (project[0], sourceBranch, targetBranch))
        url = ServiceUrl.createMrBranch.format(url=url, id=project[1])
        data = {
            "source_branch": sourceBranch,
            "target_branch": targetBranch,
            "title": title
        }
        ret = fetch(url, "POST", headers=headers, data=data)
        return ret


class MROptName:
    """
    策略名称
    """
    CREATE = "create"
