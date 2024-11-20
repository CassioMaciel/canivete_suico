import re
import subprocess
from pytest import mark
import os


@mark.parametrize(
    'arquivo, rating',
    [
        ('.\\src\\bissexto.py', 10),
        ('.\\src\\fatorial.py', 10),
        ('.\\src\\fibonacci.py', 10),
        ('.\\src\\clear.py', 10),
        ('.\\src', 10),
    ],
)
def test_pylint(arquivo, rating):
    result = subprocess.run(
        ['pylint', arquivo],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    raw_message = result.stdout
    pattern = r'Your code has been rated at ([0-9]{1,2}.[0-9]{2})/10'
    rating = float(re.search(pattern, raw_message).group(1))

    assert rating >= rating , f'Unexpected Pylint rating:\n{result.stdout}'


@mark.parametrize(
    'arquivo',
    [
        ('.\\src\\bissexto.py'),
        ('.\\src\\fatorial.py'),
        ('.\\src\\fibonacci.py'),
        ('.\\src\\clear.py'),
        ('.\\src'),
    ],
)
def test_mypy(arquivo):
    result = subprocess.run(
        ['mypy', '--strict', arquivo],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(result.stdout)
    print(result.stderr)

    # Verificar se a execução foi bem-sucedida
    assert result.returncode == 0, f'mypy execution failed:\n{result.stderr}'
