import pytest
import yaml

from pythoncode.calculator import Calculator

with open('./data.yml') as f:
    data = yaml.safe_load(f)

class TestCal:
    # cal = Calculator()
    def setup_class(self):
        print("\n开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("\n结束计算")

    @pytest.mark.parametrize('a,b,exp', data['add'])
    def test_add(self, a, b, exp):
        res = self.cal.add(a, b)
        # print(res)
        assert res == exp

    @pytest.mark.parametrize('a,b,exp', data['sub'])
    def test_sub(self,a,b,exp):
        res =  self.cal.sub(a,b)
        assert res == exp