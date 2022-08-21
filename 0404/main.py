from typing import Final

latin_alphabet: Final = "abcdefghijklmnopqrstuvwxyz"
cyrillic_alphabet: Final = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def encoding(fracture, str):
    str_list = list(str)
    for i in range(len(str_list)):
        if latin_alphabet.__contains__((str_list[i]).lower()):
            str_list[i] = latin_alphabet.__getitem__(
                -1 * (len(latin_alphabet) - latin_alphabet.index(str_list[i].lower()) - fracture))
        if cyrillic_alphabet.__contains__((str_list[i]).lower()):
            str_list[i] = cyrillic_alphabet.__getitem__(
                -1 * (len(cyrillic_alphabet) - cyrillic_alphabet.index(str_list[i].lower()) - fracture))
        if str[i].isupper():
            str_list[i] = str_list[i].upper()

    str = ''.join(str_list)
    return str


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example = "бAлbeЯ"
    print(example)
    print("-"*30)
    print(encoding(3, example))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
