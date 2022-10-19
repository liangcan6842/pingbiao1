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
@allure.story("用户登录接口")
@allure.description("用户登录")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_login_user(get_token_fixture):
    """用户登录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "username": "test1019",
        "password": "1234567",
        "macCode": ""
    }
    url = URL + "/login"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)

@allure.feature("权限管理")
@allure.story("用户登录接口")
@allure.description("修改密码")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_alter_user_password(get_token_fixture):
    """修改密码"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "oldPassword": "123456",
        "newPassword": "123456"
    }
    url = URL + "/cp"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户登录接口")
@allure.description("查询个人信息")
@allure.severity(allure.severity_level.NORMAL)
def test_3_query_personal_message(get_token_fixture):
    """查询个人信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/profile"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("用户登录接口")
@allure.description("查询我的权限")
@allure.severity(allure.severity_level.NORMAL)
def test_4_query_my_authorization(get_token_fixture):
    """查询我的权限"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/menus"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()