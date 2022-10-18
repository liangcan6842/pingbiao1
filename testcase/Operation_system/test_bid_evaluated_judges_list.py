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
@allure.story("评标-评委名单")
@allure.description("评委添加、修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_judges(get_token_fixture):
    """评委、添加修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        # "id": 0,  #修改必传
        "projectId":13 ,  #评标项目id
        "name": "1018评标项目评委",  #名称
        "company": "重庆审计",  #所在单位
        "macCode": "10181234",  #mac码
        "expired": "2022-10-25 17:00:00",  #时效时间
        "isLiable": 1   #是否是招标人评委（1：是；2：否）
    }
    url = URL + "/bid/judges/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评委名单")
@allure.description("删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_delete_judges(get_token_fixture):
    """删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = [4]
    url = URL + "/bid/judges/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评委名单")
@allure.description("评委分页查询")
@allure.severity(allure.severity_level.NORMAL)
def test_3_judges_paging_query(get_token_fixture):
    """评委分页查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "page": 1,
        "limit": 10,
        "projectId":13 , #评标项目id
        # "name": "" #名称
    }
    url = URL + "/bid/judges/page"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评委名单")
@allure.description("导入评委")
@allure.severity(allure.severity_level.NORMAL)
def test_4_import_judges(get_token_fixture):
    """导入评委"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "multipart/form-data;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13 , #评标项目id
        "file": "" #excel文件
    }
    url = URL + "/bid/judges/import"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评委名单")
@allure.description("修改状态")
@allure.severity(allure.severity_level.NORMAL)
def test_5_alter_judges_state(get_token_fixture):
    """修改状态"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "id":3 , #评委id
        "status": 1 #状态,0:关闭,1:开启
    }
    url = URL + "/bid/judges/updateStatus"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("业务系统")
@allure.story("评标-评委名单")
@allure.description("导入模板下载")
@allure.severity(allure.severity_level.NORMAL)
def test_6_download_import_module(get_token_fixture):
    """导入模板下载"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/bid/judges/template"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()









