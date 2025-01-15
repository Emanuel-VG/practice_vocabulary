from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        # Creamos un GridLayout que se usará dentro del ScrollView
        grid = GridLayout(cols=1, size_hint_y=None, spacing=10)
        # Ajusta el tamaño del GridLayout al contenido
        grid.bind(minimum_height=grid.setter('height'))

        # Añadimos varios Labels al GridLayout
        for i in range(50):
            label = Label(
                text=f"Label {i + 1}",
                size_hint_y=None,  # Necesario para que el ScrollView funcione
                height=40          # Altura fija para cada Label
            )
            grid.add_widget(label)

        # Creamos el ScrollView y añadimos el GridLayout
        scroll_view = ScrollView(size_hint=(1, 1), bar_width=10)
        scroll_view.add_widget(grid)

        # Envolvemos el ScrollView en un BoxLayout (opcional, para personalizar más)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(scroll_view)

        return layout


if __name__ == '__main__':
    MyApp().run()
