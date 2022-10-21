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
@allure.story("评标-文件管理")
@allure.description("监督人签到表")
@allure.severity(allure.severity_level.NORMAL)
def test_1_supervisor_sign_in_sheet(get_token_fixture):
    """监督人签到表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13  #评标项目id
    }
    url = URL + "/bid/manageFile/supervisorList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("评委签到表")
@allure.severity(allure.severity_level.NORMAL)
def test_2_judge_sign_in_sheet(get_token_fixture):
    """评委签到表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13  #评标项目id
    }
    url = URL + "/bid/manageFile/judgesSignList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("专家列表")
@allure.severity(allure.severity_level.NORMAL)
def test_3_expert_list(get_token_fixture):
    """专家列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13  #评标项目id
    }
    url = URL + "/bid/manageFile/judgesList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("未通过初审表")
@allure.severity(allure.severity_level.NORMAL)
def test_4_not_pass_first_trial_sheet(get_token_fixture):
    """未通过初审表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13  #评标项目id
    }
    url = URL + "/bid/manageFile/getVeto"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("详细、商务评、技术评审汇总")
@allure.severity(allure.severity_level.NORMAL)
def test_5_detail_business_summary(get_token_fixture):
    """详细、商务评、技术评审汇总"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"projectId":13}   #项目id
    url = URL + "/bid/manageFile/getSummary"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("详细、商务评、技术评审信息")
@allure.severity(allure.severity_level.NORMAL)
def test_6_detail_business_message(get_token_fixture):
    """详细、商务评、技术评审信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "nodeId":2,    #评审办法类型
        "judgesId":3     #专家id
    }
    url = URL + "/bid/manageFile/getReviewDetail"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("签字图片")
@allure.severity(allure.severity_level.NORMAL)
def test_7_signature_picture(get_token_fixture):
    """签字图片"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "type":1,     #1：评委；2：监督人
        "projectId":13     #项目id
    }
    url = URL + "/bid/manageFile/getSignqzImgy"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("初步评审表")
@allure.severity(allure.severity_level.NORMAL)
def test_8_first_step_review_sheet(get_token_fixture):
    """初步评审表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13,     #项目id
        "judgesId":3     #评委id
    }
    url = URL + "/bid/manageFile/getPreliminary"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("开标记录表")
@allure.severity(allure.severity_level.NORMAL)
def test_9_bid_open_record_sheet(get_token_fixture):
    """开标记录表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/bid/manageFile/getOpenRecord"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-文件管理")
@allure.description("评估报告")
@allure.severity(allure.severity_level.NORMAL)
def test_10_evaluated_report(get_token_fixture):
    """评估报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13     #项目id
    }
    url = URL + "/bid/manageFile/assessment"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()
