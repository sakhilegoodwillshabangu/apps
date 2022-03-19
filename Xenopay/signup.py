from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from credentials_checker import *
from home import HomeScreen
from kivy.clock import Clock
import _thread as thread
from error_screen import ErrorScreen
import time
ui = Builder.load_string("""
<SignUpLoadingBox>:
    size_hint:None, None
    size:"40dp", "40dp"
    Image:
        source:"load.gif"
        center:self.parent.center
        size:40, 40
        allow_stretch:True
        anim_delay:-1
        anim_loop:10000000000000000000000000
        anim_delay:0.01
<SignUpBodyPageScreen>:
    id:sign_up_page_screen_object
    name:"sign_up_page_screen"
    MDBoxLayout:
        md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
        MDBoxLayout:
            radius:[20, 20, 0, 0]
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            orientation:"vertical"
            padding:"10dp", "5dp"
            spacing:5
            MDBoxLayout:
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDTextField:
                    id:sign_up_names_text_field
                    mode:"fill"
                    icon_right:"account-circle"
                    icon_left_color_normal:[0, 0, 0, 1]
                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                    radius:[20, 20, 20, 20]
                    hint_text:"--full_names--"
                    pos_hint:{"center_x":.5, "center_y":.5}
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDTextField:
                    id:sign_up_last_name_text_field
                    mode:"fill"
                    icon_right:"account-circle"
                    icon_left_color_normal:[0, 0, 0, 1]
                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                    radius:[20, 20, 20, 20]
                    hint_text:"--surname--"
                    pos_hint:{"center_x":.5, "center_y":.5}
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDTextField:
                    id:sign_up_email_text_field
                    mode:"fill"
                    icon_right:"email"
                    icon_left_color_normal:[0, 0, 0, 1]
                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                    radius:[20, 20, 20, 20]
                    hint_text:"--email@address--"
                    pos_hint:{"center_x":.5, "center_y":.5}
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDTextField:
                    id:sign_up_password_one_text_field
                    mode:"fill"
                    icon_right:"key-variant"
                    icon_left_color_normal:[0, 0, 0, 1]
                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                    radius:[20, 20, 20, 20]
                    hint_text:"--create password--"
                    password:True
                    pos_hint:{"center_x":.5, "center_y":.5}
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                MDTextField:
                    id:sign_up_password_two_text_field
                    mode:"fill"
                    icon_right:"key-variant"
                    icon_left_color_normal:[0, 0, 0, 1]
                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                    radius:[20, 20, 20, 20]
                    hint_text:"--verify password--"
                    password:True
                    pos_hint:{"center_x":.5, "center_y":.5}
            SignUpFlatButton:
                id:sign_up_flat_button
                root:sign_up_page_screen_object
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                size_hint_y:None
                height:"40dp"
                radius:[30, 30, 30, 30]
                MDLabel:
                    id:sign_up_button_label
                    text:"Sign-up"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
            MDBoxLayout:
<SignUpScreen>:
    id:sign_up_screen_object
    name:"sign_up_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
        padding:5
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            padding:"0dp", "0dp"
            radius:[20, 20, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                icon:"chevron-left"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                color:[1, 1, 1, 1]
                user_font_size:"40dp"
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackToLoginScreen()
            MDLabel:
                text:"Xenopay"
                
                color:[1, 1, 1, 1]
                font_size:"25dp"
        MDBoxLayout:
            ScreenManager:
                root:sign_up_screen_object
                SignUpBodyPageScreen:
""")
class SignUpLoadingBox(MDBoxLayout):
    pass
class SignUpBodyPageScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = -1
        self.touch = True
    def addLoading(self, seconds):
        self.touch = False
        self.ids.sign_up_flat_button.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.ids.sign_up_button_label.text = "Loading..."
        self.ids.sign_up_flat_button.add_widget(SignUpLoadingBox())
    def unscheduleLoadingState(self):
        self.ids.sign_up_button_label.text = "Sign-up"
        self.ids.sign_up_flat_button.remove_widget(self.ids.sign_up_flat_button.children[0])
        self.ids.sign_up_flat_button.md_bg_color = [0, 154/float(255), 255/float(255), 1]
    def makeRequest(self, seconds):
        try:
            response = requests.get("http://localhost:8080/", params = self.params)
            if eval(response[0])  == 0:
                self.response = 1
            else:
                self.response = 0
                self.error_message = "Could'nt login user does'nt exist"
        except:
            self.response = -2
            self.error_message = "Network connection failure"
    def determineNextScreen(self, seconds):
        if self.response == 1:
            Clock.schedule_once(self.createHomeScreen, 0)
            self.unscheduleLoadingState()
        elif self.response == 0:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.error_message, button)
            button.bind(on_release = self.close)
        elif self.response == -2:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.error_message, button)
            button.bind(on_release = self.close)
        else:
            Clock.schedule_once(self.determineNextScreen, 0)
    def createHomeScreen(self, seconds):
        home_screen = HomeScreen()
        self.parent.add_widget(home_screen)
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "home_screen"
    def callDialog(self, text, button):
        self.dialog = MDDialog(title = "Login Error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        print("Dismiss button pressed")
        self.dialog.dismiss()
class SignUpScreen(MDScreen):
    def goBackToLoginScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "login_screen"
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
class SignUpFlatButton(TouchBox):
    def goToLoadingScreen(self):
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "loading_screen"
    def respondToTouch(self):
        names  = self.root.ids.sign_up_names_text_field.text
        last_name = self.root.ids.sign_up_last_name_text_field.text
        email = self.root.ids.sign_up_email_text_field.text
        password_one = self.root.ids.sign_up_password_one_text_field.text
        password_two = self.root.ids.sign_up_password_two_text_field.text
        print(names, last_name, email, password_one, password_two)
        text_fields_check = checkUnfilledCredentials([names, last_name, email, password_one, password_two])
        email_check = checkEmailQualification(email)
        password_check = checkPasswordQualification(password_one, password_two)
        if not text_fields_check:
            self.callDialog("Fill all text fields")
        elif not email_check:
            self.callDialog("Enter valid email address")
        elif not password_check:
            if len(password_one) < 8:
                self.callDialog("Password size should be atleast 8 characters")
            else:
                self.callDialog("Passwords don'nt match")
        else: 
            if self.root.touch:
                Clock.schedule_once(self.root.addLoading, 0)
                Clock.schedule_once(self.root.makeRequest, 0)
                Clock.schedule_once(self.root.determineNextScreen, 3)
    def checkSignUpCredentials(self, text_fields_check, email_check, check_password):
        if not (text_fields_check and email_check and check_password):
            return 0
        else:
            return 1
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Sign Up Error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()