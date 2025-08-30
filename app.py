from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import cod

mod = 0

class TestApp(App):
    def build(self):
        biglay = GridLayout(cols=1, rows=4)
        smalay = GridLayout(cols=2, rows=1)

        intxt = TextInput(text='Input text', size_hint_y=3)
        inkey = TextInput(text='Input key', multiline=False)
        outxt = TextInput(text='Output', readonly=True, size_hint_y=3)

        proc=Button(text='proceed')
        def process(instance): outxt.text = cod.run(intxt.text, inkey.text, mod)
        proc.bind(on_press=process)
        smalay.add_widget(proc)

        modsw = Button(text='mode=crypt')
        def modeswap(instance):
            global mod
            if mod: 
                mod=0
                modsw.text = 'mode=crypt'
            else:
                mod=1
                modsw.text = 'mode=decrypt'
        modsw.bind(on_press=modeswap)
        smalay.add_widget(modsw)
        biglay.add_widget(smalay)

        biglay.add_widget(intxt)
        biglay.add_widget(inkey)
        biglay.add_widget(outxt)
        return biglay
TestApp().run()