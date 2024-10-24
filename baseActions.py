import pyautogui as pt
import time
from PIL import Image

class BaseActios:
    def __init__(self):
        print('Iniciando...')

    def abrir_software(self):
        pt.press('win')
        time.sleep(1)

    def write_text(self, text):
        pt.typewrite(text)

    def key_enter(self):
        pt.press('enter')