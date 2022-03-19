from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.button import MDIconButton
from touch import TouchBox
ui = Builder.load_string("""
<PayScreen>:
    name:"pay_screen"
    id:pay_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"10dp", "10dp"
        spacing:10
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                theme_text_color: "Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                icon:"arrow-left-thick"
                on_release:root.goBackToHomeScreen()
            MDLabel:
                text:"Pay"
                font_size:"23dp"
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[20, 20, 20, 20]
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                MDLabel:
                    text:"R0"
                    font_size:"24dp"
                    bold:True
                    color:[1, 1, 1, 1]
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    id:amount
            MDBoxLayout:
                root:pay_screen
                MDBoxLayout:
                DigitLayout:
                    size_hint_x:None
                    width:"300dp"
                    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                    radius:[20, 20, 20, 20]
                MDBoxLayout:
            MDBoxLayout:
                root:pay_screen
                size_hint_y:None
                height:"60dp"
                padding:"10dp", "10dp"
                spacing:5
                RequestButtonBox:
                SendButtonBox:
<DigitButtonBox>:
    size_hint_x:None
    width:"100dp"
    padding:"20dp", "0dp"
<ButtonBox>:
    text:""
    size_hint_y:None
    height:"40dp"
    radius:[30, 30, 30, 30]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    MDLabel:
        text:root.text
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:[1, 1, 1, 1]
<SendButtonBox>:
    text:"Send"
<RequestButtonBox>:
    text:"Request"
""")
class ButtonBox(TouchBox):
    pass
class SendButtonBox(ButtonBox):
    def respondToTouch(self):
        try:
            if float(self.parent.root.amount) > 0:
                self.parent.root.parent.transition = SlideTransition(direction = "left")
                self.parent.root.parent.current = "who_to_pay_screen"
                self.parent.root.parent.ids.who_to_pay_object.ids.screen_title.text = "Who to Pay?"
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.transition = NoTransition()
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.current = "pay_someone_screen"
        except:
            pass
class RequestButtonBox(ButtonBox):
    def respondToTouch(self):
        try:
            if float(self.parent.root.amount) > 0:
                self.parent.root.parent.transition = SlideTransition(direction = "left")
                self.parent.root.parent.current = "who_to_pay_screen"
                self.parent.root.parent.ids.who_to_pay_object.ids.screen_title.text = "Who to Request?"
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.transition = NoTransition()
                self.parent.root.parent.ids.who_to_pay_object.ids.body_screen_manager.current = "request_someone_screen"
        except:
            pass
class DigitButtonBox(MDBoxLayout):
    pass
class DigitLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 4
        self.putDigit()
    def putDigit(self):
        for char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0", "*"]:
            print("Character : ", char)
            if char == "*":
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "close", user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.cancel)
            elif char == ".":
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "circle-small", user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.enterDot)
            else:
                button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"),
                                                           icon = "numeric-" + char, user_font_size = "30dp", pos_hint = {"center_x":.5}, 
                                                           theme_text_color = "Custom", text_color = [1, 1, 1, 1])
                button.bind(on_press = self.enterDigit)
            digit_button = DigitButtonBox()
            digit_button.add_widget(button)
            self.add_widget(digit_button)
    def enterDigit(self, button):
        number = button.icon[-1]
        print("Number :", number )
        if self.parent.root.amount == "":
           if number == "0":
                return
        self.parent.root.amount = self.parent.root.amount + number
        print("Amount : ", self.parent.root.amount)
        self.parent.root.ids.amount.text = "R" + self.parent.root.amount
        print("Label text : ", self.parent.root.ids.amount.text)
    def enterDot(self, button):
        if "." not in self.parent.root.amount:
            if self.parent.root.amount == "":
                self.parent.root.amount = "0."
            else:
                self.parent.root.amount = self.parent.root.amount + "."
        self.parent.root.ids.amount.text = "R" + self.parent.root.amount
    def cancel(self, button):
        if self.parent.root.amount == "0" or self.parent.root.amount == "":
            self.parent.root.amount = ""
        elif len(self.parent.root.amount) == 1:
            self.parent.root.amount = ""
            self.parent.root.ids.amount.text = "R0"
        else:
            print("amount length : ", len(self.parent.root.amount))
            if (self.parent.root.amount[0]  == "0") and (len(self.parent.root.amount) == 2):
                print("The length is 2 indeed")
                self.parent.root.amount = ""
                self.parent.root.ids.amount.text = "R0"
            else:
                self.parent.root.amount = self.parent.root.amount[:-1]
                self.parent.root.ids.amount.text = "R" + self.parent.root.amount
class PayScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.amount = ""
    def goBackToHomeScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"