from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from datetime import date
import calendar
from kivy.core.window import Window


kv = Builder.load_string("""
#:import Button kivy.uix.button.Button
#:import Label kivy.uix.label.Label

<SecondPage>:
    
    scroll_type: ['bars', 'content']
    scroll_wheel_distance: dp(114)
    bar_width: dp(3)
    bar_color: .52, .52, .52, 1
    viewclass: 'Button'
    RecycleBoxLayout:
        default_size: None, dp(40)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        padding: 10
        
<Button>
    text_size: self.size     
    halign: 'left'
    valign: 'middle'
    padding_x: 10
    background_color: .52, .52, .52, 1
    color: 1,1,1,1
    on_press: print('pressed')
    
<Label>
    color: 0.87, 0.88, 0.88, 1
    font_size: 20

<DataYear>:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y:None

        Label:
            id: lbl
            text: 'CURRENT YEAR: 2020'
            size_hint_x: 1
            bold: True
            color: .22, .22, .22, 1
        Button:
            id: table_floor
            on_press: root.manager.current = 'page2'
        
            
    RecycleView:

        viewclass: 'Button'
        id: table_floor        
        RecycleBoxLayout:
            default_size: None, dp(40)
            default_size_hint: 1, None
            height: self.minimum_height
            orientation: 'vertical'
            multiselect: True
            touch_multiselect: True
            padding: 10
            

<Label>
    color: 0,0,0,1
    font_size: 35


<Button>
    text_size: self.size
    halign: 'left'
    valign: 'middle'
    padding_x: 10
    background_color: .52, .52, .52, 1
    bold: True
    color: 0.87, 0.88, 0.88, 1
    font_size: 20           
""")


class TestApp(App):

    def build(self):
        return sm

class DataYear(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        year_data = []
        # month adding to button
        for data in [date(2000, i, 1) for i in range(1, 13)]:
            year_data.append({'text': str(data.strftime("%B")).upper()})

            self.ids.table_floor.data = year_data


class SecondPage(RecycleView, Screen):

    def __init__(self, **args):
        super(SecondPage, self).__init__(**args)

        # assigning day of month and day of week to one button
        # week-day str, month-day int
        self.data = [{'text': ' |  ' + str(data.strftime("%A  %d")).upper(), 'id': str(data)}
                      for data in (date(2020, 5, i) for i in range(1, calendar.monthlen(2020, 5) + 1))]

# Create the screen manager
sm = ScreenManager()
sm.add_widget(DataYear(name='page1'))
sm.add_widget(SecondPage(name='page2'))


class SecPage(App):
    def build(self):
        Window.clearcolor = (0.87, 0.88, 0.88, 1)
        return SecondPage()


class MyApp(App):

    def build(self):
        Window.clearcolor = (0.87, 0.88, 0.88, 1)
        return sm


if __name__ == '__main__':
    app = MyApp()
    app.run()

