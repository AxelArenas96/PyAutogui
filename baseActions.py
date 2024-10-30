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

    def key_tab(self):
        pt.press('tab')

    def search_image(self, image, confidence):
        search = pt.locateOnScreen(image, confidence)
        if search:
            x, y = pt.center(search)
            print('Imagen encontrada en las coordenadas: ', x, ',', y)
        else:
            print('Image not found...')

    def pause(self, time_seg):
        time.sleep(time_seg)

    def click(self, image, confidence):
        search = pt.locateOnScreen(image, confidence)
        if search:
            x, y = pt.center(search)
            self.pause(1)
            pt.click(x, y)
            print('clik at the position: ', x, ',', y)
        else:
            print('Image not found...')



