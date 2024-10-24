from baseActions import BaseActios

class OpenVisionPlus:
    def __init__(self):
        self.pt = BaseActios()

    def vision_plus(self, text):
        self.pt.abrir_software()
        self.pt.write_text(text)
        self.pt.key_enter()



