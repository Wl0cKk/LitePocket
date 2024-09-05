import os
import sqlite3
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

class MainLayout(MDBoxLayout):
    pass

class PreInstallationWindow(MDBoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        Window.minimum_width = 240
        Window.minimum_height = 240
        self.title = "LitePocket"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "White"
        
        if not self.first_entry_check():
            Builder.load_file('pre_window.kv')
            return PreInstallationWindow()
        else:
            Builder.load_file('litepocket.kv')
            return MainLayout()
    
    def first_entry_check(self):
        return os.path.exists('wallet.db')
    
    def on_start(self):
        if not self.first_entry_check():
            self.show_pre_installation_dialog()
        else:
            self.root.ids.footer.ids.tabs.switch_tab(text="Receive")
    
    def show_pre_installation_dialog(self):
        pass
        
    def generate_wallet(self):
        pass
    
    def restore_wallet(self):
        pass
    
    def backup_seed(self):
        pass
    
    def proceed_setup(self):
        pass

    def on_checkbox_active(self, checkbox, type_):
        if type_ == 'seed_phrase' and checkbox.active:
            self.root.ids.checkbox_private_key.active = False   
        elif type_ == 'private_key' and checkbox.active:
            self.root.ids.checkbox_seed_phrase.active = False

def setup_database(self):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wallets (
            id INTEGER PRIMARY KEY,
            private_key TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def proceed_setup(self):
    seed_phrase = self.root.ids.seed_phrase.text
    private_key = self.root.ids.private_key.text
    password = self.root.ids.password.text
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wallets (private_key, password) VALUES (?, ?)', (private_key, password))
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    MainApp().run()
