from icecream import ic
import time
import random
import pathlib
import csv
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
# from kivy.core.window import Window
from kivy.core.audio import SoundLoader
# from kivy.uix.layout import Layout
from kivy.uix.dropdown import DropDown
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen
# kivy.require('1.9.0')

path_font_name = 'lsansuni.ttf'


class Window1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        headers = RelativeLayout()
        with headers.canvas.before:
            Color(0.13, 0.13, 0.15, 1)
            self.rect = Rectangle(size=headers.size, pos=headers.pos)
        headers.bind(size=self.update_background, pos=self.update_background)
        grid_layout = GridLayout(cols=4)
        grid_layout.size_hint = (1, .9)
        paths_themes = self.paths_themes_list()
        # file_path = self.path_them()
        file_path = 'data/noun/technology/computer_internet'
        # headers.add_widget(
        #     Button(text='↻', pos_hint={'x': 0, 'top': 1}, size_hint=(.2, .1)))
        headers.add_widget(self.options_themes(paths_themes, file_path))
        # headers.add_widget(Button(text='mode', pos_hint={
        #                    'right': 1, 'top': 1}, size_hint=(.2, .1)))
        with open(file_path+'/words.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                grid_layout.add_widget(self.label_word(line[0]))
                grid_layout.add_widget(
                    self.create_phonetics(line[1], file_path, line[4]))
                grid_layout.add_widget(self.image(file_path, line[8], line[7]))
                grid_layout.add_widget(self.example(line[9]))
        headers.add_widget(grid_layout)
        self.add_widget(headers)

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

    def play_sound(self, path):
        sound = SoundLoader.load(path)
        ic(path)
        if sound:
            sound.play()

    def paths_themes_list(self):
        base_path = pathlib.Path('data')
        files_words_csv = base_path.rglob('words.csv')
        paths = [path.__str__().replace('/words.csv', '')
                 for path in files_words_csv]
        # random_them = random.choice(paths).__str__()
        return paths

    def label_word(self, word):
        word_english = Label(
            text=word, font_name=path_font_name,
            size_hint=(.5, None),
            height=100,
            color=(0, 0, 0, 1)
        )
        with word_english.canvas.before:
            Color(0.52, 0.57, 0.67, 1)
            word_english.rect = Rectangle(
                size=word_english.size, pos=word_english.pos)
        word_english.bind(size=lambda instance, value: setattr(
            word_english.rect, 'size', value))
        word_english.bind(pos=lambda instance, value: setattr(
            word_english.rect, 'pos', value))
        return word_english

    def create_phonetics(self, phonetics, path_sound, word_sound):
        component = Button(
            text=phonetics, font_name=path_font_name,
            size_hint_x=.5,
            background_color=(0.66, 0.72, 0.81, 1),
            background_normal='',
            color=(0, 0, 0, 1)
        )
        component.bind(on_press=lambda instance: self.play_sound(
            path_sound+'/'+word_sound))
        return component

    def image(self, path, path_image_small, path_image_big):
        if path_image_small:
            image_word = Image(
                source=path+'/'+path_image_small,
                pos_hint={'center_x': .5, 'center_y': .5},
                size_hint_x=.5
            )
            # image_word.size_hint_y =1
            return image_word
        if path_image_big:
            image_word = Image(
                source=path+'/'+path_image_big,
                pos_hint={'center_x': .5, 'center_y': .5},
                size_hint_x=.5
            )
            # image_word.size_hint_y =1
            return image_word
        return Label(text='', size_hint_x=.1)

    def example(self, text):
        sentence = Label(
            text=text,
            size_hint_x=1,
            color=(0, 0, 0, 1)
        )
        with sentence.canvas.before:
            Color(0.52, 0.57, 0.67, 1)
            sentence.rect = Rectangle(size=sentence.size, pos=sentence.pos)
        sentence.bind(size=lambda instance, value: setattr(
            sentence.rect, 'size', value))
        sentence.bind(pos=lambda instance, value: setattr(
            sentence.rect, 'pos', value))
        return sentence
