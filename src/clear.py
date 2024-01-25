"""
Used to clear the screen in terminal in different operating systems
If is windows, use the command cls
if is linux, use the command clear
"""
from os import system, name


def clear() -> None:
    """

    Limpa o terminal/console.

    Esta função detecta o sistema operacional e utiliza os comandos apropriados
     para limpar o terminal.
    Suporta Windows (cls) e sistemas baseados em Unix/Linux/Mac (clear).

    Exemplo de uso:
    >>> clear()
    """

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
