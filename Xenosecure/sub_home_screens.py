import math
import os
import _thread as thread
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.utils.fitimage import FitImage
from kivymd.uix.imagelist import SmartTile
from kivy.uix.screenmanager import SlideTransition
from kivy.core.audio import SoundLoader
import pickle
from kivy.lang import Builder
ui = Builder.load_string("""
<MediaFileBar>:
    id:media_file_bar
    size_hint_y:None
    height:"50dp"
    PlayButtonBox:
        root:media_file_bar
        size_hint:None, None
        size:"50dp", "50dp"
        MDIcon:
            id:media_icon_object
            user_font_size:"30dp"
            icon:"play"
            theme_text_color:"Custom"
            text_color:[190/float(255), 190/float(255), 190/float(255), 1]
            pos_hint:{"center_x":.5, "center_y":.5}
    MDLabel:
        id:file_name
        shorten:True
        text:"file_name"
        text_size:self.size
        valign:"middle"
        halign:"left"
        color:[1, 1, 1, 1]
    EncryptButtonBox:
        size_hint:None, None
        size:"100dp", "40dp"
        radius:[30, 30, 30, 30]
        md_bg_color:[35/float(255), 35/float(255), 122/float(255), 1]
        MDLabel:
            id:encrypt_button_label
            text:"encrypt file"
            color:[190/float(255), 190/float(255), 190/float(255), 1]
            text_size:self.size
            halign:"center"
            valign:"middle"
<VideoFilesScreen>:
    name:"video_files_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            radius:[40, 40, 40, 40]
            size_hint_y:None
            height:"60dp"
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            MDLabel:
                text:"Video files"
                font_size:"20dp"
                text_size:self.size
                valign:"middle"
                halign:"center"
        MDBoxLayout:
            id:current_box
            ScrollView:
                id:video_scroll_view
                size_hint:None, None
                size:current_box.size
<MusicFilesScreen>:
    name:"music_files_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            radius:[40, 40, 40, 40]
            size_hint_y:None
            height:"60dp"
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            MDLabel:
                text:"Music files"
                font_size:"20dp"
                text_size:self.size
                valign:"middle"
                halign:"center"
        MDBoxLayout:
            id:music_list_box
            ScrollView:
                id:music_scroll_view
                size_hint:None, None
                size:music_list_box.size
<ImageTile>:
    radius:[10, 10, 10, 10]
    id:image_object
    size_hint_y:None
    height:"200dp"
    source:"images.jpeg"
<ImagesFilesScreen>:
    id:images_files_screen
    name:"images_files_screen"
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            radius:[40, 40, 40, 40]
            size_hint_y:None
            height:"60dp"
            md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
            MDLabel:
                text:"Images files"
                font_size:"20dp"
                text_size:self.size
                valign:"middle"
                halign:"center"
        MDBoxLayout:
            id:images_list_box
            ScrollView:
                root:images_files_screen
                id:images_scroll_view
                size_hint:None, None
                size:images_list_box.size
""")
class TouchBox(MDBoxLayout):
    def on_touch_down(self, touch):
        x_size = self.pos[0] + self.size[0]
        y_size = self.pos[1] + self.size[1]
        if ((touch.x > self.pos[0] and touch.x < x_size) and (touch.y > self.pos[1] and touch.y < y_size)):
            self.respondToTouch()
    def respondToTouch(self):
        pass
class VideoFilesScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        print(self.parent)
        self.files = self.parent
class PlayButtonBox(TouchBox):
    def playSound(self, file_name):
        self.parent.ids.media_icon_object.text_color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.parent.ids.file_name.color = [20/float(255), 20/float(255), 20/float(255), 1]
        self.parent.parent.sound = SoundLoader.load(file_name)
        self.parent.parent.sound.play()
    def stopSound(self):
        self.parent.parent.sound.stop()
        self.parent.ids.media_icon_object.text_color = [190/float(255), 190/float(255), 190/float(255), 1]
        self.parent.ids.file_name.color = [190/float(255), 190/float(255), 190/float(255), 1]
    def respondToTouch(self):
        print("Respond to play sound buttontouch")
        if self.parent.file_type == "Music":
            print("file type is music")
            file_name = self.root.file_name
            for _object in self.parent.parent.children:
                _object.ids.media_icon_object.text_color = [190/float(255), 190/float(255), 190/float(255), 1]
                _object.ids.file_name.color = [190/float(255), 190/float(255), 190/float(255), 1]
            print(self.parent.parent.sound_object)
            if self.parent.parent.sound_object:
                print("Stoping music")
                self.stopSound()
                print("se", self.parent.parent.sound_object)
                if self.parent.parent.sound_object == self:
                    self.parent.parent.sound_object = None
                else:
                    print("Second play")
                    self.parent.parent.sound_object = self
                    self.playSound(file_name)
            else:
                print("First play", self)
                self.parent.parent.sound_object = self
                self.playSound(file_name)
