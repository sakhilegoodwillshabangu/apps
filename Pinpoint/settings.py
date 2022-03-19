from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivy.lang import Builder
ui = Builder.load_string("""
<SelectionOptionBar>:
    size_hint_x:None
    width:"250dp"
    radius:[40, 40, 40, 40]
    md_bg_color:[0, 154/float(255), 255/float(255), 1]
    MDIconButton:
        id:icon_object
        size_hint:None, None
        size:"40dp", "40dp"
        icon:"check"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
        md_bg_color:[0, 154/float(255), 255/float(255), 1]
        pos_hint:{"center_y":.5}
    MDLabel:
        id:label_object
        text:"Share with friends"
        bold:True
        text_hint:self.size
        halign:"center"
        valign:"middle"
        color:[1, 1, 1, 1]
    MDIconButton:
        id:icon_object
        size_hint:None, None
        size:"40dp", "40dp"
        icon:"account-multiple"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
        md_bg_color:[0, 154/float(255), 255/float(255), 1]
        pos_hint:{"center_y":.5}
<SettingsScreen>:
    name:"settings_name"
    MDBoxLayout:
        orientation:"vertical"
        padding:"5dp", "5dp", "5dp", "30dp"
        spacing:10
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                icon:"arrow-left-thick"
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                pos_hint:{"center_y":.5}
                on_release:root.exitSettings()
        MDBoxLayout:
        MDBoxLayout:
            id:friends_share_box
            size_hint_y:None
            height:"50dp"
            Widget:
            SelectionOptionBar:
        MDBoxLayout:
            id:public_share_box
            size_hint_y:None
            height:"50dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"account-group"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                pos_hint:{"center_y":.5}
                on_release:root.selectPublicShare(self)
        MDBoxLayout:
            id:no_one_share_box
            size_hint_y:None
            height:"50dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"account-multiple-remove"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
                pos_hint:{"center_y":.5}
                on_release:root.selectShareWithNoOne(self)
""")
class SelectionOptionBar(MDBoxLayout):
    pass
class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_selected_object = None
        self.icon = "account-multiple"
        self.share_rule = "public"
        self.id = ""
        self.function_object = self.selectFriendsShare
    def shiftBar(self):
        if self.share_rule == "friends":
            self.selectFriendsShare(1)
        elif self.share_rule == "public":
            self.selectPublicShare(1)
        else:
            self.selectShareWithNoOne(1)
    def removeBar(self):
        last_object = self.current_selected_object.children[0]
        self.current_selected_object.remove_widget(last_object)
    def addButton(self):
        button = MDIconButton(size_hint = (None, None), size = ("40dp", "40dp"), 
                                                   icon = self.icon, pos_hint = {"center_y":.5}, theme_text_color = "Custom", 
                                                   text_color = [1, 1, 1, 1], md_bg_color = [0, 154/float(255), 255/float(255), 1])
        button.bind(on_release = self.function_object)
        button.icon = self.icon
        self.current_selected_object.add_widget(button)
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/userPin/updateShareRule/", params = {"user_id":self.id, "share_rule":self.share_rule}).text)
            if response[0]  == 1:
                self.response = 1
                self.friends = response[1]
            else:
                self.response = 0
        except:
            self.response = -2
    def selectFriendsShare(self, button):
        self.removeBar()
        self.addButton()
        self.current_selected_object = self.ids.friends_share_box
        bar = SelectionOptionBar()
        self.icon = "account-multiple"
        self.function_object = self.selectFriendsShare
        button = self.ids.friends_share_box.children[0]
        self.ids.friends_share_box.remove_widget(button)
        self.ids.friends_share_box.add_widget(bar)
        if not self.share_rule == "friends":
            self.share_rule = "friends"
            Clock.schedule_once(self.makeRequest, 0)
    def selectPublicShare(self, button):
        self.removeBar()
        self.addButton()
        self.current_selected_object = self.ids.public_share_box
        bar = SelectionOptionBar()
        self.icon = "account-group"
        self.function_object = self.selectPublicShare
        bar.ids.icon_object.icon = "account-group"
        bar.ids.label_object.text = "Share with public"
        button = self.ids.public_share_box.children[0]
        self.ids.public_share_box.remove_widget(button)
        self.ids.public_share_box.add_widget(bar)
        if not self.share_rule == "public":
            self.share_rule = "public"
            Clock.schedule_once(self.makeRequest, 0)
    def selectShareWithNoOne(self, button):
        self.removeBar()
        self.addButton()
        self.current_selected_object = self.ids.no_one_share_box
        bar = SelectionOptionBar()
        self.icon = "account-multiple-remove"
        self.function_object = self.selectShareWithNoOne
        bar.ids.icon_object.icon = "account-multiple-remove"
        bar.ids.label_object.text = "Share with no one"
        button = self.ids.no_one_share_box.children[0]
        self.ids.no_one_share_box.remove_widget(button)
        self.ids.no_one_share_box.add_widget(bar)
        if not self.share_rule == "no_one":
            self.share_rule = "no_one"
            Clock.schedule_once(self.makeRequest, 0)
    def exitSettings(self):
        screen_manager = self.parent
        screen_manager.transition = SlideTransition(direction = "right")
        screen_manager.current = "set_location_screen"
        screen_manager.root.parent.root.ids.settings_button.text_color = [0, 0, 0, 1]
class Test(MDApp):
    def build(self):
        root = SettingsScreen()
        root.current_selected_object = root.ids.friends_share_box
        root.shiftBar()
        return root
if __name__ == "__main__":
    Test().run()