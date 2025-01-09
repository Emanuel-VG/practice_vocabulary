from icecream import ic
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
from kivy.core.window import Window
# from pyglet import canvas
# kivy.require('1.9.0')

path_font_name = 'lsansuni.ttf'


class NestedGridLayoutApp(App):
    def build(self):
        Window.fullscreen = True
        headers = RelativeLayout()
        headers.add_widget(
            Button(text='↻', pos_hint={'x': 0, 'top': 1}, size_hint=(.2, .2)))
        headers.add_widget(Label(text='TITLE', pos_hint={
                           'center_x': .5, 'top': 1}, size_hint=(.2, .2)))
        headers.add_widget(Button(text='mode', pos_hint={
                           'right': 1, 'top': 1}, size_hint=(.2, .2)))
        # GridLayout principal
        # main_layout = GridLayout(rows=2)

        # Sub GridLayout 1
        high, width = Window.size
        ic(high)
        ic(width)
        grid_layout = GridLayout(cols=4)
        base_path = pathlib.Path('data')
        folders = [folder for folder in base_path.iterdir()]
        category = random.choice(folders)
        if category.name != 'noun':
            path_category = pathlib.Path(category.__str__())
            category_types = [item for item in path_category.iterdir()]
            path_file = random.choice(category_types).__str__()+'/words.csv'
            ic(path_file.replace('data/', ''))
            with open(path_file, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    ic(line[0])
                    ic(line[1])
                    grid_layout.add_widget(
                        Label(text=line[0], font_name=path_font_name))
                    grid_layout.add_widget(
                        Button(text=line[1], font_name=path_font_name))
                    grid_layout.add_widget(Image(source=line[8], size_hint=(
                        1, .5), pos_hint={'center_x': .5, 'center_y': .5}))
                    grid_layout.add_widget(Label(text=line[1]))
        headers.add_widget(grid_layout)
        # Add sub_gridlayout to main_gridlayout
        # main_layout.add_widget(sub_layout2)

        return headers


if __name__ == "__main__":
    NestedGridLayoutApp().run()
