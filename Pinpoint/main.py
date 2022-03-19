from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from gateway import GatewayScreen
from home import HomeScreen
import multiprocessing
ui = Builder.load_string("""
<MainScreenManager>:
    HomeScreen:
    GatewayScreen:
        id:gateway_screen
""")
class MainScreenManager(ScreenManager):
    pass
class TestApp(MDApp):
    def build(self):
        root = MainScreenManager()
        return root
if __name__ == "__main__":
    TestApp().run()