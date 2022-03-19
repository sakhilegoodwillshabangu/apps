from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
ui = Builder.load_string("""
<PlaceSearchScreen>:
    name:"places_search_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            padding:"10dp", "0dp"
            MDTextField:
                id:location_text_field
                icon_right:"cog"
                mode:"fill"
                icon_left_color_normal:[0, 0, 0, 1]
                hint_text_color_normal:[0/float(255), 154/float(255), 255/float(255), 1]
                radius:[20, 20, 20, 20]
                line_color_normal:[0, 154/float(255), 255/float(255), 1]
                hint_text:"State, City, Town"
                pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            padding:"10dp", "0dp"
            size_hint_y:None
            height:"40dp"
            MDBoxLayout:
                size_hint_y:None
                height:"40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[0, 154/float(255), 255/float(255), 1]
        MDBoxLayout:
<LookUpScreen>:
    name:"look_up_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            ScreenManager:
                PlaceSearchScreen:
                PlacesToStayScreen:
""")
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        x_size = self.pos[0] + self.size[0]
        y_size = self.pos[1] + self.size[1]
        if ((touch.x > self.pos[0] and touch.x < x_size) and (touch.y > self.pos[1] and touch.y < y_size)):
            self.respondToTouch()
    def respondToTouch(self):
        pass
class PlaceSearchScreen(MDScreen):
    pass
class PlacesToStayScreen(MDScreen):
    pass
class PlacesToEatButtonBox(TouchBox):
    def respondToTouch(self):
        self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
        self.parent.children[0].md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
class PlacesToStayButtonBox(TouchBox):
    def respondToTouch(self):
        self.md_bg_color = [0, 154/float(255), 255/float(255), 1]
        self.parent.children[-1].md_bg_color = [190/float(255), 190/float(255), 190/float(255), 1]
class LookUpScreen(MDScreen):
    pass