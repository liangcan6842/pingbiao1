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
@allure.story("评标办法-初步评审配置")
@allure.description("新增")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bid_evaluated_method(get_token_fixture):
    """新增"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "status": 1,           #状态,0:关闭,1:开启
        "content": 2,          #内容:1-形式评审，2-资格评审，3-响应性评审
        "serialNumber": 2,     #	序号
        "reviewFactor": "根据评标资格分数",    #评审因素
        "reviewStandard": "4365478",  #评审标准
        "scoreType": "统一打分",       #打分方式：统一打分
        "required": 1,         #0-否，1-是
        "projectId": 18,         #关联项目id
        "nodeId": 1
    }
    url = URL + "/v1/bidReviewPreliminary/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-初步评审配置")
@allure.description("列表查询")
@allure.severity(allure.severity_level.NORMAL)
def test_2_bid_evaluated_method_list_query(get_token_fixture):
    """列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13,
        "nodeId":2
    }
    url = URL + "/v1/bidReviewPreliminary/list"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-初步评审配置")
@allure.description("修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_alter_bid_evaluated_method(get_token_fixture):
    """修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 4,
        "status": 1,  #状态,0:关闭,1:开启
        "content": 2,  #内容:1-形式评审，2-资格评审，3-响应性评审
        "serialNumber": 2,  ##	序号
        "reviewFactor": "质量",  #评审因素
        "reviewStandard": "236456",  #评审标准
        "scoreType": "同意打分",  #
        "required": 1,  #0-否，1-是
        "projectId": 18,  #关联项目id
        "nodeId": 2  #评标办法id
    }
    url = URL + "/v1/bidReviewPreliminary/update"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-初步评审配置")
@allure.description("删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_delete_bid_evaluated_method(get_token_fixture):
    """删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [6]
    url = URL + "/v1/bidReviewPreliminary/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()
