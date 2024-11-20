from pytest import mark
from src.cryptographic.cifra_de_cesar import caesar_cipher
from src.cryptographic.cifra_de_cesar import _remove_special_chars
from random import randint

def test_caesar_cipher1():
    text = "Ninguém nasce odiando outra pessoa pela cor de sua pele, por sua" \
           " origem ou ainda por sua religião. Para odiar, as pessoas " \
           "precisam aprender, e se podem aprender a odiar, elas podem ser " \
           "ensinadas a amar \nNelson Mandela"
    shift = randint(1, 100)
    encrypted_message = caesar_cipher(text, shift)
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    assert decrypted_message == _remove_special_chars(text)

@mark.parametrize(
'input, output, shift',
    [
        ('Ninguém nasce', 'qlqjxhp qdvfh', 3),
        ('pele, por', 'shoh, sru', 3),
        ('religião. Para odiar', 'uholjldr. sdud rgldu', 3),
        ('amar \nNelson', "dpdu \nqhovrq", 3)

    ]
)
def test_caesar_cipher2(input, output, shift):
    encrypted_message = caesar_cipher(input, shift)
    print(encrypted_message)
    assert encrypted_message == output

@mark.parametrize(
'input',
    [
        ('lingüiça'),
        ("Café"),
        ("área"),
        ("época"),
        ("relógio"),
        ("Ângulo"),
        ("você"),
        ("vovô"),
        ("karatê"),
        ("Às vezes")
    ]
)
def test_caesar_cipher3(input):
    shift = randint(1, 100)
    encrypted_message = caesar_cipher(input, shift)
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    assert decrypted_message == _remove_special_chars(input)
