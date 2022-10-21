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
        "name": "1018评标项目评委",      #姓名
        "idnum": "500231199912122453",     #身份证号码
        "company": "重庆审计",   #工作单位
        "phone": "15612345632",     #电话
        "remark": "评委签到"      #备注
    }
    url = URL + "/dst/bid/judges/signIn"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
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
        "img": "1018评标项目评委签字",       #签名图片
    }
    url = URL + "/dst/bid/judges/signQz"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("评审、技术评分")
@allure.severity(allure.severity_level.NORMAL)
def test_3_review_technology_score(get_token_fixture):
    """评审、技术评分"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
          "projectId": 13,  #项目id
          "bidderId": 11,   #投标人id
          "reviewDetailId": 29,  #详细评审id
          "score": 84  #分数
    }
    url = URL + "/dst/bid/judges/score"
    res = requests.post(url=url, headers=headers,json=data,).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("前一行是否打分完成")
@allure.severity(allure.severity_level.MINOR)
def test_4_previous_row_score(get_token_fixture):
    """前一行是否打分完成"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13,          #项目id
        "reviewDetailId": 24          #评审id
    }
    url = URL + "/dst/bid/judges/isFinish"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("下一步")
@allure.severity(allure.severity_level.MINOR)
def test_5_next_step(get_token_fixture):
    """下一步"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId": 13,   #项目id
        "type": 3,        #1-详细评审,2-商务评审,3-技术评审;(当前页面处于阶段)
        "nodeId":2
    }
    url = URL + "/dst/bid/judges/next"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("否决投标")
@allure.severity(allure.severity_level.MINOR)
def test_6_evaluated_report(get_token_fixture):
    """否决投标"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "bidderId": 11,   #投标人id
        "reason": "未到达初步评审要求",    #不符合审查标准的具体内容
        "other": "无",      #其他说明事项
        "remark": "321tqew"      #备注
    }
    url = URL + "/dst/bid/judges/veto"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
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
    url = URL + "/dst/bid/judges/lineChart"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
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
    url = URL + "/dst/bid/judges/getSummary"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
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
        "nodeId":3           #节点id
    }
    url = URL + "/dst/bid/judges/getReviewDetail"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("推荐候选人数量")
@allure.severity(allure.severity_level.NORMAL)
def test_10_recommend_candidate_number(get_token_fixture):
    """推荐候选人数量"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13,            #项目id
        "number":3                #候选人数量
    }
    url = URL + "/dst/bid/judges/referrerNum"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("评委决议")
@allure.severity(allure.severity_level.NORMAL)
def test_11_judge_decision(get_token_fixture):
    """评委决议"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":18,            #项目id
        "state":2                #	0：未决议；1：同意；2：不同意
    }
    url = URL + "/dst/bid/judges/resolution"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("获取评委决议")
@allure.severity(allure.severity_level.NORMAL)
def test_12_get_judge_decision(get_token_fixture):
    """获取评委决议"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13            #项目id
    }
    url = URL + "/dst/bid/judges/getResolution"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("否决投标人列表")
@allure.severity(allure.severity_level.NORMAL)
def test_13_vote_bidder_list(get_token_fixture):
    """否决投标人列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":18            #项目id
    }
    url = URL + "/dst/bid/judges/bidderList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("桌面端")
@allure.story("评标评委端")
@allure.description("评估报告")
@allure.severity(allure.severity_level.NORMAL)
def test_14_evaluate_report(get_token_fixture):
    """评估报告"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "projectId":13            #项目id
    }
    url = URL + "/dst/bid/judges/assessment"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()








if __name__ == '__main__':
    pytest.main()