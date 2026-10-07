from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calculator(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.display = TextInput(
            text="",
            readonly=True,
            font_size=32,
            halign="right",
            multiline=False
        )

        layout.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]

        for row in buttons:
            row_layout = BoxLayout(spacing=5)

            for value in row:
                button = Button(
                    text=value,
                    font_size=25
                )
                button.bind(on_press=self.button_pressed)
                row_layout.add_widget(button)

            layout.add_widget(row_layout)

        return layout

    def button_pressed(self, button):
        value = button.text

        if value == "C":
            self.display.text = ""

        elif value == "=":
            try:
                result = eval(self.display.text)
                self.display.text = str(result)
            except:
                self.display.text = "Error"

        else:
            self.display.text += value


if __name__ == "__main__":
    Calculator().run()
