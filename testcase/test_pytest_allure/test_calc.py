from testcase.test_pytest_allure.calc import Calculator
import pytest


class TestCalc():
    def setup_class(self):
        print("每个测试类执行前执行setup_class")

    def teardown_class(self):
        print("每个测试类执行后执行teardown_class")

    def setup(self):
        self.calc = Calculator()
        print("每个测试用例执行前执行setup")

    def teardown(self):
        print("每个测试用例执行后执行teardown")

    @pytest.mark.parametrize('a,b,c',[
        (1,1,2),
        (0.1,0.1,0.2),
        (-1,-1,-2),
        (2,2,3),
        (1000,1000,2000),
        (6,6,5)
    ])
    def test_add(self,a,b,c):
        assert c == self.calc.add(a,b)
