from openVisionPlus import OpenVisionPlus


if __name__ == '__main__':
    pt = OpenVisionPlus()
    pt.vision_plus('mocha')
    pt.connect_to_vision('resources/images/connect_button.png', confidence=0.9)
    pt.connect_to_vision('resources/images/uam.png', confidence=0.8)
    pt.login(client='765', name='V765UIDS02', password='Cqjdy*1010')





