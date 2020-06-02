from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

KV = '''
<MyButton>:
    on_press:print(self.text)

<RV>:
    viewclass: 'MyButton'
    data:[{'text': str(x)} for x in range(30)]
    RecycleBoxLayout:
        cols:20
        size_hint: None,None
        width:self.minimum_width
        height: self.minimum_height

<SV>:


BoxLayout:
    RV:
    SV:
'''

class MyButton(Button):
    pass

class SV(ScrollView):
    def __init__(self,**kwargs):
        super(SV,self).__init__(**kwargs)
        self.layout = BoxLayout(cols=20,size_hint=(None,None))
        for i in range(1000):
            self.layout.add_widget(MyButton(text = str(i),size_hint=(None,None)))
        self.layout.bind(minimum_height=self.layout.setter('height'),minimum_width=self.layout.setter('width'))
        self.add_widget(self.layout)

class RV(RecycleView):
    pass

class TestApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    TestApp().run()