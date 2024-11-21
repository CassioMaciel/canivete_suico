# fonte : https://numerical.recipes/book.html pag 201
from typing import List
def polynomial_evaluate(c: List[float], x: float) -> float:
    '''
    these funcion evaluate the value of a polynomial of type
    y = c[0] + c[1]*x + c[2]*x^2 + c[3]*x^3 + c[4]*x^4+ ...

    >>> polynomial_evaluate([-14, 5, 1], 2)
    0
    '''

    index: int = 0
    y: float = 0           # Explicit is better than implicit
    for coeficiente in c:  # Other solution is with enumerate
        y += coeficiente * x ** index
        index += 1

    return y


if __name__ == '__main__':  # pragma no cover
    y = polynomial_evaluate([-14, 5, 1], -2.5)
    print(y)
