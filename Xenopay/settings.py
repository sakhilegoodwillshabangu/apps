from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
ui = Builder.load_string("""
<ChangeEmailBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"email"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"Change Email"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<ChangePasswordBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"key-variant"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"Change Password"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<AboutBarBox>:
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    radius:[20, 20, 20, 20]
    orientation:"vertical"
    MDBoxLayout:
        BoxLayout:
        MDIconButton:
            size_hint:None, None
            size:"50dp", "50dp"
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            user_font_size:"40dp"
            icon:"information"
            pos_hint:{"center_x":.5, "center_y":.5}
        BoxLayout:
    MDBoxLayout:
        MDLabel:
            text:"About"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
<ReactionBarBox>:
    orientation:"vertical"
    MDBoxLayout:
        MDLabel:
            text:"How was your user experiance"
            text_size:self.size
            halign:"center"
            valign:"middle"
    MDBoxLayout:
        spacing:5
        BoxLayout:
        MDIconButton:
            id:heart_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"heart-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithHeart()
        MDIconButton:
            id:thumb_up_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"thumb-up-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithThumbUp()
        MDIconButton:
            id:happy_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-happy-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithHappyFace()
        MDIconButton:
            id:cool_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-cool-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithCoolFace()
        MDIconButton:
            id:frown_button_object
            size_hint:None, None
            size:"50dp", "50dp"
            user_font_size:"40dp"
            icon:"emoticon-frown-outline"
            pos_hint:{"center_x":.5, "center_y":.5}
            on_release:root.reactWithFrownFace()
        BoxLayout:
<SettingsScreen>:
    id:settings_screen_object
    name:"settings_screen"
    md_bg_color:[0, 0, 0, 1]
    MDBoxLayout:
        orientation:"vertical"
        padding:"10dp", "5dp"
        spacing:10
        md_bg_color:[0, 0, 0, 1]
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            size_hint_y:None
            height:"130dp"
            orientation:"vertical"
            radius:[20, 20, 20, 20]
            MDBoxLayout:
                MDIconButton:
                    size_hint:None, None
                    size:"50dp", "50dp"
                    user_font_size:"30dp"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    icon:"arrow-left-thick"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    on_release:root.goBackToHome()
                MDLabel:
                    text:"Settings"
                    font_size:"25dp"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDBoxLayout:
                    size_hint:None, None
                    size:"50dp", "50dp"
            MDBoxLayout:
                size_hint_y:None
                height:"80dp"
                padding:"5dp", "0dp"
                MDTextField:
                    hint_text:"---Feedback---"
                    icon_right:"send"
                    mode:"fill"
                    radius:[20, 20, 20, 20]
                    pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            ScreenManager:
                id:settings_body_screen_manager
                Screen:
                    name:"menu_screen"
                    MDBoxLayout:
                        screen_manager:settings_body_screen_manager
                        spacing:10
                        padding:"5dp", "10dp", "5dp", "10dp"
                        orientation:"vertical"
                        ChangeEmailBarBox:
                        ChangePasswordBarBox:
                        AboutBarBox:                       
                Screen:
                    name:"change_email_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                user_font_size:"30dp"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                icon:"menu"
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"Change Email"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            root:settings_screen_object
                            padding:"10dp", "0dp"
                            spacing:5
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:new_email_object
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--New Email"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:confirm_email_object
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Confirm Email"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            ChangeEmailContinueButton:
                                size_hint_y:None
                                height:"50dp"
                                radius:[30, 30, 30, 30]
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                BoxLayout:
                                    size_hint:None, None
                                    size:"50dp", "50dp"
                                MDLabel:
                                    text:"Continue"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                                MDIconButton:
                                    size_hint:None, None
                                    size:"50dp", "50dp"
                                    user_font_size:"30dp"
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    icon:"arrow-right-thick"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            Widget:
                Screen:
                    name:"change_password_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                user_font_size:"30dp"
                                icon:"menu"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"Change Password"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            root:settings_screen_object
                            padding:"10dp", "0dp"
                            spacing:5
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:old_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Old Password"
                                    password:True
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:new_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    password:True
                                    hint_text:"--New Password"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                MDTextField:
                                    id:confirm_password
                                    mode:"fill"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    radius:[20, 20, 20, 20]
                                    hint_text:"--Verify Password"
                                    password:True
                            ChangePasswordContinueButton:
                                size_hint_y:None
                                height:"50dp"
                                radius:[30, 30, 30, 30]
                                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                BoxLayout:
                                    size_hint:None, None
                                    size:"50dp", "50dp"
                                MDLabel:
                                    text:"Continue"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                                MDIconButton:
                                    size_hint:None, None
                                    size:"50dp", "50dp"
                                    user_font_size:"30dp"
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    icon:"arrow-right-thick"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                            Widget:
                Screen:
                    name:"about_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"60dp"
                            padding:5
                            MDIconButton:
                                size_hint:None, None
                                size:"40dp", "40dp"
                                icon:"menu"
                                theme_text_color:"Custom"
                                text_color:[1, 1, 1, 1]
                                user_font_size:"30dp"
                                on_release:root.goBackToSettingsMenu()
                            MDLabel:
                                text:"About"
                                text_size:self.size
                                halign:"center"
                                valign:"middle"
                                color:[1, 1, 1, 1]
                            Widget:
                                size_hint_x:None
                                width:"40dp"
                        MDBoxLayout:
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"70dp"
                                Widget:
                                MDIconButton:
                                    size_hint:None, None
                                    size:"70dp", "70dp"
                                    icon:"information"
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    user_font_size:"60dp"
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                Widget:
                            MDBoxLayout:
                                size_hint_y:None
                                height:about_label.height
                                Label:
                                    text:"Xenopay version 1.0.0 for android is a payment application that works with different retailers to facilitate payments and money deposits"
                                    id:about_label
                                    text_size:self.width, None
                                    size_hint:1, None
                                    halign:"center"
                                    valign:"middle"
                                    height:self.texture_size[1]
                                    color:[1, 1, 1, 1]
                            MDBoxLayout:
                            MDBoxLayout:
                                size_hint_y:None
                                height:"30dp"
                                MDLabel:
                                    color:[120/float(255), 120/float(255), 120/float(255), 1]
                                    text:"Copyright@2022 Xenopay all right reserved"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
""")
class SettingsScreen(MDScreen):
    def goBackToSettingsMenu(self):
        self.ids.settings_body_screen_manager.transition = SlideTransition(direction ="right")
        self.ids.settings_body_screen_manager.current = "menu_screen"
    def goBackToHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
    def respondToTouch(self):
	    pass
