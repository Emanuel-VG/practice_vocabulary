from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Window2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text='Esta es la Pantalla 2')
        boton = Button(text='Regresar a Pantalla 1')
        boton.bind(on_press=self.change_window)

        layout.add_widget(label)
        layout.add_widget(boton)
        self.add_widget(layout)

    def change_window(self, instance):
        self.manager.current = 'window1'
