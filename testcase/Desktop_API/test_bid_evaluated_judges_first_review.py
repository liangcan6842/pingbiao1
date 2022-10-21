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
@allure.story("评标评委端")
@allure.description("保存填写内容")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_save_write_content(get_token_fixture):
    """保存填写内容"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [
      {
        # "id": 0,
        "status": 1,          #	状态,0:关闭,1:开启
        "bidderId": 11,        #biz_ebid_bidder投标人id
        "preliminaryId": 5,   #bid_review_preliminary表 初步评审配置id
        "judgesId": 3,        #biz_ebid_judges评审人id
        "projectId": 13,       #评标项目id
        "state": 1            #0-不通过，1-通过
      }
    ]
    url = URL + "/dst/bid/preliminary/review"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("下一步")
@allure.severity(allure.severity_level.NORMAL)
def test_2_next_step(get_token_fixture):
    """下一步"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bid/preliminary/nest"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("查询表格内容")
@allure.severity(allure.severity_level.NORMAL)
def test_3_query_sheet_content(get_token_fixture):
    """查询表格内容"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bid/preliminary/table"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("初步评审汇总")
@allure.severity(allure.severity_level.NORMAL)
def test_4_first_step_review_summary(get_token_fixture):
    """初步评审汇总"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bid/preliminary/summary"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()