class EncryptButtonBox(TouchBox):
    def respondToTouch(self):
        self.md_bg_color = [20/float(255), 20/float(255), 20/float(255), 1]
        file_object = open("dbase.db", "rb")
        data = pickle.load(file_object)
        thread.start_new_thread(self.parent.encryptFile, (self.parent.file_name, data["key"]))
class MediaFileBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MDBoxLayout, self).__init__(**kwargs)
        self.file_type = ""
        self.encrypting = False
        self.file_size = 0
        self.file_name = ""
        self.encrypted_data_size = 0
    def encryptFile(self, filename, key):
        if self.file_size == 0:
            self.file_size = os.path.getsize(filename)
            file_object = open(filename, "rb")
            data = file_object.read()
            file_object.close()
            data = bytearray(data)
            for index, value in enumerate(data):
                data[index] = value ^ key
                self.encrypted_data_size += 1
                self.updateProgress()
            path_list = filename.split("/")
            encrypted_file_object = open("Encypted-" + path_list[-1], "wb")
            encrypted_file_object.write(data)
            encrypted_file_object.close()
    def updateProgress(self):
        percentage = (self.encrypted_data_size/self.file_size) * 100
        percentage = round(percentage, 2)
        self.ids.encrypt_button_label.text = str(percentage) + "℅"
        if percentage == 100:
            self.ids.encrypt_button_label.text = "Done"
class VideoFilesList(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.videos_list = []
        self.padding = ("15dp", "10dp")
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
    def addVideoBar(self):
        for video_file in self.videos_list:
            path_list = video_file.split("/")
            media_file_bar = MediaFileBar()
            media_file_bar.file_name = video_file
            media_file_bar.ids.file_name.text = path_list[-1]
            media_file_bar.file_type = "Video"
            self.add_widget(media_file_bar)
class MusicFilesScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.files = self.parent
class MusicFilesList(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.music_list = []
        self.sound_object = None
        self.padding = ("15dp", "10dp")
        self.size_hint_y = None
        self.bind(minimum_height = self.setter("height"))
    def addVideoBar(self):
        for music_file in self.music_list:
            path_list = music_file.split("/")
            media_file_bar = MediaFileBar()
            media_file_bar.file_name = music_file
            media_file_bar.ids.file_name.text = path_list[-1]
            media_file_bar.file_type = "Music"
            media_file_bar.ids.media_icon_object.icon = "music"
            self.add_widget(media_file_bar)
class ImageTile(FitImage):
    def on_touch_down(self, touch):
        x_size = self.pos[0] + self.size[0]
        y_size = self.pos[1] + self.size[1]
        if ((touch.x > self.pos[0] and touch.x < x_size) and (touch.y > self.pos[1] and touch.y < y_size)):
            print("Image Name", self.source)
            self.parent.parent.root.parent.root.parent.transition = SlideTransition(direction = "left")
            self.parent.parent.root.parent.root.parent.current = "view_media_file_screen"
            objects = self.parent.parent.root.parent.root.parent.children
            #print("#*#*#*#:", objects)
            self.parent.parent.root.parent.root.parent.children[0].ids.current_image.source = self.source
class ImagesFilesScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.files = self.parent
class ImagesFilesList(MDGridLayout):
    def __init__(self, **kwargs):
        super(MDGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.size_hint_y  = None
        self.images_list = []
        self.bind(minimum_height = self.setter("height"))
        self.padding = ("5dp", "10dp")
        self.spacing = "4dp"
    def addVideoBar(self):
        for image_file in self.images_list:
            image_tile = ImageTile()
            image_tile.source = image_file
            self.add_widget(image_tile)