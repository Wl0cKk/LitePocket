from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    MDButton:
        text: "Click Me"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    MyApp().run()
