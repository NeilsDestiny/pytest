import pytest
# 创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("登录操作")
# 测试用例1：需要提前登录
def test_case1(login):
    print("测试用例1")
# 测试用例2：不需要提前登录
def test_case2():
    print("测试用例2")
# 测试用例3：需要提前登录
def test_case3(login):
    print("测试用例3")
# 测试用例4：不需要提前登录
def test_case4():
    print("测试用例4")
