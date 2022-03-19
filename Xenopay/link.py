from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
from touch import TouchBox
import _thread as thread
import time
from load import LoadingScreen
uix = Builder.load_string("""
<LinkUserButtonBox>:
    size_hint_y:None
    height:"50dp"
    md_bg_color:[0, 154/float(255), 255/float(255), 1]
    radius:[30, 30, 30, 30]
    BoxLayout:
        size_hint_x:None
        width:"50dp"
    MDLabel:
        text:"Link user"
        color:[1, 1, 1, 1]
        text_size:self.size
        halign:"center"
        valign:"middle"
        bold:True
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        icon:"arrow-right-thick"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
        pos_hint:{"center_x":.5, "center_y":.5}
<LinkUserScreen>:
    id:link_user_screen
    name:"link_user_screen"
    MDBoxLayout:
        orientation:"vertical"
        spacing:5
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_y":.5}
                on_release:root.goBackToMenuScreen()
        MDBoxLayout:
            ScreenManager:
                id:body_screen_manager
                Screen:
                    name:"link_sub_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"80dp"
                            MDTextField:
                                id:email_address_text_field
                                hint_text:"--email@address.com--"
                                mode:"fill"
                                radius:[20, 20, 0, 0]
                                icon_right:"email"
                                pos_hint:{"center_x":.5, "center_y":.5}
                        MDBoxLayout:
                            size_hint_y:None
                            height:"80dp"
                            MDTextField:
                                id:user_name_text_field
                                hint_text:"--username--"
                                mode:"fill"
                                radius:[20, 20, 0, 0]
                                icon_right:"account-circle"
                                pos_hint:{"center_x":.5, "center_y":.5}
                        LinkUserButtonBox:
                            root:link_user_screen
                        Widget:
                LoadingScreen:
""")
class LinkUserButtonBox(TouchBox):
    def respondToTouch(self):
        loading_screen = LoadingScreen()
        self.root.ids.body_screen_manager.add_widget(loading_screen)
        self.root.ids.body_screen_manager.transition = SlideTransition(direction = "left")
        self.root.ids.body_screen_manager.current = "loading_screen"
        thread.start_new_thread(loading_screen.ids.loading_grid.walkBoxes, ())
class LinkUserScreen(MDScreen):
    def goBackToMenuScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "menu_screen"