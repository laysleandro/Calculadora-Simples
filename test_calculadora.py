import sys
import os
import pytest 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import menu #aqui também podemos colocar outras funcoes a serem testadas

#teste de adição:
def test_adicao():
    assert 23 + 4 == 27

#teste de subtracao:
def test_diferenca():
    assert 455 - 40 == 415

#teste de multipicacao:
def test_multiplicacao():
    assert 25 * 4 == 100

#teste divisao:
def test_divisao():
    assert 10 / 5 == 2 

#teste divisao por zero: