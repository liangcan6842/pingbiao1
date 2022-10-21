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
@allure.story("评标监督人端")
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
        "projectId": 13,   #评标项目id
        "name": "1018评标监督人",       #名称
        "company": "重庆永投集团",    #工作单位
        "phone": "13212341234",      #电话
        "remark": "评标监督人签到"         #备注
    }
    url = URL + "/dst/bid/supervisor/signIn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
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
        "img": "1018评标监督人签字",       #签名图片
    }
    url = URL + "/dst/bid/supervisor/signQz"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("专家列表")
@allure.severity(allure.severity_level.NORMAL)
def test_3_expert_list(get_token_fixture):
    """专家列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"projectId": 13}
    url = URL + "/dst/bid/supervisor/judgesList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("查看初步评审")
@allure.severity(allure.severity_level.MINOR)
def test_4_look_first_step_review(get_token_fixture):
    """查看初步评审"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "judgesId":3          #选择评委id
    }
    url = URL + "/dst/bid/supervisor/judgesId"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("初步评审汇总")
@allure.severity(allure.severity_level.MINOR)
def test_5_first_step_review_summary(get_token_fixture):
    """初步评审汇总"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bid/supervisor/summary"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("评估报告")
@allure.severity(allure.severity_level.MINOR)
def test_6_evaluated_report(get_token_fixture):
    """评估报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"projectId":13}   #评标项目id
    url = URL + "/dst/bid/supervisor/assessment"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("折线图")
@allure.severity(allure.severity_level.MINOR)
def test_7_line_chart(get_token_fixture):
    """折线图"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id":2}   #评审项id
    url = URL + "/dst/bid/supervisor/lineChart"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("详细、商务评、技术评审汇总")
@allure.severity(allure.severity_level.NORMAL)
def test_8_detail_business_summary(get_token_fixture):
    """详细、商务评、技术评审汇总"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"projectId":13}   #项目id
    url = URL + "/dst/bid/supervisor/getSummary"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标监督人端")
@allure.description("详细、商务评、技术评审信息")
@allure.severity(allure.severity_level.NORMAL)
def test_9_detail_business_message(get_token_fixture):
    """详细、商务评、技术评审信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "nodeId":2,
        "judgesId":3     #专家id
    }
    url = URL + "/dst/bid/supervisor/getReviewDetail"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()








if __name__ == '__main__':
    pytest.main()