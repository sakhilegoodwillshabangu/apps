from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
ui = Builder.load_string("""
<AddPeerScreen>:
    id:add_peer_screen_object
    name:"add_peer_screen"
    MDBoxLayout:
        orientation:"vertical"
        padding:"10dp", "5dp"
        spacing:20
        BoxLayout:
        MDTextField:
            id:email_label_object
            mode:"fill"
            icon_right:"email"
            icon_left_color_normal:[0, 0, 0, 1]
            hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
            radius:[20, 20, 20, 20]
            hint_text:"email@address"
            text:"Email"
            pos_hint:{"center_x":.5, "center_y":.5}
        MDTextField:
            id:relation_label_object
            mode:"fill"
            icon_right:"graph"
            icon_left_color_normal:[0, 0, 0, 1]
            hint_text_color_normal:[120/float(255), 0/float(255), 0/float(255), 1]
            radius:[20, 20, 20, 20]
            hint_text:"relationship"
            text:"Friend"
            pos_hint:{"center_x":.5, "center_y":.5}
        MDBoxLayout:
            root:add_peer_screen_object
            size_hint_y:None
            height:"50dp"
            padding:5
            AddUserButton:
                md_bg_color:[0, 194/float(255), 255/float(255), 1]
                radius:[30, 30, 30, 30]
                MDIconButton:
                    size_hint:None, None
                    size:"40dp", "40dp"
                    icon:"plus"
                    theme_text_color:"Custom"
                    text_color:[120/float(255), 120/float(255), 120/float(255), 1]
                    pos_hint:{"center_x":.5, "center_y":.5}
                MDLabel:
                    text:"Add User"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                BoxLayout:
                    size_hint:None, None
                    size:"40dp", "40dp"
        BoxLayout:
""")
class AddPeerScreen(MDScreen):
    pass
class AddUserButton(MDBoxLayout):
    def on_touch_down(self, touch):
        if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and (touch.y - self.pos[1]) < self.size[1])):
            self.respondToTouch()
    def respondToTouch(self):
	    email = self.parent.root.ids.email_label_object.text
	    relation = self.parent.root.ids.relation_label_object.text
	    print(email, relation)