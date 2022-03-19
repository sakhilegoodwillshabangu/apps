from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.app import MDApp
from touch import TouchBox
from kivy.lang import Builder
ui = Builder.load_string("""
<UserBarBox>:
    size_hint_y:None
    height:"60dp"
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    padding:5
    MDBoxLayout:
        id:circle
        size_hint:None, None
        size:"50dp", "50dp"
        md_bg_color:[0, 1, 0, 1]
        radius:[40, 40, 40, 40]
        MDLabel:
            id:name_first_letter
            text:"S"
            text_size:self.size
            halign:"center"
            valign:"middle"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:email_address
                text:"email@address"
                text_size:self.size
                halign:"left"
                valign:"middle"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:user_name
                text:"username"
                text_size:self.size
                halign:"left"
                color:[100/float(255), 100/float(255), 100/float(255), 1]
                valign:"middle"
    MDIconButton:
        id:icon_button
        size_hint:None, None
        size:"40dp", "40dp"
        pos_hint:{"center_x":.5, "center_y":.5}
        icon:"checkbox-multiple-blank-circle"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
<WhoToPayScreen>:
    name:"who_to_pay_screen"
    MDBoxLayout:
        orientation:"vertical"
        padding:"10dp", "5dp"
        md_bg_color:[0, 0, 0, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"130dp"
            md_bg_color:[72/float(255), 62/float(255), 139/float(255), 1]
            radius:[20, 20, 0, 0]
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                MDIconButton:
                    size_hint:None, None
                    size:"50dp", "50dp"
                    icon:"arrow-left-thick"
                    user_font_size:"30dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    pos_hint:{"center_x":.5, "center_y":.5}
                    on_release:root.goBackToPayScreen()
                MDLabel:
                    id:screen_title
                    text:"Who to pay?"
                    font_size:"23dp"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDBoxLayout:
                    size_hint_x:None
                    width:"50dp"
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                padding:"5dp", "0dp"
                MDTextField:
                    hint_text:"--email@address--"
                    mode:"fill"
                    icon_right:"send"
                    radius:[20, 20, 0, 0]
                    pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            orientation:"vertical"
            radius:[0, 0, 20, 20]
            md_bg_color:[72/float(255), 62/float(255), 139/float(255), 1]
            MDBoxLayout:
                ScreenManager:
                    id:body_screen_manager
                    MDScreen:
                        name:"request_someone_screen"
                        MDBoxLayout:
                            FloatLayout:
                                size_hint:None, None
                                size:self.parent.size
                                pos:self.parent.pos
                                MDBoxLayout:
                                    pos:self.parent.pos
                                    orientation:"vertical"
                                    MDBoxLayout:
                                        size_hint_y:None
                                        height:"40dp"
                                        padding:"0dp", "0dp", "5dp", "5dp"
                                        Widget:
                                        MDBoxLayout:
                                            size_hint_x:None
                                            width:"100dp"
                                            radius:[30, 30, 30, 30]
                                            md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                            MDLabel:
                                                text:"Request"
                                                text_size:self.size
                                                halign:"center"
                                                valign:"middle"
                                                color:[1, 1, 1, 1]
                                    MDBoxLayout:
                                        ScrollView:
                                            size_hint:None, None
                                            size:self.parent.size
                                            UsersRequestListLayout:
                                MDBoxLayout:
                                    pos:self.parent.pos
                                    padding:"10dp", "50dp"
                                    Widget:
                                    MDBoxLayout:
                                        size_hint_y:None
                                        height:"50dp"
                                        padding:5
                                        Widget:
                                        MDIconButton:
                                            size_hint:None, None
                                            size:"40dp", "40dp"
                                            icon:"motion"
                                            theme_text_color:"Custom"
                                            text_color:[1, 1, 1, 1]
                                            user_font_size:"20dp"
                                            md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                            on_press:root.goToViewYourRequests()
                    MDScreen:
                        name:"pay_someone_screen"
                        MDBoxLayout:
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"40dp"
                                padding:"0dp", "0dp", "5dp", "5dp"
                                Widget:
                                MDBoxLayout:
                                    size_hint_x:None
                                    width:"100dp"
                                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                    radius:[30, 30, 30, 30]
                                    MDLabel:
                                        text:"Send"
                                        text_size:self.size
                                        halign:"center"
                                        valign:"middle"
                                        color:[1, 1, 1, 1]
                            MDBoxLayout:
                                ScrollView:
                                    size_hint:None, None
                                    size:self.parent.size
                                    UsersPayListLayout:
            MDBoxLayout:
                size_hint_y:None
                height:"2dp"
""")
class UserBarBox(TouchBox):
    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
        self.pay_or_request = "pay"
    def respondToTouch(self):
        if self.ids.icon_button.icon == "checkbox-multiple-blank-circle":
            self.ids.icon_button.icon = "checkbox-multiple-marked-circle"
            self.ids.icon_button.text_color = [0, 154/float(255), 255/float(255), 1]
        else:
            self.ids.icon_button.icon = "checkbox-multiple-blank-circle"
            self.ids.icon_button.text_color = [255/float(255), 255/float(255), 255/float(255), 1]
class UsersRequestListLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.padding = "5dp", "5dp"
        self.size_hint_y = None
        self.search_list = []
        self.bind(minimum_height = self.setter("height"))
        for i in range(10):
            bar = UserBarBox()
            self.add_widget(bar)
    def addUsersOnList(self):
        for info in self.search_list:
            bar = UserBarBox()
            bar.ids.name_first_letter.text = info[0]
            bar.ids.email_address.text = info[1]
            bar.ids.user_name.text = info[2]
            bar.pay_or_request = "request"
            self.add_widget(bar)
class UsersPayListLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.users_list = []
        self.padding = "5dp", "5dp"
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        for i in range(10):
            bar = UserBarBox()
            self.add_widget(bar)
    def addUsersOnList(self):
        for info in self.users_list:
            bar = UserBarBox()
            bar.ids.name_first_letter.text = info[0]
            bar.ids.email_address.text = info[1]
            bar.ids.user_name.text = info[2]
            bar.pay_or_request = "pay"
            self.add_widget(bar)
class WhoToPayScreen(MDScreen):
    def goBackToUsers(self):
        self.ids.body_screen_manager.transition = SlideTransition(direction = "right")
        self.ids.body_screen_manager.current = "users_list_screen"
    def goBackToPayScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "pay_screen"
    def goToViewYourRequests(self):
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "my_money_requests"
class TestApp(MDApp):
    def build(self):
        root = WhoToPayScreen()
        return root
if __name__ == "__main__":
    TestApp().run()