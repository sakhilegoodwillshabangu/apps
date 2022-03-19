from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition, FadeTransition
from kivymd.uix.gridlayout import MDGridLayout
from touch import TouchBox
from load import LoadingScreen
from kivy.lang import Builder
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
ui = Builder.load_string("""
<MarketBarBox>:
    orientation:"vertical"
    id:market_bar_box
    ticker_logo:""
    ticker_symbol:""
    text_color:[0, 0, 0, 1]
    spacing:10
    size_hint_x:None
    width:"150dp"
    MDBoxLayout:
        padding:"5dp", "0dp"
        radius:[20, 20, 20, 20]
        md_bg_color:[82/float(255), 71/float(255), 149/float(255), 1]
        MDBoxLayout:
            size_hint_x:None
            width:"50dp"
            MDBoxLayout:
                orientation:"vertical"
                size_hint:None, None
                size:"40dp", "40dp"
                radius:[30, 30, 30, 30]
                md_bg_color:[1, 1, 1, 1]
                pos_hint:{"center_y":.5}
                Widget:
                FitImage:
                    size_hint:None, None
                    size:"38dp", "38dp"
                    radius:[28, 28, 28, 28]
                    source:market_bar_box.ticker_logo
                    pos_hint:{"center_x":.5, "center_y":.5}
                Widget:
        MDBoxLayout:
            MDLabel:
                text:market_bar_box.ticker_symbol
                bold:True
                color:market_bar_box.text_color
                text_size:self.size
                halign:"center"
                valign:"middle"
<MarketContent>:
    orientation:"vertical"
    MDBoxLayout:
        size_hint_y:None
        height:"30dp"
        MDLabel:
            id:price
            text:""
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[1, 1, 1, 1]
    MDBoxLayout:
        size_hint_y:None
        height:"20dp"
        MDLabel:
            id:percentage
            text:""
            text_size:self.size
            halign:"center"
            valign:"middle"
            color:[0, 1, 0, 1]
    MDBoxLayout:
        Widget:
        FitImage:
            id:graph
            size_hint:None, None
            size:"300dp", "250dp"
            pos_hint:{"center_x":.5, "center_y":.5}
            source:""
        Widget:
<MarketsViewScreen>:
    name:"market_view_screen"
    id:markets_view_screen
    MDBoxLayout:
        orientation:"vertical"
        spacing:0
        padding:"5dp"
        md_bg_color:[0, 0, 0, 1]
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            size_hint_y:None
            height:"80dp"
            radius:[20, 20, 0, 0]
            MDIconButton:
                size_hint:None, None
                size:"50dp", "50dp"
                user_font_size:"30dp"
                icon:"arrow-left-thick"
                theme_text_color:"Custom"
                text_color:[1, 1, 1, 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_release:root.goBackToHomeScreen()
            MDLabel:
                id:screen_title
                text:"Crypto Markets View"
                font_size:"23dp"
                text_size:self.size
                halign:"center"
                valign:"middle"
                color:[1, 1, 1, 1]
            MDBoxLayout:
                size_hint_x:None
                width:"50dp"
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            radius:[0, 0, 20, 20]
            ScreenManager:
                id:body_screen_manager
                MDScreen:
                    name:"crypto_market_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"100dp"
                            spacing:5
                            ScrollView:
                                bar_width:0
                                size_hint:None, None
                                size:self.parent.size
                                pos:self.parent.pos
                                CryptoMarketsLayout:
                                    root:markets_view_screen
                                    CryptoMarketsBarBox:
                                        ticker_logo:"bitcoin.jpeg"
                                        ticker_symbol:"BTC-USD"
                                        text_color:[0, 1, 154/float(255), 1]
                                    CryptoMarketsBarBox:
                                        ticker_logo:"dogecoin.png"
                                        ticker_symbol:"DOGE-USD"
                                    CryptoMarketsBarBox:
                                        ticker_logo:"ethereum.jpeg"
                                        ticker_symbol:"ETH-USD"
                        MDBoxLayout:
                            ScreenManager:
                                id:crypto_graph_screen
                                LoadingScreen:
                                MDScreen:
                                    name:"bitcoin_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:bitcoin_rand_content_space
                                MDScreen:
                                    name:"dogecoin_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:dogecoin_rand_content_space
                                MDScreen:
                                    name:"ethereum_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:ethereum_rand_content_space
                MDScreen:
                    name:"currency_market_screen"
                    MDBoxLayout:
                        orientation:"vertical"
                        MDBoxLayout:
                            size_hint_y:None
                            height:"100dp"
                            spacing:5
                            ScrollView:
                                bar_width:0
                                size_hint:None, None
                                size:self.parent.size
                                pos:self.parent.pos
                                ExChangeMarketsLayout:
                                    root:markets_view_screen
                                    ExChangeMarketsBarBox:
                                        ticker_logo:"dollar.png"
                                        ticker_symbol:"USDZAR=X"
                                        text_color:[0, 1, 154/float(255), 1]
                                    ExChangeMarketsBarBox:
                                        ticker_logo:"pound.png"
                                        ticker_symbol:"GBPZAR=X"
                                    ExChangeMarketsBarBox:
                                        ticker_logo:"euro.jpeg"
                                        ticker_symbol:"EURZAR=X"
                        MDBoxLayout:
                            ScreenManager:
                                id:exchange_graph_screen
                                LoadingScreen:
                                MDScreen:
                                    name:"dollar_rand_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:dollar_rand_content_space
                                MDScreen:
                                    name:"pound_rand_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:pound_rand_content_space
                                MDScreen:
                                    name:"euro_rand_price_screen"
                                    MDBoxLayout:
                                        MarketContent:
                                            id:euro_rand_content_space
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            padding:[0, 10, 0, 0]
            MDBoxLayout:
                md_bg_color:[0, 154/float(255), 1, 1]
                radius:[30, 30, 30, 30]
                MDLabel:
                    text:"Refresh"
                    text_size:self.size
                    halign:"center"
                    valign:"middle"
                    color:[1, 1, 1, 1]
""")
class MarketBarBox(TouchBox):
    pass
