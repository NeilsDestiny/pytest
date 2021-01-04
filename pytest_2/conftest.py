import pytest
import yaml
import os
from pytest_2 import cal

# path = os.path.dirname(__file__) + "\data2.yml"
path = os.path.join("data2.yml")
# print(path)

with open(path,encoding='utf-8') as f:
    file = yaml.safe_load(f)
    my_data= file['datas']
    my_id = file['ids']

@pytest.fixture(scope='module')
def get_calc():
    # print('获取计算器实例')
    calc = cal.Calculators()
    print("\n开始计算")
    yield calc
    print("\n结束计算")

@pytest.fixture(params=my_data['add'], ids=my_id['add'])
def get_add(request):
    add_data = request.param
    # print(f"request.param的测试数据是：{add_data}")
    return add_data

@pytest.fixture(params=my_data['sub'], ids=my_id['sub'])
def get_sub(request):
    sub_data = request.param
    # print(f"request.param的测试数据是：{sub_data}")
    return sub_data

@pytest.fixture(params=my_data['mul'], ids=my_id['mul'])
def get_mul(request):
    mul_data = request.param
    return mul_data

@pytest.fixture(params=my_data['div'], ids=my_id['div'])
def get_div(request):
    div_data = request.param
    return div_data
