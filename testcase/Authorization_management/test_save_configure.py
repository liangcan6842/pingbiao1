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
@allure.story("配置管理")
@allure.description("保存配置")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_save_configure(get_token_fixture):
    """保存配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0,
        "status": 1,   #状态,0:关闭,1:开启
        "name": "101943576357364567配置",    #配置名
        "value": "b768c203039f455d245debfce2bad0fd",   #配置值
        "category": "101453645019",  #分类
        "key": "3426"        #配置键
    }
    url = URL + "/sys/config/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("配置管理")
@allure.description("分页查询配置")
@allure.severity(allure.severity_level.NORMAL)
def test_1_paging_query_configure(get_token_fixture):
    """分页查询配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "name": "",
        "category": ""
    }
    url = URL + "/sys/config/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("配置管理")
@allure.description("查询配置")
@allure.severity(allure.severity_level.NORMAL)
def test_1_query_configure(get_token_fixture):
    """查询配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 3}
    url = URL + "/sys/config/view"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("权限管理")
@allure.story("配置管理")
@allure.description("删除配置")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_delete_configure(get_token_fixture):
    """删除配置"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [1]
    url = URL + "/sys/config/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()