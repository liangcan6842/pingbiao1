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
@allure.story("评标办法-流程配置")
@allure.description("选择评标办法")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_chose_bid_evaluated_method(get_token_fixture):
    """选择评标办法"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "configId": 2,           #评标办法流程配置id
        "projectId": 13          #评标项目id
    }
    url = URL + "/v1/bidMethodConfig/project"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-流程配置")
@allure.description("拷贝评标办法")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_copy_bid_evaluated_method(get_token_fixture):
    """拷贝评标办法"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13,               #当前评标项目id
        "copyProjectId": 18            #拷贝项目id
    }
    url = URL + "/v1/bidMethodConfig/project/copy"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-流程配置")
@allure.description("启动禁用")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_setup_disable(get_token_fixture):
    """启动禁用"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 1,               #评标办法id
        "state": 1             #状态1 启动，0-禁用
    }
    url = URL + "/v1/bidMethodConfig/update"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-流程配置")
@allure.description("表格查询")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_query_sheet(get_token_fixture):
    """表格查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/bidMethodConfig/list"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-流程配置")
@allure.description("根据id查询")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_recordId_query(get_token_fixture):
    """根据id查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":2 } #评标办法id
    url = URL + "/v1/bidMethodConfig/id"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200