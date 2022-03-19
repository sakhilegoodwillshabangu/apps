from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, WipeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from load import LoadingScreen
from kivymd.app import MDApp
from touch import TouchBox
from response import ResponseScreen
import time
import _thread as thread
ui = Builder.load_string("""
<UserRequestBox>:
    id:user_request_box
    size_hint_y:None
    height:"110dp"
    orientation:"vertical"
    padding:5
    md_bg_color:[60/float(255), 51/float(255), 129/float(255), 1]
    radius:[20, 20, 0, 0]
    MDBoxLayout:
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[40, 40, 40, 40]
            pos_hint:{"center_y":.5}
            md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
            MDLabel:
                id:first_letter
                text:"S"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        MDBoxLayout:
            orientation:"vertical"
            padding:"5dp", "0dp"
            MDLabel:
                id:email_address_label
                text:"sakhile@gmail.com"
                text_size:self.size
                halign:"left"
                valign:"middle"
                color:[180/float(255), 180/float(255), 180/float(255), 1]
            MDBoxLayout:
                MDIcon:
                    size_hint:None, None
                    size:"30dp", "30dp"
                    icon:"loupe"
                    theme_text_color:"Custom"
                    text_color:[130/float(255), 130/float(255), 135/float(255), 1]
                    pos_hint:{"center_y":.5}
                MDLabel:
                    id:amount_label
                    text:"Request amount is R1200"
                    text_size:self.size
                    halign:"left"
                    valign:"middle"
                    color:[130/float(255), 130/float(255), 135/float(255), 1]  
    MDBoxLayout:
        spacing:5
        Widget:
        ApproveButtonBox:
            root:user_request_box
            size_hint_x:None
            width:"100dp"
            size_hint_y:None
            height:"40dp"
            radius:[30, 30, 30, 30]
            md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
            pos_hint:{"center_y":.5}
            MDLabel:
                text:"Approve"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[0, 0, 0, 1]
        DeclineButtonBox:
            root:user_request_box
            size_hint_x:None
            width:"100dp"
            size_hint_y:None
            height:"40dp"
            radius:[30, 30, 30, 30]
            md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
            pos_hint:{"center_y":.5}
            MDLabel:
                text:"Decline"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        Widget:
<MoneyRequestsScreen>:
    name:"money_requests_screen"
    id:requests_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"5dp", "5dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[20, 20, 0, 0]
            size_hint_y:None
            height:"80dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"arrow-left-thick"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackHome()
            MDLabel:
                text:"Requests (0)"
                font_size:"23dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[0, 0, 20, 20]
            orientation:"vertical"
            ScreenManager:
                id:requests_body_screen_manager
                MDScreen:
                    name:"money_requests_user_list_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            size_hint:None, None
                            size:self.parent.size
                            bar_with:0
                            MoneyRequestsLayout:
                                root:requests_screen
                LoadingScreen:
""")
class ApproveButtonBox(TouchBox):
    def goToResponseScreen(self):
        time.sleep(3)
        response_screen = ResponseScreen()
        response_screen.previouse_screen = "money_requests_user_list_screen"
        self.root.parent.root.ids.requests_body_screen_manager.transition = SlideTransition(direction = "left")
        self.root.parent.root.ids.requests_body_screen_manager.add_widget(response_screen)
        self.root.parent.root.ids.requests_body_screen_manager.current = "response_screen"
        self.root.parent.remove_widget(self.root)
    def respondToTouch(self):
        self.root.parent.root.ids.requests_body_screen_manager.transition = SlideTransition(direction = "left")
        self.root.parent.root.ids.requests_body_screen_manager.current = "loading_screen"
        thread.start_new_thread(self.goToResponseScreen, ())
class DeclineButtonBox(TouchBox):
    def respondToTouch(self):
        print("Decline")
        print("Parent is : ", self.root.parent)
        self.root.parent.remove_widget(self.root)
class UserRequestBox(MDBoxLayout):
    pass
class MoneyRequestsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.requests_layout = [["mailaddress@gmail.com", "6000"], ["emailaddress@yahoo.com", "200"]]
        self.size_hint_y = None
        self.spacing = 5
        self.padding = ("5dp", "10dp")
        self.bind(minimum_height = self.setter("height"))
        for r_info in self.requests_layout:
            user_request_bar = UserRequestBox()
            user_request_bar.ids.first_letter.text = r_info[0][0].upper()
            user_request_bar.ids.email_address_label.text = r_info[0]
            user_request_bar.ids.amount_label.text = "Request amount is R" + r_info[1]
            self.add_widget(user_request_bar)
class MoneyRequestsScreen(MDScreen):
    def goBackHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
class TestApp(MDApp):
    def build(self):
        root = MoneyRequestsScreen()
        return root
if __name__ == "__main__":
    TestApp().run() 