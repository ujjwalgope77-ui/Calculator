"""Android calculator built with Python + Kivy.

Test on desktop:  pip install kivy && python main.py
Build APK:        buildozer android debug
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from calculator import CalcError, calculate

KEYS = [
    ["C", "DEL", "(", ")"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

OPERATOR_KEYS = {"÷", "×", "-", "+", "(", ")"}


class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        Window.clearcolor = (0.07, 0.07, 0.09, 1)
        self.expression = ""
        self.ans = 0

        root = BoxLayout(orientation="vertical", padding=12, spacing=12)

        self.display = Label(
            text="0",
            font_size="48sp",
            halign="right",
            valign="middle",
            size_hint_y=0.25,
            color=(1, 1, 1, 1),
        )
        self.display.bind(size=lambda w, s: setattr(w, "text_size", s))
        root.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=8, size_hint_y=0.75)
        for row in KEYS:
            for key in row:
                grid.add_widget(self._make_button(key))
        root.add_widget(grid)
        return root

    def _make_button(self, key):
        if key == "=":
            color = (0.95, 0.55, 0.1, 1)
        elif key in ("C", "DEL"):
            color = (0.8, 0.25, 0.25, 1)
        elif key in OPERATOR_KEYS:
            color = (0.25, 0.3, 0.45, 1)
        else:
            color = (0.18, 0.18, 0.22, 1)
        btn = Button(
            text=key,
            font_size="28sp",
            background_normal="",
            background_color=color,
        )
        btn.bind(on_release=lambda b: self.on_key(b.text))
        return btn

    def on_key(self, key):
        if key == "C":
            self.expression = ""
        elif key == "DEL":
            self.expression = self.expression[:-1]
        elif key == "=":
            self._evaluate()
            return
        else:
            self.expression += key
        self._show(self.expression or "0")

    def _evaluate(self):
        if not self.expression:
            return
        expr = self.expression.replace("×", "*").replace("÷", "/")
        try:
            result = calculate(expr, self.ans)
        except CalcError as exc:
            self.expression = ""
            self._show(f"Error: {exc}", small=True)
            return
        self.ans = result
        self.expression = str(result)
        self._show(self.expression)

    def _show(self, text, small=False):
        self.display.text = text
        self.display.font_size = "24sp" if small or len(text) > 12 else "48sp"


if __name__ == "__main__":
    CalculatorApp().run()
