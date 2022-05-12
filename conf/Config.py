import json
import os


def getConfig() -> dict:
    """
    获取配置文件
    """
    fileLocation = os.path.join(os.path.dirname(__file__), "config.json")
    with open(fileLocation) as fileContent:
        content = json.load(fileContent)
    return content
