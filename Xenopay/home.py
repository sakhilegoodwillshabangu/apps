from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from link import LinkUserScreen
from touch import TouchBox
from settings import SettingsScreen
from kivy.lang import Builder
from wallet import WalletScreen
import _thread as thread
from load import LoadingScreen
from market_view import MarketsViewScreen
from kivy.clock import Clock
import time
ui = Builder.load_string("""
<BasicTouchBox>:
    radius:[20, 20, 20, 20]
    md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
    orientation:"vertical"
    text:""
    icon:""
    MDBoxLayout:
        Widget:
        MDIconButton:
            size_hint:None, None
            size:"60dp", "60dp"
            user_font_size:"40dp"
            icon:root.icon
            theme_text_color:"Custom"
            text_color:[1, 1, 1, 1]
            pos_hint:{"center_x":.5, "center_y":.5}
        Widget:
    MDBoxLayout:
        size_hint_y:None
        height:"50dp"
        MDLabel:
            text:root.text
            text_size:self.size
            halign:"center"
            valign:"middle"
            font_size:"18dp"
            color:[1, 1, 1, 1]
<MenuScreen>:
    name:"menu_screen"
    id:menu_screen
    MDBoxLayout:
        orientation:"vertical"
        MDGridLayout:
            root:menu_screen
            spacing:10
            cols:2
            rows:3
            WalletTouchBox:
                icon:"wallet"
                text:"Wallet"
            LinkUserTouchBox:
                icon:"link-variant-plus"
                text:"Link user"
            PayTouchBox:
                icon:"offer"
                text:"Pay"
            RequestsTouchBox:
                icon:"motion"
                text:"Requests"
            BitcoinMarketTouchBox:
                icon:"bitcoin"
                text:"Crypto Market"
            StockMarketTouchBox:
                icon:"chart-timeline-variant"
                text:"Exchange Market"
<HomeScreen>:
    id:home_screen_object
    name:"home_screen"
    MDBoxLayout:
        md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
        orientation:"vertical"
        padding:"5dp", "5dp"
        spacing:5
        MDBoxLayout:
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            size_hint_y:None
            padding:"10dp", "0dp"
            height:"80dp"
            MDLabel:
                text:"Xenopay"
                font_size:"50dp"
                color:[1, 1, 1, 1]
                text_size:self.size
                halign:"left"
                font_name:"QuiteMagicalRegular-8VA2"
                valign:"middle"
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                pos_hint:{"center_x":.5, "center_y":.5}
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                icon:"exit-to-app"
                on_release:root.logOut()
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                pos_hint:{"center_x":.5, "center_y":.5}
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                icon:"cog"
                on_release:root.goToSettings()
        MDBoxLayout:
            radius:[20, 20, 20, 20]
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            padding:10
            MDBoxLayout:
                ScreenManager:
                    id:body_screen_manager
                    home_screen:home_screen_object
                    MenuScreen:
                    LinkUserScreen:
""")
class BasicTouchBox(TouchBox):
    pass
class WalletTouchBox(BasicTouchBox):
    def goToLoading(self):
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "loading_screen"
    def respondToTouch(self):
        self.main = self.parent.root.parent.home_screen.parent
        Clock.schedule_once(self.parent.root.parent.home_screen.moveToLoadingScreen, 0)
        Clock.schedule_once(self.goToWallet, 1)
    def goToWallet(self, seconds):
        if not self.main.has_screen("wallet_screen"):
            time.sleep(1)
            wallet_screen = WalletScreen()
            self.main.add_widget(wallet_screen)
        self.main.transition = SlideTransition(direction = "left")
        self.main.current = "wallet_screen"
class LinkUserTouchBox(BasicTouchBox):
    def respondToTouch(self):
        self.parent.root.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.current = "link_user_screen"
class PayTouchBox(BasicTouchBox):
    def respondToTouch(self):
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "pay_screen"
class RequestsTouchBox(BasicTouchBox):
    def respondToTouch(self):
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "money_requests_screen"
class BitcoinMarketTouchBox(BasicTouchBox):
    def respondToTouch(self):
        market_view_screen  = MarketsViewScreen()
        self.parent.root.parent.home_screen.parent.add_widget(market_view_screen)
        #market_view_screen = self.parent.root.parent.home_screen.parent.ids.market_view_screen
        market_view_screen.ids.body_screen_manager.transition = NoTransition()
        market_view_screen.ids.body_screen_manager.current = "crypto_market_screen"
        market_view_screen.ids.screen_title.text = "Crypto Markets View"
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "market_view_screen"
        thread.start_new_thread(market_view_screen.plotAllGraphs, ("BTC-USD", "DOGE-USD", "ETH-USD"))
class StockMarketTouchBox(BasicTouchBox):
    def respondToTouch(self):
        market_view_screen  = MarketsViewScreen()
        self.parent.root.parent.home_screen.parent.add_widget(market_view_screen)
        #market_view_screen = self.parent.root.parent.home_screen.parent.ids.market_view_screen
        market_view_screen.ids.body_screen_manager.transition = NoTransition()
        market_view_screen.ids.body_screen_manager.current = "currency_market_screen"
        market_view_screen.ids.screen_title.text = "Exchange Market View"
        self.parent.root.parent.home_screen.parent.transition = SlideTransition(direction = "left")
        self.parent.root.parent.home_screen.parent.current = "market_view_screen"
        thread.start_new_thread(market_view_screen.plotAllGraphs, ("USDZAR=X", "GBPZAR=X", "EURZAR=X"))
class MenuScreen(MDScreen):
    pass
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._parent = None
    def moveToLoadingScreen(self, seconds):
        if not self.parent.has_screen("loading_screen"):
            loading_screen = LoadingScreen()
            self.parent.add_widget(loading_screen)
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "loading_screen"
    def logOut(self):
        pass
    def goToSettings(self):
        if not self.parent.has_screen("settings_screen"):
            settings_screen = SettingsScreen()
            self.parent.add_widget(settings_screen)
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "settings_screen"