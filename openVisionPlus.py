from baseActions import BaseActios

class OpenVisionPlus:
    def __init__(self):
        self.pt = BaseActios()

    def vision_plus(self, text):
        self.pt.abrir_software()
        self.pt.write_text(text)
        self.pt.key_enter()

    def connect_to_vision(self, image, confidence):
        self.pt.pause(2)
        self.pt.search_image(image, confidence)
        self.pt.pause(2)
        self.pt.click(image, confidence)
        self.pt.pause(2)
        self.pt.write_text('UAM')
        self.pt.pause(1)
        self.pt.key_enter()

    def login(self, client, name, password):
        self.pt.pause(1)
        self.pt.write_text(client)
        self.pt.key_tab()
        self.pt.write_text(name)
        self.pt.key_tab()
        self.pt.write_text(password)
        self.pt.pause(1)
        self.pt.key_enter()


