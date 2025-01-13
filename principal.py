from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from first import Window1
from second import Window2


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Window1(name='window1'))
        sm.add_widget(Window2(name='window2'))
        sm.current = 'window1'
        return sm


if __name__ == '__main__':
    MyApp().run()
