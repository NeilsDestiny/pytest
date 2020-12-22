import pytest


def inc(x):
    return x + 1


def test_answer():
    print("这是我的第一条测试用例")
    assert inc(3) == 4


def test_answer1():
    print("这是我的第二条测试用例")
    assert inc(4) == 5


if __name__ == '__main__':
    # -v输出更加详细的执行信息，-s是输入我们用例中的调式信息，比如print的打印信息
    pytest.main(['test_a.py','-v','-s'])

