import kivy
import self as self
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
import speech_recognition as sr
import sys
sys.setrecursionlimit(100000)
kivy.require("1.11.1")
def recongnition():
    text = ""
    r = sr.Recognizer()
    print("Speak Anything :")

    while text == "":

        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")
    return text

class ConnectPage(GridLayout):

    def __init__(self, **kwargs):
     super().__init__(**kwargs)
     self.cols = 2




     self.add_widget(Label(text="NAME: "))

     self.name = recongnition()
     self.add_widget(Label(text = self.name))

     self.add_widget(Label(text="WHERE ARE YOU FROM: "))

     self.where = recongnition()
     self.add_widget(Label(text=self.where))

     self.add_widget(Label(text="PURPOSE OF VISIT: "))

     self.purpose = recongnition()
     self.add_widget(Label(text = self.purpose))

     self.add_widget(Label(text="WHOM DO YOU WANT TO MEET: "))

     self.who = recongnition()
     self.add_widget(Label(text=self.who))

     self.add_widget(Label(text ="ADRESS: "))

     self.adress = recongnition()
     self.add_widget(Label(text = self.adress))

     self.join = Button(text="CONFIRM OR SPEAK AGAIN")
     self.join.bind(on_press=self.confirm_button)
     self.add_widget(Label())
     self.add_widget(self.join)

    def confirm_button(self, instance):
        self.join = Button(text="CONFIRM")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

        self.join = Button(text="SPEAK AGAIN")
        self.join.bind(on_press=self.QUIT_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def QUIT_button(self,instance):
        self.clear_widgets()
        chat_app = EpicApp()
        chat_app.run()


    def join_button(self, instance):
        name = self.name
        purpose = self.purpose
        adress = self.adress
        where = self.where
        who = self.who
        with open("prev_details.txt", "a") as f:
            f.write(f"{name},{where},{purpose},{who},{adress}\n")

        info = f" {name}\n\n\n{where}\n\n\n{purpose}\n\n\n{who}\n\n\n{adress}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.cols = 1

        # And one label with bigger font and centered text
        self.message = Label(halign="center", valign="middle", font_size=30)


        self.message.bind(width=self.update_text_width)


        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message


    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class EpicApp(App):
    def build(self):


        self.screen_manager = ScreenManager()


        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)


        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()