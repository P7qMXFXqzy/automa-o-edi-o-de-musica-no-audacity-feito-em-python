import pyautogui
import time
import pydirectinput

#abrir a janela do audacity
def focarEmAudacity():
    #mover o mouse para a posição do ícone da barra inferior e selecioná-lo
    pyautogui.moveTo(278, 754)
    time.sleep(0.5)
    pyautogui.click()

#abrir a janela do cmd
def focarNoCmd():
    pyautogui.moveTo(316, 754)
    time.sleep(0.5)
    pyautogui.click()

#executar o macro e exportar o arquivo como mp3
def aplicarMacroEExportar():
    pyautogui.moveTo(499, 34)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(549, 107)
    time.sleep(0.5)
    pyautogui.moveTo(809, 181)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(24, 33)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(57, 181)
    time.sleep(0.5)
    pyautogui.moveTo(319, 181)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('enter')

#função para músicas maiores que 1 minuto
def edicaoMaior():
    #definir em que direção ocorrerá a edição
    direcao = input("editar à frente ou atrás? (f/a) ")
    while(direcao != "f" and direcao != "a"):
        direcao = input("escolha inválida!\neditar à frente ou atrás? (f/a) ")
    input("selecione o ponto de partida e confirme")
    focarEmAudacity()
    #selecionar a minutagem e pressionar os botões correspondentes 
    if(direcao == "f"):
        pyautogui.moveTo(546, 698)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pydirectinput.press('up')
    else:
        pyautogui.moveTo(546, 674)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pydirectinput.press('down')
    #remover áreas não selecionadas
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.5)
    aplicarMacroEExportar()
    time.sleep(0.5)
    focarNoCmd()

#edição para músicas menores que 1 minuto
def edicaoMenor():
    #esperar confirmação e remover parte esquerda da música
    input("selecione a parte esquerda da música e confirme")
    focarEmAudacity()
    time.sleep(0.5)
    pyautogui.moveTo(500, 676)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pydirectinput.press('down')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(0.5)
    #abrir janela do cmd, esperar confirmação e remover parte esquerda da música
    focarNoCmd()
    input("selecione a parte direita da música e confirme")
    focarEmAudacity()
    time.sleep(0.5)
    pyautogui.moveTo(500, 699)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pydirectinput.press('up')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(0.5)
    aplicarMacroEExportar()
    time.sleep(0.5)
    focarNoCmd()