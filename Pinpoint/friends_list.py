from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from touch import TouchBox
from kivy.lang import Builder
ui = Builder.load_string("""
<UserBox>:
    id:user_box
    size_hint:None, None
    size:"110dp", "85dp"
    spacing:5
    orientation:"vertical"
    MDBoxLayout:
        root:user_box
        Widget:
        UserProfilePicture:
            id:profile_image_object
        Widget:
    MDBoxLayout:
        size_hint_y:None
        height:"20dp"
        radius:[20, 20, 20, 20]
        MDLabel:
            id:user_name
            bold:True
            text:"@Username"
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[0, 0, 0, 1]
<UserProfilePicture>:
    size_hint:None, None
    size:"60dp", "60dp"
    padding:"0dp", "1.5dp"
    radius:[50, 50, 50, 50]
    md_bg_color:[0/float(255), 255/float(255), 154/float(255), 1]
    Widget:
    MDBoxLayout:
        size_hint:None, None
        size:"57dp", "57dp"
        radius:[47, 47, 47, 47]
        md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
        FloatLayout:
            size_hint:None, None
            size:self.parent.size
            pos:self.parent.pos
            FitImage:
                id:profile_image
                pos:self.parent.pos
                source:"male_avater_1.jpeg"
                id:profile_image
                size_hint:None, None
                size:"57dp", "57dp"
                radius:[47, 47, 47, 47]
            MDBoxLayout:
                orientation:"vertical"
                pos:self.parent.pos
                MDBoxLayout:
                    size_hint_y:None
                    height:"30dp"
                    MDBoxLayout:
                        size_hint_x:None
                        width:"40dp"
                    MDBoxLayout:
                        id:ticker_space
                        size_hint:None, None
                        size:"30dp", "30dp"
                        radius:[30, 30, 30, 30]
                        md_bg_color:[255/float(255), 215/float(255), 0/float(255), 1]
                        padding:5
                        MDIcon:
                            id:location_icon
                            icon:"map-marker-check"
                            theme_text_color:"Custom"
                            text_color:[0, 154/float(255), 255/float(255), 1]
                            pos_hint:{"center_x":.5, "center_y":.5}
                MDBoxLayout:
    Widget:
<FriendsListBox>:
    id:friends_list_box
    size_hint_y:None
    height:"85dp"
    ScrollView:
        bar_width:0
        size_hint:None, None
        size:self.parent.size
        pos:self.parent.pos
        FriendsListLayout:
            root:friends_list_box
""")
class UserBox(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coordinates = []
        self.user_image = ""
class UserProfilePicture(TouchBox):
    def respondToTouch(self):
        try:
            self.parent.root.parent.current_selected_profile.ids.ticker_space.md_bg_color = [255/float(255), 215/float(255), 0/float(255), 1]
        except:
            pass
        if self.ids.location_icon.icon == "map-marker-check":
            self.ids.ticker_space.md_bg_color = [0/float(255), 255/float(255), 0/float(255), 1]
            self.parent.root.parent.root.parent.root.locateThisUser(self.parent.root.user_image, self.parent.root.coordinates)
        else:
            self.parent.root.parent.root.parent.root.unLocateThisUser(self.parent.root.coordinates)
            self.ids.ticker_space.md_bg_color = [255/float(255), 0, 0, 1]
        self.parent.root.parent.current_selected_profile = self
class FriendsListLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.current_selected_profile = None
        self.size_hint_x = None
        self.spacing = 2
        self.friends = [["female_avater_1.png", "Minkey", [0, 1], "no_one"]]
        self.bind(minimum_width = self.setter("width"))
        self.listFriends()
    def listFriends(self):
        for friend in self.friends*5:
            user = UserBox()
            user.user_image = friend[0]
            user.ids.profile_image_object.ids.profile_image.source = friend[0]
            user.ids.user_name.text = "@_" + friend[1]
            user.coordinates = friend[2]
            if friend[3] == "no_one":
                user.ids.profile_image_object.ids.location_icon.text_color = [112/float(255), 128/float(255), 144/float(255), 1]
                user.ids.profile_image_object.ids.location_icon.icon = "map-marker-remove-variant"
            self.add_widget(user)
class FriendsListBox(MDBoxLayout):
    pass