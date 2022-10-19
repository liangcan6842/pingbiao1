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
@allure.story("评标-评估报告")
@allure.description("新增\修改评估报告")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bid_evaluated_report_module(get_token_fixture):
    """新增\修改评估报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id": 2,   #修改必传
        "status": 1,  #	状态,0:关闭,1:开启
        "name": "评标项目评估模板1018",      #模板名
        "template": "评估报告模板1"    #对应模板名
    }
    url = URL + "/bid/assessmentTemplate/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评估报告")
@allure.description("评估报告列表")
@allure.severity(allure.severity_level.NORMAL)
def test_2_bid_evaluated_report_module_list(get_token_fixture):
    """评估报告列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/bid/assessmentTemplate/getList"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评估报告")
@allure.description("评估报告模板详情")
@allure.severity(allure.severity_level.MINOR)
def test_3_bid_evaluated_report_module_detail(get_token_fixture):
    """评估报告模板详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":1 } #模板id
    url = URL + "/bid/assessmentTemplate/details"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()