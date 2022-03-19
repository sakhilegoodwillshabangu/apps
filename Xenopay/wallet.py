from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import SlideTransition
from touch import TouchBox
from load import LoadingScreen
from kivy.lang import Builder
ui = Builder.load_string("""
<TransactionBarBox>:
    size_hint_y:None
    height:"70dp"
    radius:[10, 40, 10, 40]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    padding:"10dp", "10dp"
    MDBoxLayout:
        id:circle
        size_hint:None, None
        size:"50dp", "50dp"
        md_bg_color:[0, 1, 0, 1]
        radius:[40, 40, 40, 40]
        MDLabel:
            id:name_first_letter
            text:"S"
            text_size:self.size
            halign:"center"
            valign:"middle"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:email_address
                text:"email@address"
                bold:True
                text_size:self.size
                halign:"left"
                valign:"middle"
        MDBoxLayout:
            padding:"10dp", "0dp"
            MDLabel:
                id:date_and_time
                text:"01/Jan/2000"
                text_size:self.size
                halign:"left"
                color:[140/float(255), 140/float(255), 140/float(255), 1]
                valign:"middle"
    MDBoxLayout:
        size_hint_x:None
        width:transaction_amount_label.width
        MDLabel:
            id:transaction_amount_label
            text:"+R1200"
            bold:True
            text_size:None, self.height
            size_hint:None, 1
            width:self.texture_size[0]
            color:[0/float(255), 255/float(255), 0/float(255), 1]
<WalletScreen>:
    name:"wallet_screen"
    id:wallet_screen
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0, 0, 0, 1]
        padding:"5dp", "5dp"
        MDBoxLayout:
            size_hint_y:None
            height:"80dp"
            radius:[20, 20, 0, 0]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackHome()
            MDLabel:
                text:"Wallet"
                font_size:"23dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            radius:[0, 0, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:"5dp", "0dp"
                MDBoxLayout:
                    size_hint_x:None
                    width:label_one.width
                    MDLabel:
                        id:label_one
                        text:"Available Balance R "
                        color:[220/float(255), 220/float(255), 220/float(255), 1]
                        font_size:"18dp"
                        size_hint:None, 1
                        font_name:"CarandaPersonalUse-qLOq"
                        text_size:None, self.height
                        halign:"center"
                        valign:"middle"
                        width:self.texture_size[0]
                MDBoxLayout:
                    size_hint_x:None
                    width:label_two.width
                    MDLabel:
                        id:label_two
                        text:":"
                        bold:True
                        color:[1, 1, 1, 1]
                        font_size:"18dp"
                        text_size:None, self.height
                        size_hint:None, 1
                        halign:"left"
                        valign:"middle"
                        width:self.texture_size[0]
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                padding:"10dp", "5dp"
                spacing:5
                CashOutButtonBox:
                    id:cash_out_button_box
                    root:wallet_screen
                    size_hint_y:None
                    height:"40dp"
                    radius:[30, 30, 30, 30]
                    md_bg_color:[0, 154/float(255), 255/float(255), 1]
                    MDLabel:
                        text:"Cash-out"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        color:[1, 1, 1, 1]
                CashInButtonBox:
                    id:cash_in_button_box
                    root:wallet_screen
                    size_hint_y:None
                    height:"40dp"
                    radius:[30, 30, 30, 30]
                    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
                    MDLabel:
                        text:"Cash-in"
                        text_size:self.size
                        halign:"center"
                        valign:"middle"
                        color:[1, 1, 1, 1]
            MDBoxLayout:
                orientation:"vertical"
                padding:"5dp", "0dp"
                ScreenManager:
                    id:body_screen_manager
                    LoadingScreen:
                    MDScreen:
                        name:"cash_out"
                        MDBoxLayout:
                            orientation:"vertical"
                            ScrollView:
                                bar_width:0
                                size_hint:None, None
                                size:self.parent.size
                                CashOutLayout:
                                    id:cash_out_layout
                    MDScreen:
                        name:"cash_in"
                        MDBoxLayout:
                            orientation:"vertical"
                            ScrollView:
                                bar_width:0
                                size_hint:None, None
                                size:self.parent.size
                                CashInLayout:
                                    id:cash_in_layout
""")
class TransactionBarBox(MDBoxLayout):
    pass
class CashOutButtonBox(TouchBox):
    def respondToTouch(self):
        if self.root.ids.cash_out_layout.cash_out:
            self.root.ids.cash_out_button_box.md_bg_color = [0/float(255), 154/float(255), 255/float(255), 1]
            self.root.ids.cash_in_button_box.md_bg_color = [82/float(255), 71/float(255), 149/float(255), 1]
            self.root.ids.body_screen_manager.transition = SlideTransition(direction = "left")
            self.root.ids.body_screen_manager.current = "cash_out"
class CashInButtonBox(TouchBox):
    def respondToTouch(self):
        if self.root.ids.cash_in_layout.cash_in:
            self.root.ids.cash_out_button_box.md_bg_color = [82/float(255), 71/float(255), 149/float(255), 1]
            self.root.ids.cash_in_button_box.md_bg_color = [0, 154/float(255), 255/float(255), 1]
            self.root.ids.body_screen_manager.transition = SlideTransition(direction = "right")
            self.root.ids.body_screen_manager.current = "cash_in"
class CashOutLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.padding = "0dp", "10dp"
        self.cash_out = [["goodwill@gmail.com", "10/Dec/2020 time 10:40", "4000"]]
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addMoneyOut()
    def addMoneyOut(self):
        for user in self.cash_out:
            transaction_bar_box = TransactionBarBox()
            transaction_bar_box.ids.name_first_letter.text = user[0][0].upper()
            transaction_bar_box.ids.email_address.text = user[0]
            transaction_bar_box.ids.date_and_time.text = user[1]
            transaction_bar_box.ids.transaction_amount_label.color = [255/float(255), 69/float(255), 0/float(255), 1]
            transaction_bar_box.ids.transaction_amount_label.text = "-R" + user[2]
            self.add_widget(transaction_bar_box)
class CashInLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.spacing = 5
        self.padding = "0dp", "10dp"
        self.cash_in = [["sakhi@gmail.com", "10/Dec/2020 time 10:40", "4000"]]
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
        self.addMoneyIn()
    def addMoneyIn(self):
        for user in self.cash_in:
            transaction_bar_box = TransactionBarBox()
            transaction_bar_box.ids.name_first_letter.text = user[0][0].upper()
            transaction_bar_box.ids.email_address.text = user[0]
            transaction_bar_box.ids.date_and_time.text = user[1]
            transaction_bar_box.ids.transaction_amount_label.text = "+R" + user[2]
            self.add_widget(transaction_bar_box)
class WalletScreen(MDScreen):
    def goBackHome(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"