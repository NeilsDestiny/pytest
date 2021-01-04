import pytest

class TestCal:
    # 加法
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add):
        res = get_calc.add(get_add[0], get_add[1])
        # print(get_add)
        # 判断参数值是否为浮点数
        if isinstance(res,float):
            # 浮点数保留两位小数
            res = round(res,2)
        assert res == get_add[2]

    # 除法
    #order=-1 用例最后执行
    @pytest.mark.run(order=-1)
    def test_div(self, get_calc, get_div):
        try:
            res = get_calc.div(get_div[0], get_div[1])
        except Exception as e:
            print(e)
        # assert res == get_div[2]
        pytest


    # 减法
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub):
        res = get_calc.sub(get_sub[0], get_sub[1])
        assert res == get_sub[2]

    # 乘法
    def test_mul(self, get_calc, get_mul):
        res = get_calc.mul(get_mul[0], get_mul[1])
        assert res == get_mul[2]
