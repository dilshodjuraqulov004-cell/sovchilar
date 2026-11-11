from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class SovchilarApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.94, 0.98, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        title = Label(
            text="SOVCHILAR",
            font_size=30,
            color=(0.44, 0.16, 0.65, 1),
            bold=True
        )

        card = Label(
            text="Xush kelibsiz!",
            font_size=22,
            color=(0.2, 0.2, 0.2, 1)
        )

        button = Button(
            text="Boshlash",
            size_hint=(1, 0.2),
            background_color=(0.44, 0.16, 0.65, 1)
        )

        layout.add_widget(title)
        layout.add_widget(card)
        layout.add_widget(button)

        return layout

SovchilarApp().run()
