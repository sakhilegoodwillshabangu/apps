from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<EncryptedFilesScreen>:
    name:"encrypted_files_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                icon:"arrow-left-thick"
                on_release:root.goBackToHomeScreen()
            MDLabel:
                text:"Encrypted Flles"
                font_size:"23dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            BoxLayout:
                size_hint_x:None
                width:"40dp"
        MDBoxLayout:
            radius:[40, 40, 0, 0]
            md_bg_color:[25/float(255), 25/float(255), 112/float(255), 1]
""")
class EncryptedFilesScreen(MDScreen):
    def goBackToHomeScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"