from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition, SlideTransition
from sub_home_screens import *
from kivy.clock import Clock
import pickle
from kivy.lang import Builder
ui = Builder.load_string("""
<Load>:
    size_hint:None, None
    size:"50dp", "50dp"
    radius:[40, 40, 40, 40]
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
<LoadingScreen>:
    name:"loading_screen"
    MDBoxLayout:
        orientation:"vertical"
        Widget:
        Load:
            pos_hint:{"center_x":.5}
        Widget:
<HomeScreen>:
    id:home_screen
    name:"home_screen"
    MDBoxLayout:
        orientation:"vertical"
        md_bg_color:[0/float(255), 0/float(255), 0/float(255), 1]
        MDBoxLayout:
            size_hint_y:None
            height:"100dp"
            padding:"10dp", "0dp"
            spacing:5
            MDLabel:
                text:"Xenosecure"
                text_size:self.size
                halign:"left"
                font_size:"25dp"
                valign:"middle"
                font_name:"Amsterdam-ZVGqm"
                color:[1, 1, 1, 1]
            MDIconButton:
                id:open_lock_button
                size_hint:None, None
                theme_text_color:"Custom"
                size:"40dp", "40dp"
                icon:"lock-open-minus-outline"
                md_bg_color:[190/float(255), 190/float(255), 190/float(255), 1]
                pos_hint:{"center_x":.5, "center_y":.5}
                on_press:root.goToEncryptedFiles()
        MDBoxLayout:
            id:body
            radius:[30, 30, 0, 0]
            padding:"5dp", "5dp"
            md_bg_color:[25/float(255), 25/float(255), 112/float(255), 1]
            MDBoxLayout:
                ScreenManager:
                    root:home_screen
                    id:home_body_screen_manager_object
                    MDScreen:
                        name:"first_screen"
                        MDBoxLayout:
                            orientation:"vertical"
                            Widget:
                            LoadFilesButtonBox:
                                root:home_screen
                                size_hint:None, None
                                size:"120dp", "40dp"
                                radius:[30, 30, 30, 30]
                                md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
                                pos_hint:{"center_x":.5}
                                MDLabel:
                                    text:"Load files"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:[1, 1, 1, 1]
                            Widget:
                    LoadingScreen:
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
            md_bg_color:[25/float(255), 25/float(255), 112/float(255), 1]
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                radius:[40, 40, 0, 0]
                md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
                MDBoxLayout:
                    MDIconButton:
                        id:video_files_button
                        size_hint:None, None
                        size:"40dp", "40dp"
                        theme_text_color:"Custom"
                        text_color:[220/float(255), 20/float(255), 60/float(255), 1]
                        user_font_size:"30dp"
                        icon:"play-circle"
                        pos_hint:{"center_x":.5, "center_y":.5}
                        on_press:root.goToVideoFiles()
                MDBoxLayout:
                    MDIconButton:
                        id:music_files_button
                        size_hint:None, None
                        size:"40dp", "40dp"
                        theme_text_color:"Custom"
                        user_font_size:"30dp"
                        icon:"music-circle-outline"
                        pos_hint:{"center_x":.5, "center_y":.5}
                        on_press:root.goToMusicFiles()
                MDBoxLayout:
                    MDIconButton:
                        id:images_files_button
                        size_hint:None, None
                        size:"40dp", "40dp"
                        theme_text_color:"Custom"
                        user_font_size:"30dp"
                        icon:"image-outline"
                        pos_hint:{"center_x":.5, "center_y":.5}
                        on_press:root.goToImagesFiles()
                MDBoxLayout:
                    MDIconButton:
                        id:other_files_button
                        size_hint:None, None
                        size:"40dp", "40dp"
                        theme_text_color:"Custom"
                        user_font_size:"30dp"
                        icon:"dots-horizontal"
                        pos_hint:{"center_x":.5, "center_y":.5}
                        on_press:root.goToOtherFiles()
                MDBoxLayout:
                    MDIconButton:
                        size_hint:None, None
                        size:"40dp", "40dp"
                        user_font_size:"30dp"
                        icon:"cog-transfer-outline"
                        pos_hint:{"center_x":.5, "center_y":.5}
                        on_release:root.goToSettings()
""")
class LoadFilesButtonBox(TouchBox):
    def respondToTouch(self):
        self.root.ids.home_body_screen_manager_object.transition = SlideTransition(direction = "left")
        self.root.ids.home_body_screen_manager_object.current = "loading_screen"
        Clock.schedule_once(self.root.checkFiles, 1)
        Clock.schedule_once(self.root.moveToVideosScreen, 3)
        Clock.schedule_once(self.root.moveToMusicScreen, 3)
        Clock.schedule_once(self.root.moveToImagesScreen, 3)
class Load(MDBoxLayout):
    pass
