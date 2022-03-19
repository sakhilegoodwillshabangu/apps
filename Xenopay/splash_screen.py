from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<SplashScreen>:
    name:"splash_screen"
    MDBoxLayout:
        md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
        orientation:"vertical"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            Widget:
            MDBoxLayout:
                size_hint:None, None
                size:"200dp", "200dp"
                md_bg_color:[0/float(255), 154/float(255), 255/float(255), 1]
                radius:[190, 190, 190, 190]
                pos_hint:{"center_x":.5, "center_y":.5}
                Widget:
                FitImage:
                    size_hint:None, None
                    size:"196dp", "196dp"
                    source:"xenopay_logo.jpg"
                    radius:[186, 186, 186, 186]
                    pos_hint:{"center_x":.5, "center_y":.5}
                Widget:
            Widget:
""")
class SplashScreen(MDScreen):
    pass