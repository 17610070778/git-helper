import requests


def fetch(url: str, method: str, headers: object, data: object) -> object:
    """
    用于请求git服务器
    """
    ret = None
    if "GET" == method:
        ret = requests.get(url, headers=headers, data=data)
    elif "POST" == method:
        ret = requests.post(url, headers=headers, data=data)
    elif "DELETE" == method:
        ret = requests.delete(url, headers=headers, data=data)
    else:
        raise RuntimeError("暂不支持的请求方式" + method)
    return ret


def getHeaders(value: str):
    return {
        "PRIVATE-TOKEN": value
    }
