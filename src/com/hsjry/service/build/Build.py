from abc import ABCMeta, abstractmethod
import os
import paramiko


class Build(metaclass=ABCMeta):
    """
    专用打包服务，将所有模块按照指定分支进行打包，并产出jar包文件
    """

    @abstractmethod
    def build(self, rootPath, projectRepositorys, param):
        """
        开始构建
        """


class BuildJar(Build):
    def build(self, rootPath, projectRepositorys, param):

        codePath = os.path.join(rootPath, "code")
        if not os.path.exists(codePath):
            os.mkdir(codePath)

        for project in projectRepositorys:
            sshUrl = project["ssh-url"]
            projectPath = os.path.join(codePath, project["project-name"])
            # 将代码拉到指定目录
            if os.path.exists(projectPath):
                # 目录存在，则进去同步仓库、切换分支、
                command = "git -C %s fetch" % projectPath
                os.system(command)
                command = "git -C {projectPath} checkout {branch}".format(projectPath=projectPath,
                                                                          branch=param["branch"])
                os.system(command)
                command = "git -C %s pull origin" % projectPath
                os.system(command)
            else:
                # 创建当前分支
                command = 'git clone -b %s %s %s ' % (param["branch"], sshUrl, projectPath)
                os.system(command)
            print("-----------------------------------%s code sync success !!! --------------------------------------" %
                  project["project-name"])

class BuildOptName:
    """
    Opt名称
    """
    BUILD = "build"
