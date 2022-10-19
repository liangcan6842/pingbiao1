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
@allure.story("角色管理")
@allure.description("新增角色")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_role(get_token_fixture):
    """新增角色"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,      #状态,0:关闭,1:开启
        "name": "1019角色",       #名称
        "remark": "新增一个角色",     #备注
        "sign": "测试角色",       #角色标识
        "menus": [8]       #菜单id
    }
    url = URL + "/sys/role/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("分页查询角色")
@allure.severity(allure.severity_level.NORMAL)
def test_2_paging_query_role(get_token_fixture):
    """分页查询角色"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        # "name": "test1019",
        # "start": "",
        # "end": "",
        #"status": 1,
    }
    url = URL + "/sys/role/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("查询角色")
@allure.severity(allure.severity_level.NORMAL)
def test_3_query_role(get_token_fixture):
    """查询角色"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 48 }
    url = URL + "/sys/role/view"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("修改角色")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_alter_role(get_token_fixture):
    """修改角色"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":1 ,
        "status": 1,      #状态,0:关闭,1:开启
        "name": "1019角色",       #名称
        "remark": "新增一个角色",     #备注
        "sign": "测试角色",       #角色标识
        "menus": []       #菜单id
    }
    url = URL + "/sys/role/edit"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("删除角色")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_delete_role(get_token_fixture):
    """删除角色"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 9 }
    url = URL + "/sys/role/delete"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("修改角色状态")
@allure.severity(allure.severity_level.CRITICAL)
def test_6_alter_role_state(get_token_fixture):
    """修改角色状态"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 6,"status": 1 }    #状态 状态,0:关闭,1:开启
    url = URL + "/sys/role/state"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("角色权限查询")
@allure.severity(allure.severity_level.NORMAL)
def test_7_query_role_authorization(get_token_fixture):
    """角色权限查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 8 }
    url = URL + "/sys/role/menus"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("角色管理")
@allure.description("角色列表查询")
@allure.severity(allure.severity_level.NORMAL)
def test_8_query_role_list(get_token_fixture):
    """角色列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/sys/role/list"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
if __name__ == '__main__':
    pytest.main()