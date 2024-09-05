import os
import sqlite3
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

class Header(MDBoxLayout):
    pass

class Footer(MDBoxLayout):
    pass

class MainLayout(MDBoxLayout):
    pass

class PreInstallationWindow(MDBoxLayout):
    pass

class LockScreenWindow(MDBoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        Window.minimum_width = 240
        Window.minimum_height = 240
        self.title = "LitePocket"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "White"

        if not self.first_entry_check():
            return self.show_pre_installation_dialog()
        else:
            Builder.load_file('litepocket.kv')
            return MainLayout()

    def on_start(self):
        if self.first_entry_check():
            self.root.ids.footer.ids.tabs.switch_tab(text="Receive")

    def first_entry_check(self):
        return os.path.exists('wallet.db')

    def show_pre_installation_dialog(self):
        Builder.load_file('pre_window.kv')
        return PreInstallationWindow()

    def generate_wallet(self):
        pass

    def restore_wallet(self):
        pass

    def backup_seed(self):
        pass

    def proceed_setup(self):
        pass

if __name__ == '__main__':
    MainApp().run()
