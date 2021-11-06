from kivy.app import App
from kivy.core.text import Label
from kivy.core.window import Window, Animation
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from settings import tile_color_map


class Tile(Button):
    '''
    customised Tile class (inherited from Button) with property value
    when changing value, change text and color at the same time
    '''
    def __init__(self, value=0, **kwargs):
        Label.__init__(self, **kwargs)
        self.font_size = 48
        self.disabled = True
        self.value = value
        self.background_disabled_normal = self.background_normal

    def set_value(self, value):
        '''change the background the color and text when changing the attribute value'''
        self._value = value
        if value == 0:
            self.text = ''
        else:
            self.text = str(value)
        if value in tile_color_map:
            t = 0.1 if value > 0 else 0
            anim = Animation(background_color=tile_color_map.get(value), duration=t)
            anim.start(self)

    def get_value(self):
        return self._value

    value = property(get_value, set_value)


class Menu(Screen):
    '''the menu screen'''

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout(orientation='vertical')
        title = Label(text='2048', font_size=48)
        startButton = Button(text='Start', on_press=self.start_game, font_size=48)
        exitButton = Button(text='Exit', on_press=App.get_running_app().stop, font_size=48)

        self.layout.add_widget(title)
        self.layout.add_widget(startButton)
        self.layout.add_widget(exitButton)
        self.add_widget(self.layout)

    def start_game(self, value):
        '''slide to game screen and start game'''
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

