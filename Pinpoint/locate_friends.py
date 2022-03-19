from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import SlideTransition
from mani_image import resizeImage
import time
import _thread as thread
from touch import TouchBox
from kivy.clock import Clock
from kivy.lang import Builder
from new_friend import AddNewFriendScreen
from friends_list import FriendsListBox
ui = Builder.load_string("""
<ResponseBox>:
    id:response_box
    padding:"5dp", "0dp"
    MDLabel:
        id:error_label
        text:""
        font_size:"20dp"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:[1, 0, 0, 1]
    MDBoxLayout:
        size_hint_x:None
        width:"160dp"
        orientation:"vertical"
        Widget:
        ReloadButton:
            root:response_box
            size_hint_y:None
            height:"40dp"
            md_bg_color:[0, 154/float(255), 255/float(255), 1]
            radius:[30, 30, 30, 30]
            pos_hint:{"center_y":.5}
            MDIconButton:
                id:icon_button
                size_hint:None, None
                size:"40dp", "40dp"
                user_font_size:"30dp"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                icon:"plus"
                pos_hint:{"center_y":.5}
            MDLabel:
                id:button_label
                text:""
                text_size:self.size
                halign:"left"
                valign:"middle"
                color:[1, 1, 1, 1]
        Widget:
<LoadFriends>:
    size_hint:None, None
    size:"60dp", "60dp"
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
<LoadSpace>:
    padding:5
    MDBoxLayout:
        Widget:
        LoadFriends:
            pos_hint:{"center_y":.5}
        Widget:
<LocateFriendsScreen>:
    id:locate_friends_screen
    name:"locate_friends_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
        MDBoxLayout:
            id:header_box
            root:locate_friends_screen
            size_hint_y:None
            height:"155dp"
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"60dp"
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    user_font_size:"30dp"
                    icon:"arrow-left-thick"
                    theme_text_color:"Custom"
                    text_color:[0, 0, 0, 1]
                    pos_hint:{"center_y":.5}
                    on_release:root.goBackToHome()
                MDLabel:
                    text:"Locate friends"
                    font_size:"40dp"
                    font_name:"HoneybeePersonalUseRegular-YzBn4"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[0, 0, 0, 1]
                MDBoxLayout:
                    size_hint_x:None
                    width:"40dp"
            LoadSpace:
        MDBoxLayout:
            radius:[30, 30, 0, 0]
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            MyMap:
                id:map
                zoom:1
""")
class LoadSpace(MDBoxLayout):
    pass
class ResponseBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_code = -1
class ReloadButton(TouchBox):
    def respondToTouch(self):
        if self.root.error_code == 1:
            print("Go to add friends")
            print(self.root.parent.root.parent)
            if not self.root.parent.root.parent.has_screen("new_user_screen"):
                add_new_friend = AddNewFriendScreen()
                self.root.parent.root.parent.add_widget(add_new_friend)
            self.root.parent.root.parent.transition = SlideTransition(direction = "left")
            self.root.parent.root.parent.current = "new_user_screen"
        elif self.root.error_code == 2:
            Clock.schedule_once(self.root.parent.root.load, 0)
            self.root.parent.root.getFriends()
class MyMap(MapView):
    pass
class LoadFriends(MDBoxLayout):
    pass
class ResponseBox(MDBoxLayout):
    pass
class LocateFriendsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loader = LoadSpace()
        self.id = ""
        self.nofriends_error_box = ResponseBox()
        self.nofriends_error_box.error_code = 1
        self.connection_error_box = ResponseBox()
        self.connection_error_box.error_code = 2
        self.response = -1
    def goBackToHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
    def locateThisUser(self, image, coord):
        self.ids.map.lat = coord[0]
        self.ids.map.lon = coord[1]
        self.marker = MapMarkerPopup(source = "50_friend.png", lat = coord[0], lon = coord[1])
        self.ids.map.add_marker(self.marker)
        self.ids.map.zoom = 10
    def unLocateThisUser(self, coord):
        self.ids.map.zoom = 1
    def load(self, seconds):
        self.response = -1
        last_object = self.ids.header_box.children[0]
        self.ids.header_box.remove_widget(last_object)
        self.ids.header_box.add_widget(self.loader)
    def loadFriends(self, seconds):
        friends_list_box = FriendsListBox()
        try:
            friends_list_box.friends = self.friends
        except:
            pass
        print("Children:", self.ids.header_box)
        last_object = self.ids.header_box.children[0]
        print("------:", last_object)
        self.ids.header_box.remove_widget(last_object)
        self.ids.header_box.add_widget(friends_list_box)
    def makeRequest(self, seconds):
        try:
            response = eval(requests.get("http://localhost:8080/userPin/loadFriends/", params = {"user_id":self.id}).text)
            if response[0]  == 1:
                self.response = 1
                self.friends = response[1]
            else:
                self.response = 0
        except:
            self.response = -2
    def findNextBox(self, seconds):
        if self.response == 1:
            Clock.schedule_once(self.loadFriends, 0)
        elif self.response == 0:
            self.ids.header_box.remove_widget(self.ids.header_box.children[0])
            self.nofriends_error_box.ids.error_label.text = "No friends"
            self.nofriends_error_box.ids.icon_button.icon = "plus"
            self.nofriends_error_box.ids.button_label.text = "Add friends"
            self.ids.header_box.add_widget(self.nofriends_error_box)
        elif self.response == -2:
            print("####", self.ids.header_box)
            self.ids.header_box.remove_widget(self.ids.header_box.children[0])
            self.connection_error_box.ids.error_label.text = "Connection Error"
            self.connection_error_box.ids.icon_button.icon = "reload"
            self.connection_error_box.ids.button_label.text = "Try again"
            self.ids.header_box.add_widget(self.connection_error_box)
        else:
            Clock.schedule_once(self.findNextBox, 0)
    def getFriends(self):
        Clock.schedule_once(self.makeRequest, 0)
        Clock.schedule_once(self.findNextBox, 3)
class TestApp(MDApp):
    def build(self):
        root = LocateFriendsScreen()
        print("####", root.ids.header_box)
        return root
if __name__ == "__main__":
    TestApp().run()