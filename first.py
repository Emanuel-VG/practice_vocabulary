from icecream import ic
import csv
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
# from kivy.uix.layout import Layout
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen
# kivy.require('1.9.0')

path_font_name = 'lsansuni.ttf'


class Window1(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ic(self.file_path)
        self.file_path = 'data/noun/technology/computer_internet'
        ic(self.file_path)
        Window.size = (1366, 768)
        Window.left = 0
        Window.top = 0
        headers = RelativeLayout()
        with headers.canvas.before:
            Color(0.13, 0.13, 0.15, 1)
            self.rect = Rectangle(size=headers.size, pos=headers.pos)
        headers.bind(size=self.update_background, pos=self.update_background)
        grid_layout = GridLayout(cols=4, padding=10, spacing=(1, 3))
        grid_layout.size_hint = (1, .9)
        # paths_themes = self.paths_themes_list()
        # file_path = self.path_them()
        # headers.add_widget(
        #     Button(text='↻', pos_hint={'x': 0, 'top': 1}, size_hint=(.2, .1)))
        # headers.add_widget(self.options_themes(paths_themes, file_path))
        title_button = Button(
            text=self.file_path.replace('data/', '').upper(),
            font_size=30,
            size_hint=(.8, .1),
            pos_hint={'left': 0, 'top': 1},
            color=(0.8, 0.8, 0.8, 1),
            bold=True
        )
        title_button.bind(on_press=self.change_window)
        headers.add_widget(title_button)
        # headers.add_widget(Button(text='mode', pos_hint={
        #                    'right': 1, 'top': 1}, size_hint=(.2, .1)))
        with open(self.file_path+'/words.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                grid_layout.add_widget(self.label_word(line[0]))
                grid_layout.add_widget(
                    self.create_phonetics(line[1], self.file_path, line[4]))
                grid_layout.add_widget(self.image(
                    self.file_path, line[8], line[7]))
                grid_layout.add_widget(self.example(line[9]))
        headers.add_widget(grid_layout)
        self.add_widget(headers)

    def update_background(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def change_window(self, instance):
        self.manager.current = 'window2'

    def play_sound(self, path):
        sound = SoundLoader.load(path)
        ic(path)
        if sound:
            sound.play()

    def label_word(self, word):
        word_english = Label(
            text=word,
            size_hint=(.5, None),
            height=100,
            color=(0, 0, 0, 1),
            bold=True,
            font_size=20,
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
            color=(0, 0, 0, 1),
            font_size=20
        )
        component.bind(on_press=lambda instance: self.play_sound(
            path_sound+'/'+word_sound))
        return component

    def image(self, path, path_image_small, path_image_big):
        if path_image_small:
            image_word = Image(
                source=path+'/'+path_image_small,
                pos_hint={'center_x': .5, 'center_y': .5},
                size_hint_x=.3,
            )
        elif path_image_big:
            image_word = Image(
                source=path+'/'+path_image_big,
                pos_hint={'center_x': .5, 'center_y': .5},
                size_hint_x=.3,
            )
        else:
            image_word = Label(text='', size_hint_x=.1)
        with image_word.canvas.before:
            Color(0.52, 0.57, 0.67, 1)
            image_word.rect = Rectangle(
                size=image_word.size, pos=image_word.pos)
        image_word.bind(size=lambda instance, value: setattr(
            image_word.rect, 'size', value))
        image_word.bind(pos=lambda instance, value: setattr(
            image_word.rect, 'pos', value))
        return image_word

    def example(self, text):
        sentence = Label(
            text=text,
            size_hint_x=1,
            color=(0, 0, 0, 1),
            text_size=(550, None),
            font_size=12,
            # halign='center'
        )
        with sentence.canvas.before:
            Color(0.52, 0.57, 0.67, 1)
            sentence.rect = Rectangle(size=sentence.size, pos=sentence.pos)
        sentence.bind(size=lambda instance, value: setattr(
            sentence.rect, 'size', value))
        sentence.bind(pos=lambda instance, value: setattr(
            sentence.rect, 'pos', value))
        return sentence

    def change_window(self, instance):
        self.manager.current = 'window2'

    def path_from_window2(self, text):
        ic(text)
        self.file_path = text
