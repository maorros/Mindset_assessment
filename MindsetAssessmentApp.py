import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget


class MyScreenManager (ScreenManager):
    the_tablet = None

# MyScreenManager:
#    ZeroScreenRoom:
#    FirstScreenRoom:
#    SelectionScreenRoom:
#    SolveTangramRoom:

root_widget = Builder.load_string('''

<ZeroScreenRoom>:
    name: 'fluffy_and_buffy'
    Widget:
        Button:
            id: start_button
            background_color: 1,0,1,1
            background_normal: ''
            text: 'Start'
            font_size: 36
            size: root.width * 0.3, root.height * 0.2
            pos: root.width * 0.5 - self.width * 0.5, root.height * 0.7 - self.height * 0.5
            on_press: app.press_start_button()
<FirstScreenRoom>:
    name: 'first_screen_room'
    Widget:
        FirstScreenBackground:
            size: root.size
            pos: root.pos
        Button:
            id: left_button
            borders: 2, 'solid', (1,1,0,1)
            background_normal: './images/blue.jpg'
            background_down: './images/blue.jpg'
            size: root.width * 0.4, root.height * 0.5
            pos: root.width * 0.5 - self.width, root.height * 0.5 - self.height
            on_press: app.press_left_button()
            opacity: 1
        Button:
            id: right_button
            borders: 2, 'solid', (1,1,0,1)
            background_normal: './images/green.jpg'
            background_down: './images/green.jpg'
            size: root.width * 0.4, root.height * 0.5
            pos: root.width * 0.5 + 0.1*self.width, root.height * 0.5 - self.height
            on_press: app.press_right_button()
            opacity: 1
    FloatLayout:
        id: balloon
        canvas:
            Color:
                rgb: 1, 1, 1
            Ellipse:
                pos: left_button.pos[0]+0.35*left_button.width, left_button.pos[1]+left_button.size[1]
                size: 100 , 101
                source: './images/pink_bkg.png'
                angle_start: 0
                angle_end: 360

<FirstScreenBackground>:
    Image:
        size: root.size
        pos: root.pos
        source: './images/black_bkg.png'
        allow_stretch: True
        keep_ratio: False
''')
#  pos: right_button.pos[0]+0.32*right_button.width, right_button.pos[1]+right_button.size[1]
class MindsetAssessmentApp(App):

    def build(self):
        self.screen_manager = MyScreenManager()
        self.screen_manager.add_widget(FirstScreenRoom())
        return self.screen_manager
        #return Label(text='Hello world')

    def press_right_button(self):
        # child pressed the start button
        right_button = self.screen_manager.current_screen.ids['right_button']
        left_button = self.screen_manager.current_screen.ids['left_button']
        self.screen_manager.current_screen.ids['balloon'].opacity = 0.5
        self.screen_manager.current_screen.ids['balloon'].pos = [right_button.pos[0]+0.32*right_button.width, right_button.pos[1]+right_button.size[1]]
        # self.screen_manager.current_screen.ids['balloon'].pos = [10,10]
        self.screen_manager.canvas.ask_update()
        print [right_button.pos[0]+0.32*right_button.width, right_button.pos[1]+right_button.size[1]]
        print "right"

    def press_left_button(self):
        # child pressed the start button
        right_button = self.screen_manager.current_screen.ids['right_button']
        left_button = self.screen_manager.current_screen.ids['left_button']
        self.screen_manager.current_screen.ids['balloon'].pos = left_button.pos[0] + 0.32 * left_button.width, \
                                                                left_button.pos[1] + left_button.size[1]
        print [left_button.pos[0] + 0.32 * left_button.width, \
                                                                left_button.pos[1] + left_button.size[1]]
        self.screen_manager.current_screen.ids['balloon'].opacity = 1
        self.screen_manager.canvas.ask_update()
        print "left"


class ZeroScreenRoom(Screen):
    pass

class FirstScreenRoom(Screen):
    pass

class FirstScreenBackground(Widget):
    pass

if __name__ == '__main__':
    MindsetAssessmentApp().run()