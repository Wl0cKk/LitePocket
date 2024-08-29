from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window

class MainLayout(BoxLayout):
    pass

class Header(BoxLayout):
    pass

class Footer(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        Window.minimum_width = 240
        Window.minimum_height = 240
        self.title = "LitePocket"
        Builder.load_file('litepocket.kv')
        return MainLayout()

if __name__ == '__main__':
    MainApp().run()
