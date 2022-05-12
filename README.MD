### git-helper简介
    为了解决每次迭代上线后，批量打tag、批量切新迭代分支、批量回归，等需要人工一个一个的操作的难题，开发此工具
#### 依赖模块
##### 依赖远程调用模块
###### 外网操作
    pip install --user --index-url https://mirrors.aliyun.com/pypi/simple/ requests
    
###### 内网操作
    // requests
    pip install idna-2.10-py3-none-any.whl
    pip install urllib3-1.26.9-py2.py3-none-any.whl
    pip install chardet-4.0.0-py3-none-any.whl
    pip install certifi-2019.11.28-py2.py3-none-any.whl
    进入到 requests-master.zip文件中，执行 python setup.py install
###### git环境
    你的git要加入环境变量，并且配置好ssh免密登录
###### java环境
    JAVA_HOME要加入环境变量，因为maven使用的这个变量
###### maven环境
    mvn要加入环境变量
#### 使用文档：
##### 配置说明 ./conf/config.json
```json
{
  "git-url": "https://gitlab.com/",
  "token": "***",   // 你得token
  "project-ids": {   // 批量创建分支、mr、tag等操作
    "test1": 4,   // credit项目名称，4为项目id，可配置多个
    "test2": 5
  },
  "project-repository": [    // 自动拉代码切分支
    {
      "project-name": "tesst1",
      "ssh-url": "git@gitlab.com:/tesst1.git"
    },
    {
      "project-name": "tesst2",
      "ssh-url": "git@gitlab.com:/tesst2.git"
    }
  ]
}
```
### 注意
```json
分支名是  feature/20220421  具有斜杠的这种形式，  如果报404 请尝试 将/ 转成 %2F 如：feature%2F20220421  
```
### 使用方式 需要切到bin目录下执行如下命令
#####  批量创建branch
    python git-helper.py  branch  opt=create new_branch=tset8   origin=master
    
#####  批量删除branch
    python git-helper.py  branch  opt=delete branch=tset8

#####  批量保护branch
    python git-helper.py  branch  opt=protect branch=tset4
    
#####  批量发起mr
    python git-helper.py mr  opt=create source_branch=tset4   target_branch=main title="系统测试"
    
#####  批量打Tag
    python git-helper.py tag  opt=create tag_name=V2.1.7.3  ref=tset4
    
#####  拉代码
    python git-helper.py build  opt=build branch=feature/20220429
    
    