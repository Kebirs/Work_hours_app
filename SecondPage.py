from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from datetime import date
import calendar
from kivy.core.window import Window


kv = Builder.load_string("""
#:import Button kivy.uix.button.Button

<SecondPage>:
    
    scroll_type: ['content']
    scroll_wheel_distance: dp(70)
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
<Label>

    color: 0.87, 0.88, 0.88, 1
    font_size: 20
    
            
""")


class SecondPage(RecycleView):

    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)

        # assigning day of month and day of week to one button
        # week-day str, month-day int
        self.data = [{'text': ' |  ' + str(data.strftime("%A  %d")).upper(), 'id': str(data)}
                      for data in (date(2020, 5, i) for i in range(1, calendar.monthlen(2020, 5) + 1))]


class SecPage(App):
    def build(self):
        Window.clearcolor = (0.87, 0.88, 0.88, 1)  # kolor tła
        return SecondPage()


app2 = SecPage()
app2.run()