class ExChangeMarketsBarBox(MarketBarBox):
    def updateUsdZarPriceOnScreen(self):
        self.parent.root.ids.dollar_rand_content_space.ids.price.text = "USD-ZAR price R" + str(self.parent.root.ex_data["USDZAR=X"][0])
        self.parent.root.ids.dollar_rand_content_space.ids.percentage.text = "(" + str(self.parent.root.ex_data["USDZAR=X"][1]) +"%" + ")"
        self.parent.root.ids.dollar_rand_content_space.ids.graph.source = self.parent.root.ex_data["USDZAR=X"][2]
    def updateGbpZarPriceOnScreen(self):
        self.parent.root.ids.pound_rand_content_space.ids.price.text = "GBP-ZAR price R" + str(self.parent.root.ex_data["GBPZAR=X"][0])
        self.parent.root.ids.pound_rand_content_space.ids.percentage.text = "(" + str(self.parent.root.ex_data["GBPZAR=X"][1]) + "%" + ")"
        self.parent.root.ids.pound_rand_content_space.ids.graph.source = self.parent.root.ex_data["GBPZAR=X"][2]
    def updateEurZarPriceOnScreen(self):
        self.parent.root.ids.euro_rand_content_space.ids.price.text = "EUR-ZAR price R" + str(self.parent.root.ex_data["EURZAR=X"][0])
        self.parent.root.ids.euro_rand_content_space.ids.percentage.text = "(" + str(self.parent.root.ex_data["EURZAR=X"][1]) + "%" + ")"
        self.parent.root.ids.euro_rand_content_space.ids.graph.source = self.parent.root.ex_data["EURZAR=X"][2]
    def respondToTouch(self):
        children = self.parent.children
        if not self.parent.root.ids.exchange_graph_screen.current == "loading_screen":
            for _object in children:
                _object.text_color = [0, 0, 0, 1]
        if self.ticker_symbol == "USDZAR=X":
            if self.parent.root.ids.exchange_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.exchange_graph_screen.transition = FadeTransition()
                self.parent.root.ids.exchange_graph_screen.current = "dollar_rand_price_screen"
                self.updateUsdZarPriceOnScreen()
        elif self.ticker_symbol == "GBPZAR=X":
            if self.parent.root.ids.exchange_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.exchange_graph_screen.transition = FadeTransition()
                self.parent.root.ids.exchange_graph_screen.current = "pound_rand_price_screen"
                self.updateGbpZarPriceOnScreen()
        elif self.ticker_symbol == "EURZAR=X":
            if self.parent.root.ids.exchange_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.exchange_graph_screen.transition = FadeTransition()
                self.parent.root.ids.exchange_graph_screen.current = "euro_rand_price_screen"
                self.updateEurZarPriceOnScreen()
