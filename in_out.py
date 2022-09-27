# библтотека консольного ввода / вывода

import os


def input_int(msg: str) -> int:
    return int(input(msg))

def input_str(msg: str) -> str:
    return input(msg)

def input_float(msg: str) -> float:
    return float(input(msg))

def show_msg(msg: str) -> str:
    print(msg)
    os.system('pause')

