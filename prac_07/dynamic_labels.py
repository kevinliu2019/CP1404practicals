from kivy.app import App
from kivy.lang import Builder


class DynamicWidgetsApp(App):
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root


DynamicWidgetsApp().run()
