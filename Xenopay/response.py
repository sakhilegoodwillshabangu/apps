from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivymd.app import MDApp
from touch import TouchBox
from kivy.lang import Builder
ui = Builder.load_string("""
<ResponseScreen>:
    id:response_screen
    name:"response_screen"
    MDBoxLayout:
        md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
        orientation:"vertical"
        radius:[0, 0, 0, 0]
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:5
            BackButtonBox:
                root:response_screen
                size_hint:None, None
                size:"100dp", "40dp"
                radius:[30, 30, 30, 30]
                pos_hint:{"center_x":.5, "center_y":.5}
                md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
                MDLabel:
                    text:"Back"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
        Widget:
        IconSpaceBox:
            size_hint_y:None
            height:"100dp"
            Widget:
            MDIconButton:
                id:response_icon
                size_hint:None, None
                size:"100dp", "100dp"
                icon:"check"
                user_font_size:"90dp"
                theme_text_color:"Custom"
                text_color:[0, 255/float(255), 154/float(255), 1]
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"20dp"
            MDLabel:
                id:response_message
                text:"Money sent"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        Widget:
""")
class IconSpaceBox(TouchBox):
    def respondToTouch(self):
        pass
class BackButtonBox(TouchBox):
    def respondToTouch(self):
        self.root.parent.transition = SlideTransition(direction = "right")
        self.root.parent.current = self.root.previouse_screen
        #self.parent.transition = SlideTransition(direction = "right")
        #self.parent.current = self.previouse_screen
class ResponseScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.previouse_screen = ""
class Test(MDApp):
    def build(self):
        root = ResponseScreen()
        return root
if __name__ == "__main__":
    Test().run()