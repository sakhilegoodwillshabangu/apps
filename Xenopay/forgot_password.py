from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from client_request import request
from credentials_checker import *
from load import LoadingScreen
import _thread as thread
from error_screen import ErrorScreen
ui = Builder.load_string("""
<ForgotPasswordScreen>:
    id:forgot_password_screen
    name:"forgot_password_screen"
    MDBoxLayout:
        md_bg_color:[0, 0/float(255), 0/float(255), 1]
        padding:5
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            radius:[20, 20, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"40dp"
                icon:"chevron-left"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackToLogin()
            MDLabel:
                text_size:self.size
                halign:"left"
                valign:"middle"
                text:"Recover password"
                font_size:"23dp"
                color:[1, 1, 1, 1]
            BoxLayout:
                size_hint:None, None
                size:"50dp", "50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            ScreenManager:
                root:forgot_password_screen
                id:password_recovery_body_screen_manager
                Screen:
                    name:"email_screen"
                    MDBoxLayout:
                        radius:[20, 20, 0, 0]
                        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                        spacing:5
                        padding:"10dp", "5dp"
                        orientation:"vertical"
                        BoxLayout:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"70dp"
                            MDTextField:
                                id:user_email_text_field
                                mode:"fill"
                                icon_right:"email"
                                icon_left_color_normal:[0, 0, 0, 1]
                                hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                                radius:[20, 20, 20, 20]
                                hint_text:"--email@address--"
                                pos_hint:{"center_x":.5, "center_y":.5}
                        ForgotPasswordEmailButton:
                            screen_manager:password_recovery_body_screen_manager
                            md_bg_color:[0, 154/float(255), 255/float(255), 1]
                            size_hint_y:None
                            height:"40dp"
                            radius:[30, 30, 30, 30]
                            root:forgot_password_screen
                            MDLabel:
                                text:"Continue"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                                pos_hint:{"center_x":.5}
                        BoxLayout:
                Screen:
                    name:"recreate_password_screen"
                    MDBoxLayout:
                        radius:[20, 20, 0, 0]
                        spacing:5
                        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                        padding:"10dp", "5dp"
                        orientation:"vertical"
                        BoxLayout:
                        MDBoxLayout:
                            size_hint_y:None
                            height:"70dp"
                            MDTextField:
                                id:confirmation_code_text_field
                                mode:"fill"
                                icon_right:"barcode-scan"
                                icon_left_color_normal:[0, 0, 0, 1]
                                hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                                radius:[20, 20, 20, 20]
                                hint_text:"--Confirmation code--"
                                pos_hint:{"center_x":.5, "center_y":.5}
                        MDBoxLayout:
                            size_hint_y:None
                            height:"70dp"
                            MDTextField:
                                id:new_password_text_field
                                mode:"fill"
                                icon_right:"key-variant"
                                icon_left_color_normal:[0, 0, 0, 1]
                                hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                                radius:[20, 20, 20, 20]
                                hint_text:"--New Password--"
                                password:True
                                pos_hint:{"center_x":.5, "center_y":.5}
                        MDBoxLayout:
                            size_hint_y:None
                            height:"70dp"
                            MDTextField:
                                id:confirm_new_password_text_field
                                mode:"fill"
                                icon_right:"key-variant"
                                icon_left_color_normal:[0, 0, 0, 1]
                                hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
                                radius:[20, 20, 20, 20]
                                hint_text:"--Confirm Password--"
                                password:True
                                pos_hint:{"center_x":.5, "center_y":.5}
                        ChangePasswordButton:
                            screen_manager:password_recovery_body_screen_manager
                            md_bg_color:[0, 154/float(255), 255/float(255), 1]
                            size_hint_y:None
                            height:"40dp"
                            radius:[30, 30, 30, 30]
                            root:forgot_password_screen
                            MDLabel:
                                text:"Submit"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                                pos_hint:{"center_x":.5}
                        BoxLayout:
                ErrorScreen:
                    id:error_object
                LoadingScreen
""")
class ForgotPasswordScreen(MDScreen):
    def goBackToLogin(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "gateway_screen"
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
class ForgotPasswordEmailButton(TouchBox):
    def goToLoadingScreen(self):
        self.screen_manager.transition = SlideTransition(direction = "left")
        self.screen_manager.current = "loading_screen"
    def respondToTouch(self):
        email = self.root.ids.user_email_text_field.text
        print(email)
        if not checkEmailQualification(email):
            self.callDialog("Fill correct email!")
        else:
            self.goToLoadingScreen()
            thread.start_new_thread(request, (self.screen_manager, self.root.ids.error_object, "email_screen",
                             "recreate_password_screen", self.screen_manager, "http://localhost:8080/gateway/logon/", ))
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Password Recovery Error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
class ChangePasswordButton(TouchBox):
    def respondToTouch(self):
        code = self.root.ids.confirmation_code_text_field.text
        n_password = self.root.ids.new_password_text_field.text
        con_password = self.root.ids.confirm_new_password_text_field.text
        print(code, n_password, con_password)
    def callDialog(self, text):
        button = MDFillRoundFlatButton(text = "Ok")
        self.dialog = MDDialog(title = "Password Recreate Error", text = text, buttons = [button])
        button.bind(on_press = self.close)
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()