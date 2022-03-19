from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from home import HomeScreen
from view_media_file import ViewMediaFileScreen
from encrypted_files import EncryptedFilesScreen
import pickle
from kivy.clock import Clock
import random
ui = Builder.load_string("""
<MainScreenManager>:
""")
class MainScreenManager(ScreenManager):
    pass
class Xenosecure(MDApp):
    def storeKey(self):
        try:
            file_object = open("dbase.db", "rb")
        except:
            file_object = open("dbase.db", "wb")
            key = random.choice(list(range(1, 256)))
            pickle.dump({"key":key}, file_object)
    def build(self):
        self.storeKey()
        root = MainScreenManager()
        home_screen = HomeScreen()
        root.add_widget(home_screen)
        encrypted_screen = EncryptedFilesScreen()
        root.add_widget(encrypted_screen)
        view_media_file = ViewMediaFileScreen()
        root.add_widget(view_media_file)
        return root
if __name__ == "__main__":
    Xenosecure().run()