"""
This module does a cesar cypher in the function 
    cifra_de_cesar
"""
import re



def caesar_cipher(message: str, shift: int = 3) -> str:
    """
    This function do the Caesar cipher of a text
    :param message: the text to be encrypted
    :param shift: The rot number of the cypher
    :return: cyphed message
    """
    mensagem_criptografada: str = ""
    letra: str
    for letra in message:
        letra = _remove_special_chars(letra)
        if re.match(r'[ \n.,$*&%#@!?;:]', letra) is not None:
            mensagem_criptografada += letra
            continue
        alphabet_position = _letter_to_number(letra)
        alphabet_position += shift
        letra = _number_to_letter(alphabet_position)
        mensagem_criptografada += letra

    return mensagem_criptografada


def _number_to_letter(entrada: int) -> str:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    index = entrada % len(alphabet)
    return alphabet[index-1]


def _letter_to_number(entrada: str) -> int:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    number: int = alphabet.index(entrada[0])+1
    return number


def _remove_special_chars(string: str) -> str:
    string = string.lower()
    string = re.sub(r'[ãáàâ]', "a", string)
    string = re.sub(r'[éêè]', "e", string)
    string = re.sub(r'[íîì]', "i", string)
    string = re.sub(r'[óõôò]', "o", string)
    string = re.sub(r'[úûùü]', "u", string)
    string = re.sub(r'[ç]', "c", string)

    return string


if __name__ == '__main__': # pragma no cover
    MSG = "Ninguém nasce odiando outra pessoa pela cor de sua pele, por sua" \
           " origem ou ainda por sua religião. Para odiar, as pessoas " \
           "precisam aprender, e se podem aprneder a odia, elas podem ser " \
           "ensinadas a amar \nNelson Mandela"
    crip_mesage = caesar_cipher(MSG, 3)
    print(crip_mesage)
    descriptogrado = caesar_cipher(crip_mesage, -3)
    print(descriptogrado)
