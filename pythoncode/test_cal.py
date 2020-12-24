import pytest
import yaml
from pythoncode.calculator import Calculator

with open('./data.yml') as f:
    file = yaml.safe_load(f)
    # 获取用例参数
    datas = file['datas']
    # 获取用例标题
    ids = file['ids']


class TestCal:

    def setup_class(self):
        print("\n开始计算")
        # 实例化计算器的类
        self.cal = Calculator()

    def teardown_class(self):
        print("\n结束计算")

    @pytest.mark.parametrize('a,b,exp', datas['add'], ids=ids['add'])
    def test_add(self, a, b, exp):
        res = self.cal.add(a, b)
        assert res == exp

    @pytest.mark.parametrize('a,b,exp', datas['sub'], ids=ids['sub'])
    def test_sub(self, a, b, exp):
        res = self.cal.sub(a, b)
        assert res == exp

    @pytest.mark.parametrize('a,b,exp', datas['mul'], ids=ids['mul'])
    def test_mul(self, a, b, exp):
        res = self.cal.mul(a, b)
        assert res == exp

    @pytest.mark.parametrize('a,b,exp', datas['div'], ids=ids['div'])
    def test_div(self, a, b, exp):
        res = self.cal.div(a, b)
        assert res == exp
