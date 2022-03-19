from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
import _thread as thread
import time
ui = Builder.load_string("""
<LoadingScreen>:
    id:loading_screen
    name:"loading_screen"
    MDBoxLayout:
        md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
        MDBoxLayout:
            md_bg_color:[72/float(255), 61/float(255), 139/float(255), 1]
            orientation:"vertical"
            Widget:
            MDBoxLayout:
                size_hint:None, None
                size:"150dp", "150dp"
                pos_hint:{"center_x":.5, "center_y":.5}
                LoadingGrid:
                    root:loading_screen
                    id:loading_grid
                    
                    cols:3
                    rows:3
            Widget:
""")
class LoadingGrid(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.putBlocksInGrid()
    def putBlocksInGrid(self):
        for i in range(9):
            if i in [1, 2, 4, 7]:
                box = MDBoxLayout(md_bg_color = [0, 255/float(255), 154/float(255), 1])
            else:
                box = MDBoxLayout(md_bg_color = [72/float(255), 61/float(255), 139/float(255), 1])
            self.add_widget(box)
        #thread.start_new_thread(self.walkBoxes, ())
    def walkBoxes(self):
        while True:
            self.moveBoxes([2, 5, 8, 7, 6, 3, 0, 2])
    def moveBoxes(self, indexes_list):
        blocks = indexes_list
        while blocks:
            if len(blocks) == 1:
                self.children[blocks[0] - 9].md_bg_color = [0, 255/float(255), 154/float(255), 1]
                blocks = []
            else:
                if blocks[0] not in [1, 4, 7]:
                    print(":+:+:+!!669 :", blocks[0], "len is :", len(self.root.ids.loading_grid.children))
                    self.root.ids.loading_grid.children[blocks[0] - 9].md_bg_color = [72/float(255), 61/float(255), 139/float(255), 1]
                self.root.ids.loading_grid.children[blocks[1] - 9].md_bg_color = [0/float(255), 255/float(255), 154/float(255), 1]
                blocks = blocks[1:]
            time.sleep(.2)
class LoadingScreen(MDScreen):
    pass