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
@allure.story("开标记录模板")
@allure.description("开标记录模板新增\修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_open_bid_open_module(get_token_fixture):
    """开标记录模板新增\修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0, #
        "name": "开标记录模板1",
        "fields": [
            {
                # "id": 0,
                "sn": 20221217,  #序号
                "fieldName": "开标字段",  #字段名
                "display": 1,  #是否显示
                "selects": 1,  #是否可选
                "option1": "选项1", #选项1
                "option2": "选项2",
                "option3": "选项3",
                "fixed": 0   #是否是固定值,
            }
        ]
    }
    url = URL + "/biz/obid/template/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标记录模板")
@allure.description("开标记录模板删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_delete_bid_open_record_module(get_token_fixture):
    """开标记录模板删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [4]
    url = URL + "/biz/obid/template/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标记录模板")
@allure.description("开标记录模板分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_3_bid_open_record_module_paging_query(get_token_fixture):
    """开标记录模板分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10
    }
    url = URL + "/biz/obid/template/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标记录模板")
@allure.description("开标记录详情查询")
@allure.severity(allure.severity_level.MINOR)
def test_4_bid_open_record_module_detail_query(get_token_fixture):
    """开标记录详情查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 5 #模板id
    }
    url = URL + "/biz/obid/template/view"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标记录模板")
@allure.description("添加前查询预设字段")
@allure.severity(allure.severity_level.MINOR)
def test_5_before_add_presetFields_query(get_token_fixture):
    """添加前查询预设字段"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/biz/obid/template/beforeAdd"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.mian()