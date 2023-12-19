import os
import pyautogui
from controlador import edicaoMaior, edicaoMenor
def perguntarDuracao():
    escolha = input("A música tem mais de 1 minuto? (s/n) ")
    while (escolha !="s" and escolha !="n"):
        escolha = input("Escolha inválida!\nA música tem mais de 1 minuto? (s/n) ")
    return escolha

def funcaoPrincipal():
    if(perguntarDuracao() == "s"):
        edicaoMaior()
    else:
        edicaoMenor()