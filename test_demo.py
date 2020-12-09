import pytest


def add_function(a, b):
    return a + b


# @pytest.mark.parametrize("a, b, expected", [
#     [1, 2, 3],
#     [2, 2, 4],
#     [1, 2, 2]
# ], ids=["int", "minus", "bigint"])


@pytest.mark.parametrize("a", [0, 1, 2])
@pytest.mark.parametrize("b", [3, 4, 5])
def test_add(a, b):
    # assert add_function(a, b) == expected
    print(f"测试数据组合： a->{a},b->{b}")
    # print("测试数据组合： a->%s,b->%s"%(a, b))
