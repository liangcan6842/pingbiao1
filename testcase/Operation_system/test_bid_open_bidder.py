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
@allure.story("开标-投标人")
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
        # "id": 0, #修改必传
        "name": "1018投标人43657",
        "expired": "2022-10-25 22:10:00",
        "projectId": 4
    }
    url = URL + "/biz/bidder/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
@allure.description("分页查询")
@allure.severity(allure.severity_level.CRITICAL)
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
        "bizProjectId": 4, #项目ID
        # "name": 0  #项目名称
    }
    url = URL + "/biz/bidder/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
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
    url = URL + "/biz/bidder/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
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
    url = URL + "/biz/bidder/import"
    res = requests.post(url=url, headers=headers,params=data,files=files).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
@allure.description("导入模板下载")
@allure.severity(allure.severity_level.NORMAL)
def test_5_import_module_download(get_token_fixture):
    """导入模板下载"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/biz/bidder/template"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
@allure.description("上传投标文件")
@allure.severity(allure.severity_level.CRITICAL)
def test_6_upload_bid_file(get_token_fixture):
    """上传投标文件"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 4, "tenderFile": "投标文件" }
    url = URL + "/biz/bidder/tender"
    res = requests.post(url=url,headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("开标-投标人")
@allure.description("启用-禁用")
@allure.severity(allure.severity_level.NORMAL)
def test_7_enable_disable(get_token_fixture):
    """启用-禁用"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {"id": 4}
    url = URL + "/biz/bidder/tender"
    res = requests.post(url=url,headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.mian()
