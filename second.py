from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from icecream import ic
from kivy.uix.dropdown import DropDown
import pathlib
from kivy.graphics import Rectangle, Color


class Window2(Screen):
    path_to_window1 = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path_set = ''
        themes_content = StackLayout(
            orientation='lr-tb', spacing=(5, 10), padding=10)
        with themes_content.canvas.before:
            Color(0.13, 0.13, 0.15, 1)
            self.rect = Rectangle(size=themes_content.size,
                                  pos=themes_content.pos)
        themes_content.bind(size=self.update_background,
                            pos=self.update_background)
        category = ''
        for path in self.paths_themes_list(type_path='other'):
            if path[:path.find('/')] != category:
                category = path[:path.find('/')]
                themes_content.add_widget(self.label_category(category))
            themes_content.add_widget(self.button_them(category, path))
        sub_category = ''
        themes_content.add_widget(self.label_category('NOUN'))
        for path in self.paths_themes_list():
            if path[:path.find('/')] != sub_category:
                sub_category = path[:path.find('/')]
                themes_content.add_widget(self.label_category(sub_category))
            themes_content.add_widget(self.button_them(sub_category, path))
        self.add_widget(themes_content)

    def update_background(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

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

    def label_category(self, title):
        label = Label(
            text=title.upper(),
            font_size=25,
            size_hint=(.2, .1),
            bold=True,
            color=(0, 0, 0, 1),
        )
        with label.canvas.before:
            Color(0.52, 0.57, 0.67, 1)
            label.rect = Rectangle(size=label.size, pos=label.pos)
        label.bind(size=lambda instance, value: setattr(
            label.rect, 'size', value))
        label.bind(pos=lambda instance, value: setattr(
            label.rect, 'pos', value))
        return label

    def button_them(self, category, path):
        button = Button(
            text=path.replace(category+'/', ''),
            font_size=15,
            size_hint=(.2, .1),
            background_color=(0.66, 0.72, 0.81, 1),
            background_normal='',
            color=(0, 0, 0, 1),
        )
        button.bind(on_press=lambda instance: self.two_change(path))
        return button

    def two_change(self, path):
        self.path_set = 'data/'+path
        self.change_window(self)

    def change_window(self, instance):
        window_1 = self.manager.get_screen('window1').path_from_window2(
            self.path_set)
        self.manager.current = 'window1'
