from abc import ABCMeta, abstractmethod

from requests import Response

from src.com.hsjry.constant.ServiceUrl import ServiceUrl
from src.com.hsjry.util.Fetch import fetch
import re


class Tag(metaclass=ABCMeta):
    """
    定义一个接口
    """

    @abstractmethod
    def exec(self, url, project, headers, params) -> Response:
        pass


class CreateTag(Tag):
    """
    定义一个接口
    """

    def exec(self, url, project, headers, params):
        tagName = params["tag_name"]
        ret = re.match("V2.1.*", tagName)
        if None == ret:
            raise RuntimeError("打新Tag 请符合规范 V2.1.*+")
        ref = params["ref"]
        print("项目：%s  分支：%s 创建标签：%s" % (project[0], ref, tagName))
        url = ServiceUrl.createNewTag.format(url=url, id=project[1])
        data = {
            "tag_name": tagName,
            "ref": ref
        }
        ret = fetch(url, "POST", headers=headers, data=data)
        return ret


class TagOptName:
    """
    策略名称
    """
    CREATE = "create"
