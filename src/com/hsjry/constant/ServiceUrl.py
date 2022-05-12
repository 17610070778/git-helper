class ServiceUrl:
    """
    POST
    创建一个新分支 1:主机，2：项目id， 3：新分支名称，4：源分支名称
    id	integer 整数	yes 是的	ID or 身份证或URL-encoded path of the project Url 编码的项目路径 owned by the authenticated user. 属于已验证身份的用户
    branch	string 字符串	yes 是的	Name of the branch. 分行名称
    ref	string 字符串	yes 是的	Branch name or commit SHA to create branch from. 分支名称或提交 SHA 以从
    """
    createNewBranch = "{url}/api/v4/projects/{id}/repository/branches?branch={new_branch}&ref={origin}"

    """
    DELETE
    删除一个分支 1:主机，2：项目id， 3：分支名称
    id	integer/string 整数/字符串	yes 是的	ID or 身份证或URL-encoded path of the project Url 编码的项目路径 owned by the authenticated user. 属于已验证身份的用户
    branch	string 字符串	yes 是的	Name of the branch. 分行名称
    """
    deleteBranch = "{url}/api/v4/projects/{id}/repository/branches/{branch}"

    """
    POST
    保护一个分支  1:主机，2：项目id， 3：分支名称
    id	integer/string 整数/字符串	yes 是的	The ID or 身份证或URL-encoded path of the project Url 编码的项目路径 owned by the authenticated user 属于已验证身份的用户
    name	string 字符串	yes 是的	The name of the branch or wildcard 分支或通配符的名称
    """
    protectBranch = "{url}/api/v4/projects/{id}/protected_branches?name={branch}"

    """
    POST
    创建mr  1:主机，2：项目id， 3：分支名称
    id	integer/string 整数/字符串	yes 是的	The ID or 身份证或URL-encoded path of the project Url 编码的项目路径 owned by the authenticated user 属于已验证身份的用户
    source_branch	string 字符串	yes 是的	The source branch. 源分支
    target_branch	string 字符串	yes 是的	The target branch. 目标分支
    title	string 字符串	yes 是的	Title of MR. 先生的头衔
    """
    createMrBranch = "{url}/api/v4/projects/{id}/merge_requests"

    """
    POST
    创建一个新标签  1:主机，2：项目id， 3：新tag名称，4：源分支名称
    """
    createNewTag = "{url}/api/v4/projects/{id}/repository/tags"
