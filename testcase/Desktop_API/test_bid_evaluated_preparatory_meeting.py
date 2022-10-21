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
@allure.story("评标预备会")
@allure.description("其他信息")
@allure.severity(allure.severity_level.NORMAL)
def test_1_other_message(get_token_fixture):
    """其他信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13,       #评标项目id
        "type": 2             #1：项目概况；2：评标工作记录；3：评委委员会声明书；4：专家风险责任清单
      }
    url = URL + "/dst/bid/information/getInformation"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标预备会")
@allure.description("招标文件")
@allure.severity(allure.severity_level.NORMAL)
def test_2_bid_file(get_token_fixture):
    """招标文件"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13       #评标项目id
      }
    url = URL + "/dst/bid/information/getBidding"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.mian()