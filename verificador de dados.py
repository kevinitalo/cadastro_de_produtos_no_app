import openpyxl
import pyautogui

workbook = openpyxl.load_workbook(r'C:\Users\Carol Kaust\Documents\lançamento de informações contabil\vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
# nome
    pyautogui.click(1698,859, duration=1.5)
    pyautogui.write(linha[0].value)
# produto
    pyautogui.click(1705,892, duration=1.5)
    pyautogui.write(linha[1].value)
# quantidade
    pyautogui.click(1710,924, duration=1.5)
    pyautogui.write(str(linha[2].value))
# categoria
    pyautogui.click(1787,957, duration=1.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(1627,993, duration=1.5)
    pyautogui.click(926,598, duration=1.5)