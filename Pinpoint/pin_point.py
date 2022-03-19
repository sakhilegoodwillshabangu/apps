from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.screenmanager import SlideTransition, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from friends_list import FriendsListBox
from locate_friends import LocateFriendsScreen
from kivy.clock import Clock
import _thread as thread
import time
from touch import TouchBox
from kivy.lang import Builder
from new_friend import AddNewFriendScreen
from settings import SettingsScreen
ui = Builder.load_string("""
<MapScreen>:
    id:map_screen
    name:"pin_point_screen"
    MDBoxLayout:
        id:main_box
        orientation:"vertical"
        FloatLayout:
            size_hint:None, None
            size:main_box.size
            pos:main_box.pos
            id:float_layout
            MDBoxLayout:
                pos:float_layout.pos
                MyMap:
                    id:map
                    lat:-26.3714
                    lon:28.3754
                    zoom:10
                    on_zoom:
                        self.zoom = 10 if self.zoom < 10 else self.zoom
                    on_lat:
                    on_lan:
            MDBoxLayout:
                pos:float_layout.pos
                orientation:"vertical"
                ScreenManager:
                    root:map_screen
                    id:map_sub_screen_manager
                    MDScreen:
                        name:"set_location_screen"
                        MDBoxLayout:
                            orientation:"vertical"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"60dp"
                                padding:"10dp", "10dp"
                                MDIconButton:
                                    size_hint:None, None
                                    size:"40dp", "40dp"
                                    theme_text_color:"Custom"
                                    text_color:[1, 1, 1, 1]
                                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                    icon:"plus"
                                    pos_hint:{"center_y":.5}
                                    on_release:root.goToAddFriend()
                                Widget:
                                ViewFriendsButtonBox:
                                    screen_manager:map_sub_screen_manager
                                    root:map_screen
                                    padding:"10dp", "0dp"
                                    size_hint:None, None
                                    size:"150dp", "40dp"
                                    radius:[30, 30, 30, 30]
                                    md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
                                    MDIcon:
                                        size_hint:None, None
                                        size:"40dp", "40dp"
                                        user_font_size:"30dp"
                                        icon:"account"
                                        theme_text_color:"Custom"
                                        text_color:[1, 1, 1, 1]
                                        pos_hint:{"center_y":.5, "center_x":.5}
                                    MDLabel:
                                        text:"View friends"
                                        text_size:self.size
                                        halign:"left"
                                        valign:"middle"
                                        color:[1, 1, 1, 1]
                            Widget:
                            MDBoxLayout:
                                size_hint_y:None
                                height:"110dp"
                                spacing:5
                                padding:"10dp", "30dp"
                                Widget:
                                MDIconButton:
                                    root:map_screen
                                    id:put_marker_button
                                    size_hint:None, None
                                    size:"40dp", "40dp"
                                    user_font_size:"20dp"
                                    icon:"crosshairs"
                                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                                    theme_text_color:"Custom"
                                    text_color:[255/float(255), 255/float(255), 255/float(255), 1]
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    on_release:root.addMarker()
                                MDIconButton:
                                    id:remove_marker_button
                                    size_hint:None, None
                                    size:"40dp", "40dp"
                                    user_font_size:"20dp"
                                    icon:"crosshairs-off"
                                    md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
                                    theme_text_color:"Custom"
                                    text_color:[255/float(255), 255/float(255), 255/float(255), 1]
                                    pos_hint:{"center_x":.5, "center_y":.5}
                                    on_release:root.removeMarker()
""")
class ViewFriendsButtonBox(TouchBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loading = True
        self.locate_friends_screen = LocateFriendsScreen()
    def respondToTouch(self):
        self.locate_friends_screen.id = self.root.id
        if not self.root.parent.root.parent.has_screen("locate_friends_screen"):
            self.root.parent.root.parent.add_widget(self.locate_friends_screen)
        self.root.parent.root.parent.transition = SlideTransition(direction = "left")
        self.root.parent.root.parent.current = "locate_friends_screen"
        if self.loading:
            self.loading = False
            self.locate_friends_screen.getFriends()
        else:
            Clock.schedule_once(self.locate_friends_screen.load, 0)
            self.locate_friends_screen.getFriends()
class MyMap(MapView):
    pass
class MapScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.pin_pointed = False
        self.location = []
        self.id = ""
        self.add_new_friend_screen = AddNewFriendScreen()
        self.add_new_friend_screen.id = self.id
    def goToAddFriend(self):
        if not self.parent.root.parent.has_screen("new_user_screen"):
            self.parent.root.parent.add_widget(self.add_new_friend_screen)
        self.parent.root.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.current = "new_user_screen"
    def goBackToLocationSettingScreen(self):
        self.ids.map_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.map_sub_screen_manager.current = "set_location_screen"
    def addMarker(self):
        if not self.pin_pointed:
            self.pin_pointed = True
            self.ids.put_marker_button.md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
            self.ids.remove_marker_button.md_bg_color = [0, 154/float(255), 255/float(255), 1]
            self.marker = MapMarkerPopup(source = "50_user_location.png", lat = self.ids.map.lat, lon = self.ids.map.lon)
            self.location = [self.ids.map.lat, self.ids.map.lon]
            self.ids.map.add_marker(self.marker)
            self.ids.put_marker_button.root.parent.root.ids.location_share_button.md_bg_color = [0, 154/float(255), 255/float(255), 1]
            self.ids.put_marker_button.root.parent.root.ids.location_share_button.press = True
    def removeMarker(self):
        if self.pin_pointed:
            self.pin_pointed = False
            self.ids.put_marker_button.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
            self.ids.remove_marker_button.md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
            self.ids.map.remove_widget(self.marker)
            self.ids.put_marker_button.root.parent.root.ids.location_share_button.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
            if not self.ids.put_marker_button.root.parent.root.ids.location_share_button.ids.location_share_label.text == "Share your location":
                last_object = self.ids.put_marker_button.root.parent.root.ids.location_share_button.children[0]
                self.ids.put_marker_button.root.parent.root.ids.location_share_button.ids.location_share_label.text = "Share your location"
                self.ids.put_marker_button.root.parent.root.ids.location_share_button.remove_widget(last_object)
            self.ids.put_marker_button.root.parent.root.ids.location_share_button.press = False
            try:
                Clock.unschedule(self.ids.put_marker_button.root.parent.root.ids.location_share_button.makeRequest)
                Clock.unschedule(self.ids.put_marker_button.root.parent.root.ids.location_share_button.getResponse)
            except:
                pass
    def goToSettings(self):
        if not self.ids.map_sub_screen_manager.has_screen("settings_name"):
            settings_screen = SettingsScreen()
            settings_screen.id = self.parent.root.id
            settings_screen.share_rule = self.parent.root.parent.ids.gateway_screen.share_rule
            settings_screen.current_selected_object = settings_screen.ids.friends_share_box
            settings_screen.shiftBar()
            self.ids.map_sub_screen_manager.add_widget(settings_screen)
        self.ids.map_sub_screen_manager.transition = SlideTransition(direction = "left")
        self.ids.map_sub_screen_manager.current = "settings_name"