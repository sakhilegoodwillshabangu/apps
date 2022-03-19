from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
ui = Builder.load_string("""
<DigitButtonSpace>:
    radius:[10, 10, 10, 10]
    md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
    Widget:
    MDIconButton:
        id:digit_button_object
        size_hint:None, None
        size:"50dp", "50dp"
        user_font_size:"40dp"
        icon:"android"
        pos_hint:{"center_x":.5, "center_y":.5}
        on_release:root.punchDigit()
    Widget:
<UserBarBox>:
    size_hint_y:None
    height:"50dp"
    md_bg_color:[160/float(255), 160/float(255), 160/float(255), 1]
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        usr_font_size:"40dp"
        icon:"account-circle"
        pos_hint:{"center_x":.5, "center_y":.5}
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            MDLabel:
                text:"Full Names"
                color:[120/float(255), 120/float(255), 120/float(255), 1]
                text_size:self.size
                halign:"left"
                valign:"middle"
                font_size:"20dp"
        MDBoxLayout:
            MDLabel:
                text:"Relative"
                color:[120/float(255), 120/float(255), 120/float(255), 1]
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        user_font_size:"30dp"
        icon:"checkbox-multiple-blank-circle-outline"
        pos_hint:{"center_x":.5, "center_y":.5}
<SendMoneyScreen>:
    name:"send_money_screen"
    id:send_money_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 250/float(255), 154/float(255), 1]
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"40dp"
                pos_hint:{"center_x":.5, "center_y":.5}
                icon:"chevron-left"
                on_release:root.goBackToHome()
            MDLabel:
                text:"Send money"
                font_name:"Amsterdam-ZVGqm"
                font_size:"25dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
            MDBoxLayout:
                size_hint:None, None
                size:"50dp", "50dp"
        MDBoxLayout:
            orientation:"vertical"
            radius:[30, 30, 0, 0]
            md_bg_color:[230/float(255), 230/float(255), 230/float(255), 1]
            ScreenManager:
                Screen:
                    name:"input_amount_receiver_amount"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            orientation:"vertical"
                            padding:"10dp", "5dp"
                            spacing:5
                            MDBoxLayout:
                                size_hint_y:None
                                height:"50dp"
                                MDIconButton:
                                    size_hint:None, None
                                    size:"30dp", "30dp"
                                    user_font_size:"20dp"
                                    icon:"window-close"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                MDBoxLayout:
                            MDBoxLayout:
                                id:peers_links_space
                                ScrollView:
                                    size_hint:None, None
                                    size:peers_links_space.size
                                    ListOfPeers:
                            MDBoxLayout:
                                size_hint_y:None
                                height:"50dp"
                                padding:"0dp", "5dp"
                                MDBoxLayout:
                                    radius:[20, 20, 20, 20]
                                    md_bg_color:[0/float(255), 194/float(255), 255/float(255), 1]
                                    MDLabel:
                                        text:"Continue"
                                        color:[0, 0, 0, 1]
                                        text_size:self.size
                                        halign:"center"
                                        valign:"middle"
                Screen:
                    name:"punch_amount_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            MDLabel:
                                text:"R0"
                                bold:True
                                font_size:"18dp"
                                id:amount_punched
                                color:[72/float(255), 72/float(255), 72/float(255), 1]
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                        MDBoxLayout:
                            padding:"10dp", "0dp"
                            DigitLayout:
                                root:send_money_screen
                                id:digit_layout_object
                                cols:3
                                spacing:2
                                rows:4
                        MDBoxLayout:
                            size_hint_y:None
                            height:"50dp"
                            padding:5
                            MDBoxLayout:
                                md_bg_color:[0, 194/float(255), 255/float(255), 1]
                                radius:[20, 20, 20, 20]
                                MDLabel:
                                    text:"Send"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
""")
class SendMoneyScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.amount = "0"
    def goBackToHome(self):
        self.parent.ids.home_screen_object.switchOffAllButtons()
        self.parent.ids.home_screen_object.goToWalletScreen()
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
class DigitButtonSpace(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
        self.digit = 0
    def putDot(self):
        if "." in self.parent.root.ids.amount_punched.text:
            pass
        else:
            self.parent.root.ids.amount_punched.text = self.parent.root.ids.amount_punched.text + "."
            self.parent.root.amount = self.parent.root.amount + "."
    def cancel(self):
        if self.parent.root.ids.amount_punched.text != "R0":
            self.parent.root.ids.amount_punched.text = self.parent.root.ids.amount_punched.text[:-1]
            self.parent.root.amount = self.parent.root.amount[:-1]
            if self.parent.root.ids.amount_punched.text == "R":
                self.parent.root.ids.amount_punched.text = "R0"
        else:
            self.parent.root.amount = "0"
    def punchDigit(self):
        if self.digit >= 0:
            if self.parent.root.amount == "0":
                self.parent.root.ids.amount_punched.text = "R" + str(self.digit)
                self.parent.root.amount = str(self.digit)
            else:
                self.parent.root.ids.amount_punched.text = "R" + self.parent.root.ids.amount_punched.text[1:] + str(self.digit)
        else:
            if self.ids.digit_button_object.icon == "close":
                self.cancel()
            else:
                self.putDot()
class DigitLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        for i in range(9):
            icon_button_space = DigitButtonSpace()
            icon_button_space.digit = i + 1
            icon_button_space.ids.digit_button_object.icon = "numeric-" + str(i + 1)
            self.add_widget(icon_button_space)
        icon_button_space = DigitButtonSpace()
        icon_button_space.digit = -1
        icon_button_space.ids.digit_button_object.icon = "circle-medium"
        self.add_widget(icon_button_space)
        icon_button_space = DigitButtonSpace()
        icon_button_space.ids.digit_button_object.icon = "numeric-0"
        self.add_widget(icon_button_space)
        icon_button_space = DigitButtonSpace()
        icon_button_space.ids.digit_button_object.icon = "close"
        icon_button_space.digit = -1
        self.add_widget(icon_button_space)
class UserBarBox(MDBoxLayout):
    pass
class ListOfPeers(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        for i in range(10):
            user_bar = UserBarBox()
            self.add_widget(user_bar)