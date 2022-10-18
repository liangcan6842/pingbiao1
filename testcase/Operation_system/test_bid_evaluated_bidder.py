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
@allure.story("评标-投标人")
@allure.description("新增投标人")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bidder(get_token_fixture):
    """新增投标人"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0,  #投标人ID
        "name": "1018评标项目投标人",
        "bidOffer": '12000',  #投标报价（下浮费率）
        "projectId": 13  #项目id
    }
    url = URL + "/bid/bidder/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-投标人")
@allure.description("分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_2_paging_query(get_token_fixture):
    """分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "projectId": 13, #项目ID
        # "name": 0  #项目名称
    }
    url = URL + "/bid/bidder/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-投标人")
@allure.description("删除投标人")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_delete_bidder(get_token_fixture):
    """删除投标人"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [6]
    url = URL + "/bid/bidder/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-投标人")
@allure.description("导入投标人")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_import_bidder(get_token_fixture):
    """导入投标人"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "multipart/form-data;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 4}
    files = {"file": ('1234.xlsx', open('C:\\Users\\Administrator\\Desktop\\pingbiao1\\data\\1234.xlsx', 'rb'), 'application/xls')}
    url = URL + "/bid/bidder/import"
    res = requests.post(url=url, headers=headers,params=data,files=files).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-投标人")
@allure.description("导入模板下载")
@allure.severity(allure.severity_level.NORMAL)
def test_5_import_module_download(get_token_fixture):
    """导入模板下载"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/bid/bidder/template"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.mian()
