from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.app import MDApp
from load import LoadingScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from credentials_checker import *
import time
from home import HomeScreen
from kivy.clock import Clock
from error_screen import ErrorScreen
import threading
ui = Builder.load_string("""
<LoginLoadingBox>:
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
<LoginScreen>:
    id:login_screen_object
    name:"login_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0/float(255)/float(255), 0/float(255), 0/float(255), 1]
        padding:5
        MDBoxLayout:
            radius:[20, 20, 0, 0]
            size_hint_y:None
            height:"100dp"
            padding:"10dp", "0dp"
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDLabel:
                text:"Xenopay"
                
                color:[1, 1, 1, 1]
                font_size:"25dp"
        MDBoxLayout:
            id:login_body_box_object
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[0, 0, 0, 0]
            MDBoxLayout:
                md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                orientation:"vertical"
                radius:[20, 20, 0, 0]
                ScreenManager:
                    id:login_body_screen_manager
                    MDScreen:
                        name:"login_body_screen"
                        MDBoxLayout:
                            root:login_screen_object
                            orientation:"vertical"
                            padding:"10dp", "5dp"
                            spacing:5
                            MDBoxLayout:
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:login_email_text_field
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
                                    id:login_password_text_field
                                    mode:"fill"
                                    icon_right:"key-variant"
                                    icon_left_color_normal:[0, 0, 0, 1]
                                    hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--account-password--"
                                    password:True
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            LoginButton:
                                id:login_button
                                root:login_screen_object
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                size_hint_y:None
                                height:"40dp"
                                radius:[30, 30, 30, 30]
                                root:login_screen_object
                                MDLabel:
                                    id:login_button_label
                                    text:"Login"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                                    pos_hint:{"center_x":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"40dp"
                                Widget:
                                Button:
                                    text:"Forgot Password"
                                    text_size:self.width, None
                                    halign:"center"
                                    background_color:[220/float(255), 220/float(255), 220/float(255), 1]
                                    background_normal:""
                                    background_down:""
                                    color:[0, 144/float(255), 255/float(255), 1]
                                    on_press:root.goToForgotPasswordScreen()
                            RegisterButton:
                                root:login_screen_object
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                size_hint_y:None
                                height:"40dp"
                                radius:[30, 30, 30, 30]
                                MDIconButton:
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    icon:"account-circle"
                                    size_hint:None, None
                                    size:"40dp", "40dp"
                                    pos_hint:{"center_y":.5}
                                MDLabel:
                                    text:"Register"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                                BoxLayout:
                                    size_hint:None, None
                                    size:"40dp", "40dp"
                            Widget:
                    LoadingScreen:
                    ErrorScreen:
                        id:error_screen_object
""")
class LoginLoadingBox(MDBoxLayout):
    pass
class LoginButton(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = 0
        self.touch = True
        self.error_message = ""
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
    def goToLoadingScreen(self):
        self.parent.root.ids.login_body_screen_manager.transition = SlideTransition(direction = "left")
        self.parent.root.ids.login_body_screen_manager.current = "loading_screen"
    def respondToTouch(self):
	    email = self.root.ids.login_email_text_field.text
	    password = self.root.ids.login_password_text_field.text
	    text_fields_check = checkUnfilledCredentials([email, password])
	    email_check = checkEmailQualification(email)
	    if not self.checkLoginCredentials(text_fields_check, email_check):
	        self.callDialog("Fill all text fields correctly!")
	    else:
	        self.params = {"email":email, "password":password}
	        if self.touch:
	            Clock.schedule_once(self.root.addLoading, 0)
	            Clock.schedule_once(self.root.makeRequest, 0)
	            Clock.schedule_once(self.root.determineNextScreen, 3)
    def checkLoginCredentials(self, text_fields_check, email_check):
        if not (text_fields_check and email_check):
            return 0
        else:
            return 1
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Login Error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        print("Dismiss button pressed")
        self.dialog.dismiss()
class RegisterButton(MDBoxLayout):
	def on_touch_down(self, touch):
		if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
			self.respondToTouch()
	def respondToTouch(self):
	    print("Hello world of Register")
	    self.root.parent.transition = SlideTransition(direction = "left")
	    self.root.parent.current = "sign_up_screen"
class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.touch = True
    def goToForgotPasswordScreen(self):
        self.parent.root.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.current = "forgot_password_screen"
    def addLoading(self, seconds):
        self.touch = False
        self.ids.login_button.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.ids.login_button_label.text = "Loading..."
        self.ids.login_button.add_widget(LoginLoadingBox())
    def unscheduleLoadingState(self):
        Clock.unschedule(self.addLoading)
        Clock.unschedule(self.makeRequest)
        Clock.unschedule(self.determineNextScreen)
        self.ids.login_button_label.text = "Login"
        self.ids.login_button.remove_widget(self.ids.login_button.children[0])
        self.ids.login_button.md_bg_color = [0, 154/float(255), 255/float(255), 1]
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
        if self.response == -2:
            Clock.schedule_once(self.createHomeScreen, 0)
            self.unscheduleLoadingState()
        elif self.response == 0:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.unscheduleLoadingState()
            self.response = -1
            self.callDialog(self.error_message, button)
            button.bind(on_release = self.close)
        elif self.response == 1:
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