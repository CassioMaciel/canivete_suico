from src.polynomial.polynomial_evaluate import polynomial_evaluate
from pytest import mark


@mark.parametrize(
    'c, x, f_de_x',
    [
        ([-14, 5, 1], 2, 0),
        ([-25, 0, 13, 2], -6, 11),
        ([4, -5, 3], 4, 32),
        ([2, 0, -2, 1, 2, -7], 2, -190),
        ([2, 0, -2, 1, 2, -7], -2, 242),
    ]
)
def test_polinomial_evaluate(c, x, f_de_x):
    assert polynomial_evaluate(c, x) == f_de_x
