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
@allure.story("开标管理")
@allure.description("开标项目新增\修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bid_project(get_token_fixture):
    """开标项目新增\修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #修改必传
        "name": "开标项目1546547017", #名称
        "place": "重庆南坪", #开标地点
        "owner": "1017招标人", #招标人
        "openTime": "2022-10-17 14:00:00", #开标时间
        "roomId": 2, #开标室ID
        "templateId": 5 #开标记录表ID
    }
    url = URL + "/biz/project/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

@allure.feature("业务系统")
@allure.story("开标管理")
@allure.description("开标项目删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_delete_bid_open_project(get_token_fixture):
    """开标项目删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [3]
    url = URL + "/biz/project/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标管理")
@allure.description("开标项目分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_3_bid_open_project_paging_query(get_token_fixture):
    """开标项目分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10
    }
    url = URL + "/biz/project/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标管理")
@allure.description("开标项目查询详情")
@allure.severity(allure.severity_level.MINOR)
def test_4_bid_open_project_detail_query(get_token_fixture):
    """开标项目查询详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":2  #项目id
    }
    url = URL + "/biz/project/view"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标管理")
@allure.description("查询开标记录模板")
@allure.severity(allure.severity_level.MINOR)
def test_5_query_bid_open_record_module(get_token_fixture):
    """查询开标记录模板"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":2} #项目id
    url = URL + "/biz/project/obidtemp"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.mian()






























if __name__ == '__main__':
    pytest.mian()