import os
import sys
# from typing import ContextManager, get_type_hints
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
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

Window.size = (1000, 700)
Builder.load_string("""

<Login>:
    ben: benName.text
    pw: passwort.text
    knopf: btn

    GridLayout:
        cols: 1
        size: root.width, root.height
        GridLayout:
            cols: 2
            Label:
                text: "Benutzername"
                font_size: 30
            TextInput:
                id: benName
                multiline: False
                font_size: 30
            Label:
                text: "Passwort"
                font_size: 30
            TextInput:
                password: True
                id: passwort
                multiline: False
                font_size: 30
        Button:
            text: "anmelden"
            id: btn
            size_hint: (1., 0.5)
            font_size: 30
            on_release:
                root.loginPopup()
                root.manager.current = "geheim" if passwort.text == "1234" and benName.text == "Python" else "login"
                root.manager.transition.direction = "left"

<geheimerBereich>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "geheimer Bereich"
            font_size: 30
        Button:
            text: "zurück"
            font_size: 30
            on_release:
                root.manager.current = "login"
                root.manager.transition.direction = "right"
""")


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
ms.add_widget(Login(name="login"))
ms.add_widget(geheimerBereich(name="geheim"))

class StartApp(App):
    def __get_input(self):
        input = GetInput(__file__)
        for key in dir(input):
            if key.startswith("__"):
                continue
            value = getattr(input, key)
            setattr(self, key, value)

    def build(self):
       self.__get_input()
       return ms


if __name__ == "__main__":
    StartApp().run()
