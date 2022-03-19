from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import BaseButton
from kivy.lang import Builder
ui = Builder.load_string("""
<FillRoundFlatButton>:
    text:""
    color:[0, 0, 0, 1]
    press:None
    md_bg_color:[0, 191/float(255), 255/float(255), 1]
    id:button_box_object
    size_hint_y:None
    height:"40dp"
    radius:[self.height -30, self.height - 30, self.height - 30, self.height - 30]
    MDLabel:
        text:button_box_object.text
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:button_box_object.color
<FillRoundFlatIconButton>:
    text:""
    icon:""
    press:None
    color:[0, 0, 0, 1]
    icon_color:[1, 1, 1, 1]
    md_bg_color:[0, 191/float(255), 255/float(255), 1]
    id:button_box_object
    size_hint_y:None
    height:"40dp"
    radius:[self.height -30, self.height - 30, self.height - 30, self.height - 30]
    MDIconButton:
        theme_text_color:"Custom"
        text_color:button_box_object.icon_color
        icon:button_box_object.icon
        size_hint:None, None
        size:"40dp", "40dp"
        pos_hint:{"center_y":.5}
    MDLabel:
        text:button_box_object.text
        text_size:self.size
        halign:"center"
        valign:"middle"
        color:button_box_object.color
    BoxLayout:
        size_hint:None, None
        size:"40dp", "40dp"
""")
class TouchBox(MDBoxLayout):
	def on_touch_down(self, touch):
		print(",::,46!6!,9,:%-@,-@-9,'889999799799998")
		if ((touch.x > self.pos[0] and touch.x < self.size[0]) and (touch.y > self.pos[1] and touch.y < self.size[1])):
			print("Touch Touch")
			self.respondToTouch()
	def respondToTouch(self):
		pass
class FillRoundFlatButton(TouchBox):
    pass
class FillRoundFlatIconButton(TouchBox):
    pass