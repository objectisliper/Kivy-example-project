from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from game_classes import Game
from gui import Menu


class GameApp(App):
    def build(self):
        sm = ScreenManager()
        menu = Menu(name='menu')
        game = Game(name='game')
        sm.add_widget(menu)
        sm.add_widget(game)
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    GameApp().run()
