import pytest

from pythoncode.calculator import Calculator


class TestCalc(pytest):

    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expect", [
        [3, 5, 8],
        [4, 5, 9],
        [2, 5, 8]
    ], ids=["TURE", "TURE", "FLASE"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [3, 5, 5],
        [9, 5, 4],
        [7, 5, 2]
    ], ids=["FLASE","TURE", "TURE"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [3, 5, 15],
        [4, 5, 20],
        [3, 5, 11]
    ], ids=["TURE", "TURE", "FLASE"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [3, 1, 3],
        [2, 1, 2],
        [4, 1, 3]
    ], ids=["TURE", "TURE", "FLASE"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)

