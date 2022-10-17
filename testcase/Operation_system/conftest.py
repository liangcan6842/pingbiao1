import pytest,requests,json
from ddt import ddt,file_data
from common.Package_file_method import read_yaml
URL = 'http://192.168.110.245:8887'

@pytest.fixture(scope="session")
def get_token_fixture():
    '''
    作用域为session的fixture函数，返回token
    :return:
    '''
    headers = {"Content-Type": "application/json;charset=utf8"}
    url = URL + "/login"
    data = {
        "username": "10000",
        "password": "123456"
    }
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    token = res["token"]
    return token