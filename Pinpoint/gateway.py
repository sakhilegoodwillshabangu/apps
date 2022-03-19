from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
from home import HomeScreen
import requests
from kivymd.uix.button import MDIconButton
import pickle
import time
import _thread as thread
from kivy.clock import Clock
ui = Builder.load_string("""
<LoadingBox>:
    size_hint:None, None
    size:"50dp", "50dp"
    Image:
        source:"load.gif"
        center:self.parent.center
        size:50, 50
        allow_stretch:True
        anim_delay:-1
        anim_loop:10000000000000000000000000
        anim_delay:0.01
<AvaterButtonBox>:
    size_hint:None, None
    size:"80dp", "80dp"
    id:avater_root_box
    image:""
    MDFloatLayout:
        size_hint:None, None
        size:"80dp", "80dp"
        id:float
        pos:root.pos
        MDBoxLayout:
            pos:float.pos
            FitImage:
                id:avater_image
                size_hint:None, None
                size:"80dp", "80dp"
                radius:[70, 70, 70, 70]
                source:root.image
        MDBoxLayout:
            pos:float.pos
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"30dp"
                BoxLayout:
                MDBoxLayout:
                    padding:5
                    size_hint:None, None
                    size:"30dp", "30dp"
                    radius:[30, 30, 30, 30]
                    md_bg_color:[0.86, 0.86, 0.86, 1]
                    MDBoxLayout:
                        id:light_color
                        size_hint:None, None
                        size:"20dp", "20dp"
                        radius:[20, 20, 20, 20]
                        md_bg_color:[0.29, 0.29, 0.29, 1]
            MDBoxLayout:
<ContinueButtonBox>:
    id:continue_button_box
    radius:[40, 40, 40, 40]
    md_bg_color:[0, 154/float(255), 255/float(255), 1]
    MDBoxLayout:
        size_hint_x:None
        width:"50dp"
    MDLabel:
        id:button_text_label
        text:"Continue"
        color:[1, 1, 1, 1]
        text_size:self.size
        halign:"center"
        valign:"middle"
    MDIconButton:
        size_hint:None, None
        size:"50dp", "50dp"
        user_font_size:"30dp"
        icon:"arrow-right-thick"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
        pos_hint:{"center_x":.5, "center_y":.5}
<GatewayScreen>:
    id:gateway_screen
    name:"gateway_screen"
    ScreenManager:
        root:gateway_screen
        LoginScreen:
        SignUpScreen:
<SignUpScreen>
    name:"sign_up_screen"
    id:sign_up_screen
    MDBoxLayout:
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        orientation:"vertical"
        spacing:5
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
            radius:[0, 0, 40, 40]
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                pos_hint:{"center_y":.5}
                on_release:root.goBackToLoginScreen()
            MDLabel:
                text:"Pinpoint"
                font_size:"40dp"
                font_name:"HoneybeePersonalUseRegular-YzBn4"
                text_size:self.size
                halign:"center"
                valign:"middle"
            MDBoxLayout:
                size_hint_x:None
                width:"40dp"
        MDBoxLayout:
        MDBoxLayout:
            root:sign_up_screen
            orientation:"vertical"
            MDBoxLayout:
                root:sign_up_screen
                size_hint_y:None
                height:"90dp"
                padding:5
                spacing:10
                BoxLayout:
                AvaterButtonBox:
                    image:"female_avater_1.png"
                AvaterButtonBox:
                    image:"female_avater_2.png"
                AvaterButtonBox:
                    image:"female_avater_3.jpeg"
                BoxLayout:
            MDBoxLayout:
                root:sign_up_screen
                size_hint_y:None
                height:"90dp"
                padding:5
                spacing:10
                BoxLayout:
                AvaterButtonBox:
                    image:"male_avater_1.jpeg"
                AvaterButtonBox:
                    image:"male_avater_2.jpeg"
                AvaterButtonBox:
                    image:"male_avater_3.jpeg"
                BoxLayout:
        MDBoxLayout:
            padding:"10dp", "0dp"
            size_hint_y:None
            height:"70dp"
            MDTextField:
                id:user_name
                hint_text:"-@Username"
                mode:"fill"
                radius:[20, 20, 20, 20]
                icon_right:"account-circle"
                pos_hint:{"center_y":.5}
        MDBoxLayout:
            padding:"10dp", "0dp"
            size_hint_y:None
            height:"70dp"
            MDTextField:
                id:password
                hint_text:"-Password"
                mode:"fill"
                password:True
                radius:[20, 20, 20, 20]
                icon_right:"lock"
                pos_hint:{"center_y":.5}
        MDBoxLayout:
            padding:"10dp", "0dp"
            size_hint_y:None
            height:"70dp"
            MDTextField:
                id:verify_password
                hint_text:"-Verify password"
                mode:"fill"
                password:True
                radius:[20, 20, 20, 20]
                icon_right:"lock"
                pos_hint:{"center_y":.5}
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            padding:"10dp", "10dp"
            ContinueButtonBox:
                id:continue_button_box
                root:sign_up_screen
                screen:"sign_up"
<LoginScreen>:
    id:login_screen
    name:"login_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        padding:[0, 0, 0, 10]
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
            radius:[0, 0, 40, 40]
            MDLabel:
                text:"Pinpoint"
                font_name:"HoneybeePersonalUseRegular-YzBn4"
                text_size:self.size
                halign:"center"
                valign:"middle"
                font_size:"40dp"
        MDBoxLayout:
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            padding:"10dp", "0dp"
            MDTextField:
                id:user_name
                mode:"fill"
                radius:[20, 20, 20, 20]
                hint_text:"@Username"
                icon_right:"account-circle"
                hint_text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            padding:"10dp", "0dp"
            MDTextField:
                id:password
                mode:"fill"
                radius:[20, 20, 20, 20]
                password:True
                hint_text:"-password"
                icon_right:"lock"
                hint_text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                pos_hint:{"center_x":.5, "center_y":.5}
        Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:5
            RegisterButtonBox: 
                root:login_screen
                radius:[40, 40, 40, 40]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                MDBoxLayout:
                    size_hint_x:None
                    width:"40dp"
                MDLabel:
                    text:"Register"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    icon:"account-circle"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
        MDBoxLayout:
            size_hint_y:None
            height:"60dp"
            padding:5
            ContinueButtonBox:
                id:continue_button_box
                screen:"login"
                root:login_screen
                size_hint_y:None
                height:"50dp"
                radius:[40, 40, 40, 40]
""")
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        x_size = self.pos[0] + self.size[0]
        y_size = self.pos[1] + self.size[1]
        if ((touch.x > self.pos[0] and touch.x < x_size) and (touch.y > self.pos[1] and touch.y < y_size)):
            self.respondToTouch()
    def respondToTouch(self):
        pass