class MarketContent(MDBoxLayout):
    pass
class CryptoMarketsBarBox(MarketBarBox):
    def updateBitCoinPriceOnScreen(self):
        self.parent.root.ids.bitcoin_rand_content_space.ids.price.text = "BTC-USD price $" + str(self.parent.root.crypto_data["BTC-USD"][0])
        self.parent.root.ids.bitcoin_rand_content_space.ids.percentage.text = "(" + str(self.parent.root.crypto_data["BTC-USD"][1]) +"%" +")"
        self.parent.root.ids.bitcoin_rand_content_space.ids.graph.source = str(self.parent.root.crypto_data["BTC-USD"][2])
    def updateDogeCoinPriceOnScreen(self):
        self.parent.root.ids.dogecoin_rand_content_space.ids.price.text = "DOGE-USD price $" + str(self.parent.root.crypto_data["DOGE-USD"][0])
        self.parent.root.ids.dogecoin_rand_content_space.ids.percentage.text = "(" + str(self.parent.root.crypto_data["DOGE-USD"][1]) + "%" +")"
        self.parent.root.ids.dogecoin_rand_content_space.ids.graph.source = str(self.parent.root.crypto_data["DOGE-USD"][2])
    def updateEthereumPriceOnScreen(self):
        self.parent.root.ids.ethereum_rand_content_space.ids.price.text = "ETH-USD price $" + str(self.parent.root.crypto_data["ETH-USD"][0])
        self.parent.root.ids.ethereum_rand_content_space.ids.percentage.text = "(" +str(self.parent.root.crypto_data["ETH-USD"][1]) + "%" + ")"
        self.parent.root.ids.ethereum_rand_content_space.ids.graph.source = str(self.parent.root.crypto_data["ETH-USD"][2])
    def respondToTouch(self):
        children = self.parent.children
        if not self.parent.root.ids.crypto_graph_screen.current == "loading_screen":
            for _object in children:
                _object.text_color = [0, 0, 0, 1]
        if self.ticker_symbol == "BTC-USD":
            if self.parent.root.ids.crypto_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.crypto_graph_screen.transition = FadeTransition()
                self.parent.root.ids.crypto_graph_screen.current = "bitcoin_price_screen"
                self.updateBitCoinPriceOnScreen()
        elif self.ticker_symbol == "DOGE-USD":
            if self.parent.root.ids.crypto_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.crypto_graph_screen.transition = FadeTransition()
                self.parent.root.ids.crypto_graph_screen.current = "dogecoin_price_screen"
                self.updateDogeCoinPriceOnScreen()
        elif self.ticker_symbol == "ETH-USD":
            if self.parent.root.ids.crypto_graph_screen.current == "loading_screen":
                pass
            else:
                self.text_color = [0, 1, 154/float(255), 1]
                self.parent.root.ids.crypto_graph_screen.transition = FadeTransition()
                self.parent.root.ids.crypto_graph_screen.current = "ethereum_price_screen"
                self.updateEthereumPriceOnScreen()
class CryptoMarketsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.spacing = 5
        self.padding = ("5dp", "5dp")
        self.size_hint_x = None
        self.bind(minimum_width = self.setter("width"))
class ExChangeMarketsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.spacing = 5
        self.padding = ("5dp", "5dp")
        self.size_hint_x = None
        self.bind(minimum_width = self.setter("width"))
class MarketsViewScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.crypto_data = dict()
        self.ex_data = dict()
    def goBackToHomeScreen(self):
        self.parent.transition = SlideTransition(direction = "right")
        self.parent.current = "home_screen"
    def fetchMarketData(self, currency_name):
        df = yf.Ticker(currency_name).history(period = "1d", interval = "1m")
        df2 = df.resample("1T").agg({
                        "Open":"first", 
                        "High":"max", 
                        "Low":"min", 
                        "Close":"last"
                        })
        file_name = currency_name.replace("=", "")
        file_name = currency_name.replace(".", "")
        df2.to_csv(file_name + ".csv")
    def plotAllGraphs(self, *curr):
        self.plotGraph(curr[0])
        self.plotGraph(curr[1])
        self.plotGraph(curr[2])
        if curr[0] == "BTC-USD":
            self.ids.bitcoin_rand_content_space.ids.price.text = "BTC-USD price $" + str(self.crypto_data[curr[0]][0])
            self.ids.bitcoin_rand_content_space.ids.percentage.text ="(" + str(self.crypto_data[curr[0]][1]) + "%" +")"
            self.ids.bitcoin_rand_content_space.ids.graph.source = str(self.crypto_data[curr[0]][2])
            self.ids.crypto_graph_screen.transition = SlideTransition(direction = "left")
            self.ids.crypto_graph_screen.current = "bitcoin_price_screen"
        else:
            self.ids.dollar_rand_content_space.ids.price.text = "USD-ZAR price R" + str(self.ex_data[curr[0]][0])
            self.ids.dollar_rand_content_space.ids.percentage.text = "(" + str(self.ex_data[curr[0]][1]) +"%" + ")"
            self.ids.dollar_rand_content_space.ids.graph.source = self.ex_data[curr[0]][2]
            self.ids.exchange_graph_screen.transition = SlideTransition(direction = "left")
            self.ids.exchange_graph_screen.current = "dollar_rand_price_screen"
    def getExchangePricesInfo(self, price_title, currency):
        self.ids.dollar_rand_content_space.ids.price.text = price_title + str(self.ex_data[currency][0])
        self.ids.dollar_rand_content_space.ids.percentage.text = "(" + str(self.ex_data[currency][1]) +"%" + ")"
        self.ids.dollar_rand_content_space.ids.graph.source = self.ex_data[currency][2]
    def getCryptoPriceInfo(self, price_title, currency):
        self.ids.bitcoin_rand_content_space.ids.price.text = price_title + str(self.crypto_data[currency][0])
        self.ids.bitcoin_rand_content_space.ids.percentage.text ="(" + str(self.crypto_data[currency][1]) + "%" +")"
        self.ids.bitcoin_rand_content_space.ids.graph.source = str(self.crypto_data[currency][2])
    def plotGraph(self, currency_name):
        file_name = currency_name.replace("=", "")
        file_name = file_name.replace(".", "")
        print("File Name :", file_name)
        df = pd.read_csv(file_name + ".csv")
        x = df.index
        y1 = df["Close"]
        y2 = df["Open"]
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        curve1 = ax1.plot(x, y1, label = "Close", color = "b")
        curve2 = ax2.plot(x, y2, label = "Open", color = "w")
        fig.patch.set_facecolor((72/float(255), 61/float(255), 139/float(255), 1))
        ax1.patch.set_facecolor((72/float(255), 61/float(255), 139/float(255), 1))
        plt.plot()
        ax1.grid(False)
        ax2.grid(False)
        ax1.axis("off")
        ax2.axis("off")
        fig.set_dpi(250)
        fig.savefig(file_name + ".png")
        self.fillMarketData(file_name, currency_name, df)
    def fillMarketData(self, file_name, currency_name, file_object):
        open = file_object["Open"][0]
        close = round(file_object["Close"][len(file_object) - 1], 2)
        perc = round(((close - open)/float(open)) * 100, 2)
        image_file = file_name + ".png"
        if currency_name in ["USDZAR=X", "GBPZAR=X", "EURZAR=X"]:
            self.ex_data[currency_name] = [close, perc, image_file]
        elif currency_name in ["BTC-USD", "DOGE-USD", "ETH-USD"]:
            self.crypto_data[currency_name] = [close, perc, image_file]