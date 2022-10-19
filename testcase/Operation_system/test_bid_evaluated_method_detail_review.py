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
@allure.story("评标办法-详细评审")
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
        "status": 1,        #	状态,0:关闭,1:开启
        "type": 1,          #1-详细评审，2-商务评审，3-技术评审
        "name": "专业程度打分",         #评分项名称
        "serialNumber": 1,       #序号
        "reviewStandard": "平均分达到70分即通过",    #评审标准
        "scoreType": "直接打分",        #打分方式：直接打分
        "unifiedScore": 1,      #是否检验统一打分：1-是，0-否
        "minScore": 65,              #最低分
        "maxScore": 85,          #最高分
        "projectId": 13          #项目id
    }
    url = URL + "/v1/bidReviewDetail/add"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-详细评审")
@allure.description("列表查询")
@allure.severity(allure.severity_level.NORMAL)
def test_2_bid_evaluated_method_list_query(get_token_fixture):
    """列表查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/v1/bidReviewDetail/list"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-详细评审")
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
        "id": 24,
        "status": 1,        #	状态,0:关闭,1:开启
        "type": 3,          #1-详细评审，2-商务评审，3-技术评审
        "name": "技术等级打分",         #评分项名称
        "serialNumber": 2,       #序号
        "reviewStandard": "平均分达到70分即通过",    #评审标准
        "scoreType": "直接打分",        #打分方式：直接打分
        "unifiedScore": 1,      #是否检验统一打分：1-是，0-否
        "minScore": 68,              #最低分
        "maxScore": 90,          #最高分
        "projectId": 13          #项目id
    }
    url = URL + "/v1/bidReviewDetail/update"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标办法-详细评审")
@allure.description("删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_delete_bid_evaluated_method(get_token_fixture):
    """删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 22}
    url = URL + "/v1/bidReviewDetail/delete"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()