class LoadingBox(MDBoxLayout):
    pass
class RegisterButtonBox(TouchBox):
    def respondToTouch(self):
        self.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.current = "sign_up_screen"
class ContinueButtonBox(TouchBox):
    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
        self.touch = True
    def updateLoadingState(self, seconds):
        load = LoadingBox()
        self.remove_widget(self.children[0])
        self.add_widget(load)
        self.ids.button_text_label.text = "Loading..."
        self.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
    def unscheduleLoadingState(self):
        Clock.unschedule(self.updateLoadingState)
        self.remove_widget(self.children[0])
        icon_button = MDIconButton(size_hint = (None, None), size = ("50dp", "50dp"), 
                                                            user_font_size = "30dp", theme_text_color = "Custom", text_color = [1, 1, 1, 1], 
                                                            icon = "arrow-right-thick", pos_hint = {"center_x":.5, "center_y":.5})
        self.add_widget(icon_button)
        self.ids.button_text_label.text = "Continue"
        self.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
    def loginUser(self):
        user_name = self.root.ids.user_name.text
        password = self.root.ids.password.text
        button = MDFillRoundFlatButton(text = "Ok")
        button.bind(on_release = self.close)
        if user_name == "":
            self.openDialog("Login Error", "Enter your username", button)
        elif len(password) < 8:
            self.openDialog("Login Error", "Enter atleast 8 password characters", button)
        else:
            self.root.params = {"user_name":user_name, "password":password}
            Clock.schedule_once(self.updateLoadingState, 0)
            Clock.schedule_once(self.root.makeRequest, 0)
            Clock.schedule_once(self.root.determineNextScreen, 3)
    def registerUser(self):
        avater = self.root.avater_name
        user_name = self.root.ids.user_name.text
        password = self.root.ids.password.text
        verify_password = self.root.ids.verify_password.text
        button = MDFillRoundFlatButton(text = "Ok")
        button.bind(on_release = self.close)
        if avater == "":
            self.openDialog("SignUp Error", "Pick an avater", button)
        elif user_name == "":
            self.openDialog("SignUp Error", "Enter your username", button)
        elif len(password) < 8:
            self.openDialog("SignUp Error", "Enter atleast 8 password characters", button)
        elif password != verify_password:
            self.openDialog("SignUp Error", "Passwords don't match", button)
        else:
            self.root.params = {"user_name":user_name, "password":password, "image_name":avater}
            Clock.schedule_once(self.updateLoadingState, 0)
            Clock.schedule_once(self.root.makeRequest, 0)
            Clock.schedule_once(self.root.determineNextScreen, 3)
    def respondToTouch(self):
        if self.screen == "login":
            self.loginUser()
            print("Login Screen")
        else:
            print("Sign Up Screen")
            self.registerUser()
    def openDialog(self, title, text, button):
        self.dialog = MDDialog(title = title, text = text, 
                                                         buttons = [button])
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
class AvaterButtonBox(TouchBox):
    def turnOffAvaterLights(self):
        for _object in self.parent.parent.children[0].children[1:-1] + self.parent.parent.children[1].children[1:-1]:
            _object.ids.light_color.md_bg_color = [0.29, 0.29, 0.29, 1]
    def respondToTouch(self):
        self.turnOffAvaterLights()
        self.parent.root.avater_name = self.image
        if self.ids.light_color.md_bg_color == [0.29, 0.29, 0.29, 1]:
            self.ids.light_color.md_bg_color = [0, 255/float(255), 154/float(255), 1]
            self.parent.parent.root.avater_name = self.image