class LoadingScreen(MDScreen):
    pass
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MDScreen, self).__init__(**kwargs)
        self.images_list = []
        self.videos_list = []
        self.music_list = []
        self.loading = True
        #Clock.schedule_once(self.checkFiles, 1)
        #Clock.schedule_once(self.moveToVideosScreen, 3)
    def lookForAudios(self, dirname, filename):
        if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".au"):
            pathname = os.path.join(dirname, filename)
            self.music_list.append(pathname)
    def lookForVideos(self, dirname, filename):
        if filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi"):
            pathname = os.path.join(dirname, filename)
            self.videos_list.append(pathname)
    def lookForImages(self, dirname, filename):
        if filename.endswith(".jpeg") or filename.endswith(".png"):
            pathname = os.path.join(dirname, filename)
            self.images_list.append(pathname)
    def checkFiles(self, seconds):
        for (dirname, dirsher, fileshere) in os.walk("/storage"):
            for filename in fileshere:
                self.lookForAudios(dirname, filename)
                self.lookForVideos(dirname, filename)
                self.lookForImages(dirname, filename)
        self.loading = False
    def moveToMusicScreen(self, seconds):
        if self.loading:
            Clock.schedule_once(self.moveToMusicScreen, 0)
        else:
            music_screen = MusicFilesScreen()
            music_list = MusicFilesList()
            music_list.music_list = self.music_list[:10]
            music_list.addVideoBar()
            music_screen.ids.music_scroll_view.add_widget(music_list)
            self.ids.home_body_screen_manager_object.add_widget(music_screen)
    def moveToImagesScreen(self, seconds):
        if self.loading:
            Clock.schedule_once(self.moveToImagesScreen, 0)
        else:
            images_screen = ImagesFilesScreen()
            images_list = ImagesFilesList()
            images_list.images_list = self.images_list[:10]
            images_list.addVideoBar()
            images_screen.ids.images_scroll_view.add_widget(images_list)
            self.ids.home_body_screen_manager_object.add_widget(images_screen)
    def moveToVideosScreen(self, seconds):
        if self.loading:
            Clock.schedule_once(self.moveToVideosScreen, 0)
        else:
            video_screen = VideoFilesScreen()
            video_list = VideoFilesList()
            video_list.videos_list = self.videos_list[:10]
            video_list.addVideoBar()
            video_screen.ids.video_scroll_view.add_widget(video_list)
            self.ids.home_body_screen_manager_object.add_widget(video_screen)
            self.ids.home_body_screen_manager_object.transition = SlideTransition(direction = "left")
            self.ids.home_body_screen_manager_object.current = "video_files_screen"
    def turnAllIconButtonsBlack(self):
        self.ids.video_files_button.text_color = [0, 0, 0, 1]
        self.ids.music_files_button.text_color = [0, 0, 0, 1]
        self.ids.images_files_button.text_color = [0, 0, 0, 1]
        self.ids.other_files_button.text_color = [0, 0, 0, 1]
        self.ids.video_files_button.icon = "play-circle-outline"
        self.ids.music_files_button.icon = "music-circle-outline"
        self.ids.images_files_button.icon = "image-outline"
    def goToVideoFiles(self):
        if not self.loading:
            self.turnAllIconButtonsBlack()
            self.ids.video_files_button.text_color = [220/float(255), 20/float(255), 60/float(255), 1]
            self.ids.home_body_screen_manager_object.transition = NoTransition()
            self.ids.home_body_screen_manager_object.current = "video_files_screen"
            self.ids.video_files_button.icon = "play-circle"
    def goToMusicFiles(self):
        if not self.loading:
            self.turnAllIconButtonsBlack()
            self.ids.music_files_button.text_color = [220/float(255), 20/float(255), 60/float(255), 1]
            self.ids.home_body_screen_manager_object.transition = NoTransition()
            self.ids.home_body_screen_manager_object.current = "music_files_screen"
            self.ids.music_files_button.icon = "music-circle"
    def goToImagesFiles(self):
        if not self.loading:
            self.turnAllIconButtonsBlack()
            self.ids.images_files_button.text_color = [220/float(255), 20/float(255), 60/float(255), 1]
            self.ids.home_body_screen_manager_object.transition = NoTransition()
            self.ids.home_body_screen_manager_object.current = "images_files_screen"
            self.ids.images_files_button.icon = "image"
    def goToOtherFiles(self):
        if not self.loading:
            self.turnAllIconButtonsBlack()
            self.ids.other_files_button.text_color = [220/float(255), 20/float(255), 60/float(255), 1]
    def goToSettings(self):
        file_object = open("dbase.db", "rb")
        data = pickle.load(file_object)
        if "pin" in data:
            self.parent.ids.settings_screen_object.ids.enter_key_screen.settings_type = "reset"
            self.parent.ids.settings_screen_object.ids.enter_key_screen.ids.settings_type_label.text = "Old Pin"
            print("Status:Reset Pin")
        else:
            self.parent.ids.settings_screen_object.ids.enter_key_screen.settings_type = "set"
            print("Status:Set Pin")
        file_object.close()
        self.parent.transition = SlideTransition(direction = "left")
        self.parent.current = "settings_screen"
    def goToEncryptedFiles(self):
       self.parent.transition = SlideTransition(direction = "left")
       self.parent.current = "encrypted_files_screen"