from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

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
        self.theme_cls.primary_palette = "White"
        Builder.load_file('litepocket.kv')
        return MainLayout()
    
    def on_start(self):
        self.root.ids.footer.ids.tabs.switch_tab(text="Receive")

if __name__ == '__main__':
    MainApp().run()
