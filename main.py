from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton

class MainLayout(MDBoxLayout):
    pass

class Header(MDBoxLayout):
    pass

class Footer(MDBoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        Window.minimum_width = 240
        Window.minimum_height = 240
        self.title = "LitePocket"
        self.theme_cls.theme_style = "Dark"
        Builder.load_file('litepocket.kv')
        return MainLayout()

if __name__ == '__main__':
    MainApp().run()
