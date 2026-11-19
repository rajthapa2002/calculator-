from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.08, 1)

class Calculator(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=8
        )

        self.display = TextInput(
            text='',
            font_size=35,
            multiline=False,
            halign='right',
            size_hint=(1, 0.25),
            background_color=(0.12, 0.12, 0.17, 1),
            foreground_color=(0, 1, 0.7, 1)
        )

        layout.add_widget(self.display)

        for row in [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]:
            line = BoxLayout(spacing=8)

            for item in row:
                btn = Button(
                    text=item,
                    font_size=22,
                    background_normal='',
                    background_color=(0.15, 0.18, 0.25, 1)
                )
                btn.bind(on_press=self.click)
                line.add_widget(btn)

            layout.add_widget(line)

        return layout

    def click(self, instance):
        value = instance.text

        if value == 'C':
            self.display.text = ''
        elif value == '=':
            try:
                self.display.text = str(
                    eval(self.display.text)
                )
            except:
                self.display.text = 'Error'
        else:
            self.display.text += value

Calculator().run()
