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
@allure.feature("业务系统")
@allure.story("开标-主持人")
@allure.description("开标主持人新增")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bid_project_host(get_token_fixture):
    """开标主持人新增"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必填
        "name": "1013576578主持人",
        "oexpired": "2022-10-20 14:08:00", #开标时效时间
        "eexpired": "2022-10-20 17:10:15", #评标时效时间
        "projectId": 2  #开标项目id
    }
    url = URL + "/biz/host/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-主持人")
@allure.description("开标主持人删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_delete_bid_open_host(get_token_fixture):
    """开标主持人删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [3]
    url = URL + "/biz/host/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-主持人")
@allure.description("开标主持人分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_3_bid_open_host_paging_query(get_token_fixture):
    """开标主持人分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "bizProjectId":2 , #开标项目id
        # "name": "" #名称
    }
    url = URL + "/biz/host/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200