class ChangePasswordContinueButton(TouchBox):
    def respondToTouch(self):
	    old_password = self.parent.root.ids.old_password.text
	    new_password = self.parent.root.ids.new_password.text
	    confirm_password = self.parent.root.ids.confirm_password.text
	    print(old_password, new_password, confirm_password)
class ChangeEmailContinueButton(TouchBox):
    def respondToTouch(self):
        new_email = self.parent.root.ids.new_email_object.text
        confirm_email = self.parent.root.ids.confirm_email_object.text
        print(new_email, confirm_email)
class ChangeEmailBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "change_email_screen"
class ChangePasswordBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "change_password_screen"
class AboutBarBox(TouchBox):
    def respondToTouch(self):
        self.parent.screen_manager.transition = SlideTransition(direction = "left")
        self.parent.screen_manager.current = "about_screen"
class ReactionBarBox(MDBoxLayout):
    def respondToTouch(self):
        pass
    def reactWithHeart(self):
        self.ids.heart_button_object.icon = "heart"
    def reactWithThumbUp(self):
        self.ids.thumb_up_button_object.icon = "thumb-up"
    def reactWithHappyFace(self):
        self.ids.happy_button_object.icon = "emoticon-happy"
    def reactWithCoolFace(self):
        self.ids.cool_button_object.icon = "emoticon-cool"
    def reactWithFrownFace(self):
        self.ids.frown_button_object.icon = "emoticon-frown"
class Tester(MDApp):
    def build(self):
        root = SettingsScreen()
        return root
if __name__ == "__main__":
    Tester().run()