from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from first import Window1
from second import Window2
from kivy.core.window import Window
from icecream import ic


class MyApp(App):
    def build(self):
        Window.size = (1366, 768)
        Window.left = 0
        Window.top = 0
        sm = ScreenManager()
        sm.add_widget(Window1(name='window1'))
        sm.add_widget(Window2(name='window2'))
        sm.current = 'window1'
        return sm


if __name__ == '__main__':
    MyApp().run()
