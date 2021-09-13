from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics.texture import Texture

class WindowManager(ScreenManager):
    pass

class ObjectDescribePopup(Widget):
    pass

class ScanWindow(Screen):

    is_scanning_mode = True
    mode_text = StringProperty("Scanning mode")

    def on_click(self):
        print("scan")

    def teach_network(self, texture):
        print(texture)

        show = ObjectDescribePopup()
        is_open = True
        popup_window = Popup(title="What did you photograph?", content=show, size_hint=(None, None), size=(dp(500), dp(300)))

        popup_window.open()

    def change_mode(self):
        self.is_scanning_mode = not self.is_scanning_mode
        if self.is_scanning_mode:
            self.ids.photo_button.source = "images/photo_button.png"
            self.mode_text = "Scanning mode"
        else:
            self.ids.photo_button.source = "images/photo_button2.png"
            self.mode_text = "Teaching mode"

    def animate_it(self, widget, *args):
        self.ids.mode_text.color = (1,1,1,1)
        animate = Animation(
            color=(1,1,1,0),
            duration=2
        )
        animate.start(widget)

class SettingsWindow(Screen):

    texture_to_send = None

    @classmethod
    def load_texture(cls, texture):
        cls.texture_to_send = texture
        print(cls.texture_to_send)



class MyApp(MDApp):
    pass


if __name__ == '__main__':
    MyApp().run()