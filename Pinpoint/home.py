from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivy.lang import Builder
from pin_point import MapScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy_garden.mapview import MapView
from touch import TouchBox
import time
from kivy.clock import Clock
ui = Builder.load_string("""
<LoadUpdateLocation>:
    size_hint:None, None
    size:"40dp", "40dp"
    radius:[40, 40, 40, 40]
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
<LocationShareButton>:
    size_hint_y:None
    height:"40dp"
    radius:[30, 30, 30, 30]
    md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
    MDIconButton:
        size_hint:None, None
        size:"40dp", "40dp"
        user_font_size:"30dp"
        theme_text_color:"Custom"
        text_color:[1, 1, 1, 1]
        icon:"map-marker-up"
        pos_hint:{"center_y":.5}
    MDLabel:
        id:location_share_label
        text:"Share your location"
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:[1, 1, 1, 1]
    MDBoxLayout:
        size_hint:None, None
        size:"40dp", "40dp"
<HomeScreen>:
    id:home_screen
    name:"home_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        MDBoxLayout:
            orientation:"vertical"
            size_hint_y:None
            height:"130dp"
            radius:[0, 0, 40, 40]
            md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                MDLabel:
                    text:"Pinpoint"
                    font_size:"40dp"
                    font_name:"HoneybeePersonalUseRegular-YzBn4"
                    halign:"center"
                    valign:"middle"
                    color:[0, 0, 0, 1]
            MDBoxLayout:
                size_hint_y:None
                height:"80dp"
                padding:"0dp", "10dp"
                Widget:
                FitImage:
                    id:my_avater
                    source:"male_avater_1.jpeg"
                    size_hint:None, None
                    size:"70dp", "70dp"
                    radius:[60, 60, 60, 60]
                    pos_hint:{"center_x":.5, "center_y":.5}
                Widget:
        MDBoxLayout:
            orientation:"vertical"
            MDBoxLayout:
                padding:5, 10, 5, 0
                MDBoxLayout:
                    FloatLayout:
                        size_hint:None, None
                        size:self.parent.size
                        pos:self.parent.pos
                        MDBoxLayout:
                            pos:self.parent.pos
                            ScreenManager:
                                root:home_screen
                                MapScreen:
                                    id:map_screen
                        MDBoxLayout:
                            pos:self.parent.pos
                            ScreenManager:
                                Screen:
                                    name:"empty_screen"
                                    
                                Screen:
                                    name:"settings_screen"
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:5
                LocationShareButton:
                    root:home_screen
                    id:location_share_button
                MDIconButton:
                    id:settings_button
                    size_hint:None, None
                    size:"40dp", "40dp"
                    icon:"cog"
                    theme_text_color:"Custom"
                    user_font_size:"30dp"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    on_release:root.goToSettingsScreen(self)
""")
class SettingsBox(MDBoxLayout):
    pass
class LoadUpdateLocation(MDBoxLayout):
    pass
class LocationShareButton(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.press = False
        self.response = -1
        self.location = [-26.3714, 28.3754]
    def openDialog(self, title, message, button):
        self.dialog = MDDialog(title = title, text = message, buttons = [button])
        self.dialog.open()
    def close(self, button):
        self.dialog.dismiss()
    def makeRequest(self, seconds):
        try:
            response = requests.get("http://localhost:8080/userPin/storeLocation/", params = self.params)
            if eval(response[0])  == 0:
                self.response = 1
            else:
                self.response = 0
        except:
            self.response = -2
    def resetLocationShareButton(self):
        last_object = self.children[0]
        self.remove_widget(last_object)
        self.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
        self.ids.location_share_label.text = "Share your location"
        self.press = True
    def getResponse(self, seconds):
        button = MDFillRoundFlatButton(text = "Ok")
        button.bind(on_press = self.close)
        if self.response == 1:
            self.resetLocationShareButton()
            self.openDialog("Request Success", "Location shared", button)
        elif self.response == 0:
            self.resetLocationShareButton()
            self.openDialog("Request Failure", "Location could'nt be shared", button)
        elif self.response == -2:
            self.resetLocationShareButton()
            self.openDialog("Request Failure", "Network error", button)
        else:
            Clock.schedule_once(self.getResponse, 0)
    def respondToTouch(self):
        if self.press:
            self.press = False
            self.location = self.root.ids.map_screen.location
            self.params = {"location":str(self.location), "user_id":self.root.id}
            self.add_widget(LoadUpdateLocation())
            self.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
            self.ids.location_share_label.text = "Loading..."
            Clock.schedule_once(self.makeRequest, 0)
            Clock.schedule_once(self.getResponse, 3)
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = ""
        self.location = []
    def goToUsersScreen(self):
        pass
    def goToSettingsScreen(self, button):
        button.text_color = [0, 154/float(255), 255/float(255), 1]
        self.ids.map_screen.goToSettings()