from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from touch import TouchBox
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivy.uix.screenmanager import SlideTransition
import _thread as thread 
import time
from kivy.clock import Clock
ui = Builder.load_string("""
<LoadAddFriend>:
    size_hint:None, None
    size:"50dp", "50dp"
    radius:[50, 50, 50, 50]
    Image:
        id:gif
        source:"load.gif"
        center:self.parent.center
        size:50, 50
        allow_stretch:True
        anim_delay:-1
        anim_loop:10000000000000000000000000
        #_coreimage:anim_reset(True)
        anim_delay:0.01
<Icon>:
    icon:"arrow-right-thick"
    size_hint:None, None
    size:"40dp", "40dp"
    theme_text_color:"Custom"
    text_color:[1, 1, 1, 1]
    pos_hint:{"center_y":.5}
<AddNewFriendScreen>:
    id:add_new_friend_screen
    name:"new_user_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            radius:[0, 0, 30, 30]
            md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                theme_text_color:"Custom"
                text_color:[0, 0, 0, 1]
                pos_hint:{"center_y":.5}
                on_release:root.goBack()
            MDLabel:
                text:"Add a friend"
                font_size:"40dp"
                font_name:"HoneybeePersonalUseRegular-YzBn4"
                text_size:self.size
                halign:"center"
                valign:"middle"
            MDBoxLayout:
                size_hint_x:None
                width:"40dp"
        MDBoxLayout:
            orientation:"vertical"
            padding:"5dp", "5dp"
            spacing:10
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            Widget:
            MDBoxLayout:
                size_hint_y:None
                height:"70dp"
                padding:"5dp", "0dp"
                MDTextField:
                    id:user_name
                    hint_text:"--@Username"
                    mode:"fill"
                    radius:[20, 20, 20, 20]
            AddUserButton:
                id:add_user_button_box
                root:add_new_friend_screen
                size_hint_y:None
                height:"50dp"
                radius:[40, 40, 40, 40]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                MDBoxLayout:
                    size_hint_x:None
                    width:"40dp"
                MDLabel:
                    id:button_box_label
                    text:"Continue"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    icon:"arrow-right-thick"
                    theme_text_color:"Custom"
                    text_color:[1, 1, 1, 1]
                    pos_hint:{"center_y":.5}
            MDBoxLayout:
""")
class Icon(MDIconButton):
    pass
class LoadAddFriend(MDBoxLayout):
    pass
class AddUserButton(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.press = True
    def respondToTouch(self):
        self.getUserName()
    def getUserName(self):
        user_name = self.root.ids.user_name.text
        if user_name and self.press:
            self.press = False
            print("User Name:", user_name)
            self.params = {"user_name":user_name, "user_id":self.root.id}
            last_box = self.root.ids.add_user_button_box.children[0]
            self.root.ids.button_box_label.text = "loading........"
            self.root.ids.add_user_button_box.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
            self.remove_widget(last_box)
            self.add_widget(LoadAddFriend())
            Clock.schedule_once(self.root.makeRequest, 0)
            Clock.schedule_once(self.root.findNextBox, 3)
class AddNewFriendScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = -1
        self.id = ""
    def goBack(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/userPin/storeFriend/", params = self.params).text)
            if response[0]  == 1:
                self.response = 1
            else:
                self.response = 0
        except:
            self.response = -2
    def openDialog(self, title, message, button):
        self.dialog = MDDialog(title = title, text = message, buttons = [button])
        self.dialog.open()
    def resetContiuneButton(self):
        self.response = -1
        self.ids.add_user_button_box.press = True
        self.ids.add_user_button_box.md_bg_color = [0, 154/float(255), 255/float(255), 1]
        self.ids.button_box_label.text = "Continue"
        last_object = self.ids.add_user_button_box.children[0]
        self.ids.add_user_button_box.remove_widget(last_object)
        icon_button = Icon()
        self.ids.add_user_button_box.add_widget(icon_button)
    def findNextBox(self, seconds):
        button = MDFillRoundFlatButton(text = "Ok")
        button.bind(on_press = self.close)
        if self.response == 1:
            self.resetContiuneButton()
            self.openDialog("Request Success", "Friend added", button)
        elif self.response == 0:
            self.resetContiuneButton()
            self.openDialog("Request Failure", "Friend could'nt be added", button)
        elif self.response == -2:
            self.resetContiuneButton()
            self.openDialog("Request Failure", "Network error", button)
        else:
            Clock.schedule_once(self.findNextBox, 0)
    def close(self, button):
        self.dialog.dismiss()