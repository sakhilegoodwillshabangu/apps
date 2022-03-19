from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, FadeTransition
from kivy.lang import Builder
from load import LoadingScreen
from touch import TouchBox
ui = Builder.load_string("""
<PendingRequestsScreen>:
    name:"pending_requests_screen"
    MDBoxLayout:
        ScrollView:
            size_hint:None, None
            size:self.parent.size
            PendingRequestsLayout:
<ApprovedRequestsScreen>:
    name:"approved_requests_screen"
    MDBoxLayout:
        ScrollView:
            size_hint:None, None
            size:self.parent.size
            ApprovedRequestsLayout:
<DeclinedReqeustsScreen>:
    name:"declined_requests_screen"
    MDBoxLayout:
        ScrollView:
            size_hint:None, None
            size:self.parent.size
            DeclinedRequestsLayout:
<MoneyRequestBar>:
    md_bg_color:[230/float(255), 230/float(255), 230/float(255), 1]
    size_hint_y:None
    height:"100dp"
    radius:[20, 20, 20, 20]
    padding:"5dp", "0dp"
    orientation:"vertical"
    MDBoxLayout:
        size_hint_y:None
        height:"50dp"
        MDBoxLayout:
            size_hint:None, None
            size:"40dp", "40dp"
            radius:[30, 30, 30, 30]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            pos_hint:{"center_y":.5}
            MDLabel:
                text:"G"
                id:first_letter
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
        MDBoxLayout:
            orientation:"vertical"
            padding:"5dp", "0dp"
            MDBoxLayout:
                MDLabel:
                    id:email
                    text:"email@address"
                    text_size:self.size
                    halign:"left"
                    bold:True
                    valign:"middle"
            MDBoxLayout:
                MDLabel:
                    id:username
                    text:"-Username"
                    text_size:self.size
                    halign:"left"
                    color:[120/float(255), 120/float(255), 120/float(255), 1]
                    valign:"middle"
    MDBoxLayout:
        size_hint_y:None
        height:"50dp"
        Widget:
        MDBoxLayout:
            size_hint_x:None
            width:"160dp"
            padding:"5dp", "5dp"
            MDBoxLayout:
                id:status
                md_bg_color:[180/float(255), 180/float(255), 180/float(255), 1]
                size_hint:None, None
                size:"150dp", "40dp"
                radius:[30, 30, 30, 30]
                MDLabel:
                    id:status_label
                    text:"Pending"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[60/float(255), 60/float(255), 60/float(255), 1]
                MDIconButton:
                    size_hint:None, None
                    size:"20dp", "20dp"
                    user_font_size:"20dp"
                    icon:"close"
                    theme_text_color:"Custom"
                    text_color:[220/float(255), 20/float(255), 60/float(255), 1]
                    pos_hint:{"center_x":.5, "center_y":.5}
<MyMoneyRequests>:
    id:my_money_requests
    name:"my_money_requests"
    MDBoxLayout:
        md_bg_color:[0, 0, 0, 1]
        padding:5
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[20, 20, 0, 0]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                pos_hint:{"center_y":.5}
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                on_release:root.goBack()
            MDLabel:
                text:"Money request made"
                font_size:"24dp"
                color:[1, 1, 1, 1]
                text_size:self.size
                halign:"center"
                valign:"middle"
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            radius:[0, 0, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDBoxLayout:
                md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                radius:[30, 30, 20, 20]
                orientation:"vertical"
                MDBoxLayout:
                    root:my_money_requests
                    size_hint_y:None
                    height:"50dp"
                    PendingButtonBox:
                        MDLabel:
                            id:pending_label
                            text:"Pending"
                            text_size:self.size
                            halign:"center"
                            valign:"middle"
                            color:[0, 154/float(255), 255/float(255), 1]
                    ApprovedButtonBox:
                        MDLabel:
                            id:approved_label
                            text:"Approved"
                            text_size:self.size
                            halign:"center"
                            valign:"middle"
                    DeclinedButtonBox:
                        MDLabel:
                            id:declined_label
                            text:"Declined"
                            text_size:self.size
                            halign:"center"
                            valign:"middle"
                MDBoxLayout:
                    ScreenManager:
                        id:body_screen_manager
                        PendingRequestsScreen:
                        ApprovedRequestsScreen:
                        DeclinedReqeustsScreen:
                        LoadingScreen:
""")
class MoneyRequestBar(MDBoxLayout):
    pass
class PendingRequestsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.requests = [1]
        self.padding = "10dp", "10dp"
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addRequests()
    def addRequests(self):
        for request in self.requests * 5:
            pending_request = MoneyRequestBar()
            self.add_widget(pending_request)
class ApprovedRequestsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 2
        self.requests = [1]
        self.padding = "5dp", "5dp"
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addRequests()
    def addRequests(self):
        for request in self.requests * 5:
            approved_request = MoneyRequestBar()
            approved_request.ids.status.md_bg_color = [0, 255/float(255), 154/float(255), 1]
            self.add_widget(approved_request)
class DeclinedRequestsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 2
        self.requests = [1]
        self.padding = "5dp", "5dp"
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addRequests()
    def addRequests(self):
        for request in self.requests * 5:
            declined_request = MoneyRequestBar()
            declined_request.ids.status.md_bg_color = [40/float(255), 40/float(255), 40/float(255), 1]
            declined_request.ids.status_label.color = [1, 1, 1, 1]
            self.add_widget(declined_request)
class PendingRequestsScreen(MDScreen):
    pass
class ApprovedRequestsScreen(MDScreen):
    pass
class DeclinedReqeustsScreen(MDScreen):
    pass
class PendingButtonBox(TouchBox):
    def respondToTouch(self):
        self.parent.root.turnAllButtonLabelsBlack()
        self.parent.root.ids.pending_label.color = [0, 154/float(255), 255/float(255), 1]
        if not self.parent.root.ids.body_screen_manager.has_screen("pending_requests_screen"):
            screen = PendingRequestsScreen()
            self.parent.root.ids.body_screen_manager.add_widget(screen)
        self.parent.root.ids.body_screen_manager.transition = FadeTransition()
        self.parent.root.ids.body_screen_manager.current = "pending_requests_screen"
class ApprovedButtonBox(TouchBox):
    def respondToTouch(self):
        self.parent.root.turnAllButtonLabelsBlack()
        self.parent.root.ids.approved_label.color = [0, 154/float(255), 255/float(255), 1]
        if not self.parent.root.ids.body_screen_manager.has_screen("approved_requests_screen"):
            screen = ApprovedRequestsScreen()
            self.parent.root.ids.body_screen_manager.add_widget(screen)
        self.parent.root.ids.body_screen_manager.transition = FadeTransition()
        self.parent.root.ids.body_screen_manager.current = "approved_requests_screen"
class DeclinedButtonBox(TouchBox):
    def respondToTouch(self):
        self.parent.root.turnAllButtonLabelsBlack()
        self.parent.root.ids.declined_label.color = [0, 154/float(255), 255/float(255), 1]
        if not self.parent.root.ids.body_screen_manager.has_screen("declined_requests_screen"):
            screen = DeclinedReqeustsScreen()
            self.parent.root.ids.body_screen_manager.add_widget(screen)
        self.parent.root.ids.body_screen_manager.transition = FadeTransition()
        self.parent.root.ids.body_screen_manager.current = "declined_requests_screen"
class MyMoneyRequests(MDScreen):
    def goBack(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "who_to_pay_screen"
    def turnAllButtonLabelsBlack(self):
        self.ids.pending_label.color = [0, 0/float(255), 0/float(255), 1]
        self.ids.approved_label.color = [0, 0/float(255), 0/float(255), 1]
        self.ids.declined_label.color = [0, 0/float(255), 0/float(255), 1]
class Test(MDApp):
    def build(self):
        root = MyMoneyRequests()
        return root
if __name__ == "__main__":
    Test().run()