class FormBox(MDBoxLayout):
    pass
class SignUpLoginParent(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.route = "userPin/"
        self.response = -1
        self.params = {}
        self.location = ""
        self.dialog_title = ""
        self.error_message = ""
    def createHomeScreen(self, seconds):
        home_screen = HomeScreen()
        home_screen.id = self.id
        home_screen.ids.map_screen.id = self.id
        try:
            home_screen.location = self.location
            home_screen.ids.map_screen.ids.map.lat = self.location[0]
            home_screen.ids.map_screen.ids.map.lon = self.location[1]
        except:
            pass
        home_screen.ids.my_avater = self.root.avater_name
        self.parent.root.parent.add_widget(home_screen)
        self.parent.root.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.current = "home_screen"
        print("Last line of threading")
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/" + self.route, params = self.params).text)
            if response[0]  == 1:
                self.response = 1
                self.id = response[1]
                self.parent.root.share_rule = response[2]
                try:
                    response_two = eval(requests.get("http://localhost:8080/userPin/fetchLocation/", params = {"user_id":self.id}).text)
                    if not response_two[1] == "":
                        self.location = eval(response_two[1])
                except:
                    pass
            else:
                self.response = 0
                self.error_message = "Could'nt register username taken"
        except:
            self.response = -2
            self.error_message = "Network connection failure"
    def determineNextScreen(self, seconds):
        if self.response == 1:
            Clock.schedule_once(self.createHomeScreen, 0)
            self.ids.continue_button_box.unscheduleLoadingState()
        elif self.response == 0:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.ids.continue_button_box.unscheduleLoadingState()
            self.response = -1
            self.openDialog(self.dialog_title, self.error_message, button)
            button.bind(on_release = self.close)
        elif self.response == -2:
            button = MDFillRoundFlatButton(text = "Ok")
            self.touch = True
            self.ids.continue_button_box.unscheduleLoadingState()
            self.response = -1
            self.openDialog(self.dialog_title, self.error_message, button)
            button.bind(on_release = self.close)
        else:
            Clock.schedule_once(self.determineNextScreen, 0)
    def openDialog(self, title, text, button):
        self.dialog = MDDialog(title = title, text = text, 
                                                         buttons = [button])
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
class SignUpScreen(SignUpLoginParent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.route = "userPin/register/"
        self.avater_name = ""
        self.dialog_title = "SignUp Error"
    def goBackToLoginScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "login_screen"
class LoginScreen(SignUpLoginParent):
    def __init__(self, **kwargs):
        self.route = "userPin/login/"
        super().__init__(**kwargs)
        self.dialog_title = "Login Error"
class GatewayScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.share_rule = "friends"