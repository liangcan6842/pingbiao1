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
@allure.feature("桌面端")
@allure.story("开标投标人端")
@allure.description("签到")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_sign_in(get_token_fixture):
    """签到"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "realName": "1018投标人",
        "mobile": "13212341234",
        "signInImg": "投标人签到图片"
    }
    url = URL + "/dst/bido/bidder/signin"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标投标人端")
@allure.description("签字")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_signature(get_token_fixture):
    """签字"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "signImage": "1019开标投标人签字图片",       #签名图片
    }
    url = URL + "/dst/bido/bidder/sign"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标投标人端")
@allure.description("查看开标记录表")
@allure.severity(allure.severity_level.MINOR)
def test_2_look_bid_open_record_sheet(get_token_fixture):
    """查看开标记录表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bido/bidder/create"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()