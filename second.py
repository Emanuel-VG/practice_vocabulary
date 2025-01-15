from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from icecream import ic
from kivy.uix.dropdown import DropDown
import pathlib


class Window2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        themes_content = StackLayout(
            orientation='lr-tb', spacing=10, padding=10)
        category = ''
        for path in self.paths_themes_list(type_path='other'):
            if path[:path.find('/')] != category:
                category = path[:path.find('/')]
                themes_content.add_widget(
                    Label(text=category.upper(), font_size=25, size_hint=(.2, .1), bold=True))
            themes_content.add_widget(
                Button(text=path.replace(category+'/', ''), font_size=15, size_hint=(.2, .1)))
        sub_category = ''
        themes_content.add_widget(
            Label(text='NOUN', font_size=25, size_hint=(.2, .1), bold=True))
        for path in self.paths_themes_list():
            if path[:path.find('/')] != sub_category:
                sub_category = path[:path.find('/')]
                themes_content.add_widget(
                    Label(text=sub_category.upper(), font_size=25, size_hint=(.2, .1), bold=True))
            themes_content.add_widget(
                Button(text=path.replace(sub_category+'/', ''), font_size=15, size_hint=(.2, .1)))

            # layout = BoxLayout(orientation='vertical')

            # label = Label(text='Esta es la Pantalla 2')
            # boton = Button(text='Regresar a Pantalla 1')
            # boton.bind(on_press=self.change_window)

            # layout.add_widget(label)
            # layout.add_widget(boton)
            # self.add_widget(layout)
        self.add_widget(themes_content)

    def change_window(self, instance):
        self.manager.current = 'window1'

    def options_themes(self, paths_themes, file_path):
        dropDown = DropDown()
        ic(paths_themes)
        for path in paths_themes:
            btn = Button(text=path, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropDown.select(
                btn.text))
            dropDown.add_widget(btn)
        title_and_options = Button(
            text=file_path.replace('data/', ''),
            size_hint=(.8, .1),
            pos_hint={'left': 0, 'top': 1},
        )
        title_and_options.bind(on_press=dropDown.open)
        dropDown.bind(on_select=lambda instance, x: title_and_options.setter(
            'text')(title_and_options, x))
        return title_and_options

    def paths_themes_list(self, type_path='noun'):
        base_path = pathlib.Path('data')
        files_words_csv = base_path.rglob('words.csv')
        paths = [path.__str__().replace('/words.csv', '').replace('data/', '')
                 for path in files_words_csv]
        if type_path == 'noun':
            noun = [path.replace('noun/', '')
                    for path in paths if path.count('/') == 2]
            return noun
        other = [path for path in paths if path.count('/') == 1]
        return other
