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
@allure.story("开标主持人端")
@allure.description("签字")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_signature(get_token_fixture):
    """签字"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "signImage": "1019开标主持人人签名图片432654277",       #签名图片
    }
    url = URL + "/dst/bido/host/sign"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标主持人端")
@allure.description("保存开标记录表内容")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_save_bid_open_record_sheet(get_token_fixture):
    """保存开标记录表内容"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[
          {
            # "id": 0,
            "sn": 1,           #序号
            "bidderId": 5,     #投标人ID
            "bidderName": "1018投标人",  #投标人名称
            "files": "5",       #投标文件份数
            "price": "100000",       #投标报价
            "d1Value": "投标表格值1",     #动态表格1值
            "d2Value": "投标表格值2",     #动态表格2值
            "d3Value": "投标表格值3",     #动态表格3值
            "signImg": "lucky"      #签字
          }
       ]
    url = URL + "/dst/bido/host/save"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标主持人端")
@allure.description("保存异议回复记录")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_save_bid_open_dissent_reply_record(get_token_fixture):
    """保存开标记录表内容"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data ={
        "projectId": 4,  #项目ID
        "replies": "开标项目存在的异议"    #回复
    }
    url = URL + "/dst/bido/host/reply"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标主持人端")
@allure.description("删除内容")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_delete_content(get_token_fixture):
    """删除内容"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data =[]
    url = URL + "/dst/bido/host/delete"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("开标主持人端")
@allure.description("查看开标记录表")
@allure.severity(allure.severity_level.MINOR)
def test_5_look_bid_open_record_sheet(get_token_fixture):
    """查看开标记录表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    url = URL + "/dst/bido/host/create"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()