import subprocess
from pytest import mark


@mark.parametrize(
    'arquivo',
    [
        ('.\\src\\bhaskara.py'),
        ('.\\src\\bissexto.py'),
        ('.\\src\\fatorial.py'),
        ('.\\src\\fibonacci.py'),
        ('.\\src\\clear.py'),
    ],
)
def test_pylint(arquivo):
    result = subprocess.run(
        ['pylint', arquivo],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Verificar se a execução foi bem-sucedida
    assert result.returncode == 0, f'Pylint execution failed:\n{result.stderr}'

    # Verificar se a saída contém o rating esperado
    assert (
        'Your code has been rated at 10.00/10' in result.stdout
    ), f'Unexpected Pylint rating:\n{result.stdout}'


@mark.parametrize(
    'arquivo',
    [
        ('.\\src\\bhaskara.py'),
        ('.\\src\\bissexto.py'),
        ('.\\src\\fatorial.py'),
        ('.\\src\\fibonacci.py'),
        ('.\\src\\clear.py'),
    ],
)
def test_mypy(arquivo):
    result = subprocess.run(
        ['mypy', arquivo],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Verificar se a execução foi bem-sucedida
    assert result.returncode == 0, f'mypy execution failed:\n{result.stderr}'

    # Verificar se a saída contém o rating esperado
    assert (
        'Success: no issues found in 1 source file' in result.stdout
    ), f'issues found in mypy execution\n{result.stdout}'
