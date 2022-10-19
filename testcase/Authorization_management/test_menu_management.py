import pytest,requests,json,allure
from ddt import ddt,file_data
from common.Package_file_method import read_yaml
URL = 'http://192.168.110.245:8887'
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("权限管理")
@allure.story("菜单管理")
@allure.description("新增菜单")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_menu(get_token_fixture):
    """新增菜单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,  #	状态,0:关闭,1:开启
        "name": "1019测试菜单",    #菜单名称
        "level": 2,   #权限等级(1:目录,2:菜单,3:按钮)
        # "parentId": 0,  #父级ID
        # "path": "",     #路由
        # "permission": "",  #权限标识
        # "sortNumber": 0,   #排序
        # "icon": "",        #图标
        # "checked": 'true'
    }
    url = URL + "/sys/menu/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("菜单管理")
@allure.description("新增菜单")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_batch_add_menu(get_token_fixture):
    """批量新增菜单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "parentId": 0,
        "menus": [
            {
                "status": 1,  # 状态,0:关闭,1:开启
                "name": "1019测试菜单",  # 菜单名称
                "level": 2,  # 权限等级(1:目录,2:菜单,3:按钮)
                # "parentId": 0,  #父级ID
                # "path": "",     #路由
                # "permission": "",  #权限标识
                # "sortNumber": 0,   #排序
                # "icon": "",        #图标
                # "checked": 'true'
            }
        ]
    }
    url = URL + "/sys/menu/adds"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("菜单管理")
@allure.description("查询树形结构菜单")
@allure.severity(allure.severity_level.NORMAL)
def test_3_paging_query_menu(get_token_fixture):
    """查询树形结构菜单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/sys/menu/tree"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

@allure.feature("权限管理")
@allure.story("菜单管理")
@allure.description("修改菜单")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_alter_menu(get_token_fixture):
    """修改菜单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,  #	状态,0:关闭,1:开启
        "name": "1019测试菜单",    #菜单名称
        "level": 2,   #权限等级(1:目录,2:菜单,3:按钮)
        # "parentId": 0,  #父级ID
        # "path": "",     #路由
        # "permission": "",  #权限标识
        # "sortNumber": 0,   #排序
        # "icon": "",        #图标
        # "checked": 'true'
    }
    url = URL + "/sys/menu/edit"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("菜单管理")
@allure.description("删除菜单")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_delete_menu(get_token_fixture):
    """删除菜单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":2}
    url = URL + "/sys/menu/delete"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()