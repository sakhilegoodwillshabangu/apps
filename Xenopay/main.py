from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.lang import Builder
from gateway import GatewayScreen
from home import HomeScreen
from forgot_password import ForgotPasswordScreen
ui = Builder.load_string("""
<MainScreenManager>:
    GatewayScreen:
    ForgotPasswordScreen:
""")
x = ["HoneybeePersonalUseRegular-YzBn4", 
        "LemonMilkBold-gx2B3", 
        "LibraryRecordsRegular-qZW66", 
        "LibraryRecordsRegular-qZW66", 
        "QuiteMagicalRegular-8VA2", 
        "StoryElementvRegular-X3RWa", 
        "VeganStylePersonalUse-5Y58", 
        "Amsterdam-ZVGqm", 
        "AngelesPersonalUseItalic-2Odz8", 
        "BeautifulPeoplePersonalUse-dE0g", 
        "CarandaPersonalUse-qLOq", 
        "FlorPersonalUseRegular-rgpoy", 
        "LucyTheCatRegular-Bg9x", 
        "VacationsInParadisePersonalUse-qwml"]
class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def addGatewayScreen(self, **kwargs):
        time.sleep(2)
        self.transition = SlideTransition(direction = "left")
        self.current = "gateway_screen"
class MainApp(MDApp):
    def build(self):
        return MainScreenManager()
if __name__ == "__main__":
    MainApp().run()