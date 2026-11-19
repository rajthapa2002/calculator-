from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class Calculator(App):

    def build(self):
        Window.clearcolor = (0.08, 0.08, 0.08, 1)

        main = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        self.display = TextInput(
            text='',
            font_size=35,
            readonly=True,
            halign='right',
            size_hint=(1, 0.25),
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1)
        )

        main.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=7
        )

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '⌫', '0', '=',
            '%', '.', '+', 
        ]

        for value in buttons:
            btn = Button(
                text=value,
                font_size=25,
                background_color=(0.25, 0.25, 0.25, 1)
            )
            btn.bind(on_press=self.click)
            grid.add_widget(btn)

        main.add_widget(grid)
        return main

    def click(self, instance):
        value = instance.text

        if value == 'C':
            self.display.text = ''

        elif value == '⌫':
            self.display.text = self.display.text[:-1]

        elif value == '=':
            try:
                expression = self.display.text
                allowed = '0123456789+-*/%.() '

                if not all(c in allowed for c in expression):
                    raise ValueError()

                result = eval(expression, {"__builtins__": {}})
                self.display.text = str(result)

            except:
                self.display.text = 'Error'

        else:
            self.display.text += value


Calculator().run()