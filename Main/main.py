import os
import sys

from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput
# from Source.Services.my_math_methods import MyMethods

Window.size = (1000, 1000)
Builder.load_file("start.kv")


class Games(Screen):
    btn1 = ObjectProperty()
    btn2 = ObjectProperty()
    btn3 = ObjectProperty()


class Andor1(Screen):
    btn_1 = ObjectProperty()
    btn_2 = ObjectProperty()
    btn_3 = ObjectProperty()
    btn_4 = ObjectProperty()
    btn_5 = ObjectProperty()
    btn_6 = ObjectProperty()


class Andor2(Screen):
    btn2_1 = ObjectProperty()
    btn2_2 = ObjectProperty()
    btn2_3 = ObjectProperty()
    btn2_4 = ObjectProperty()
    btn2_5 = ObjectProperty()
    btn2_6 = ObjectProperty()


class Andor3(Screen):
    btn3_1 = ObjectProperty()
    btn3_2 = ObjectProperty()
    btn3_3 = ObjectProperty()
    btn3_4 = ObjectProperty()
    btn3_5 = ObjectProperty()
    btn3_6 = ObjectProperty()


class Bonus(Screen):
    btn4_1 = ObjectProperty()
    btn4_2 = ObjectProperty()
    btn4_3 = ObjectProperty()
    btn4_4 = ObjectProperty()
    btn4_5 = ObjectProperty()
    btn4_6 = ObjectProperty()


class Login(Screen):
    ben = StringProperty()
    pw = StringProperty()
    knopf = ObjectProperty()

    def loginPopup(self):
        if self.ben == "" or self.pw == "":
            popup = Popup(title="Fehler",
            content = Label(text="Es wurde kein Passwort oder Benutzername eingegeben!"),
            size_hint=(None, None), size=(400, 400))
            popup.open()
        else:
            if self.ben == "Python" and self.pw == "1234":
                self.knopf.background_color = [0., 1., 0., 1.]
            else:
                self.knopf.background_color = [1., 0., 0., 1.]


class geheimerBereich(Screen):
    pass


ms = ScreenManager()
ms.add_widget(Games(name="games"))
ms.add_widget(Andor1(name="andor1"))
ms.add_widget(Andor2(name="andor2"))
ms.add_widget(Andor3(name="andor3"))
ms.add_widget(Bonus(name="bonus"))
ms.add_widget(Login(name="login"))
ms.add_widget(geheimerBereich(name="geheim"))


class StartApp(GetInput, App):
    def __init__(self):
        super().__init__(__file__)

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        print(self.A1)
        return ms


StartApp().run()
