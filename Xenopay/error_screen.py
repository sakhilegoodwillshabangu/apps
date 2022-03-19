from kivymd.app import MDApp
from touch import TouchBox
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<ErrorScreen>:
    id:error_screen
    name:"error_screen"
    MDBoxLayout:
        md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:"10dp", "0dp"
            OkButton:
                root:error_screen
                size_hint_x:None
                width:"100dp"
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                radius:[30, 30, 30, 30]
                MDLabel:
                    text:"Ok"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
        MDBoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"100dp", "100dp"
            user_font_size:"90dp"
            icon:"emoticon-cry"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            pos_hint:{"center_x":.5, "center_y":.5}
        MDLabel:
            text:"Network error!"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
        MDBoxLayout:
""")
class OkButton(TouchBox):
    def respondToTouch(self):
        self.root.parent.transition = SlideTransition(direction = "right")
        self.root.parent.current = self.root.previous_screen
class ErrorScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.previous_screen = ""