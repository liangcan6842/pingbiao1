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
@allure.story("用户相关功能")
@allure.description("新增用户")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_user(get_token_fixture):
    """新增用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "username": "test10195",  #用户名
        "password": "123456",  #密码
        "nickName": "1019测试",  #昵称
        "remark": "人员备注",    #备注
        "roleIds": [7]    #角色id
    }
    url = URL + "/sys/user/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户相关功能")
@allure.description("分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_2_paging_query_user(get_token_fixture):
    """分页查询用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "limit": "10",
        "page": "1",
        # "username": "test1019",
        # "nickName": "1019测试",
        # "roleId": "",
        # "roleName": "",
        # "start": "",
        # "end": ""
    }
    url = URL + "/sys/user/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户相关功能")
@allure.description("查询用户")
@allure.severity(allure.severity_level.NORMAL)
def test_3_query_user(get_token_fixture):
    """查询用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 48 }
    url = URL + "/sys/user/view"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户相关功能")
@allure.description("修改用户")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_alter_user(get_token_fixture):
    """修改用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 45,
        "username": "4263567",  #用户名
        "password": "123456",  #密码
        "nickName": "1019测试",  #昵称
        "roleIds": [6]    #角色id
    }
    url = URL + "/sys/user/edit"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户相关功能")
@allure.description("删除用户")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_delete_user(get_token_fixture):
    """删除用户"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [49]
    url = URL + "/sys/user/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()