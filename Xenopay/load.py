from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
loader = None
ui = Builder.load_string("""
<LoadingScreen>:
    name:"loading_screen"
    MDBoxLayout:
        md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
        orientation:"vertical"
        Widget:
        MDBoxLayout:
            size_hint:None, None
            size:"50dp", "50dp"
            radius:[40, 40, 40, 40]
            pos_hint:{"center_x":.5, "center_y":.5}
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
        Widget:
""")
class LoadingScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def startLoad(self):
        self.ids.gif.anim_delay = 0.01
        #self.ids.gif._coreimage.anim_reset(True)