from hello import hello 
import gradio

io = gradio.Interface(fn=hello, inputs='textbox', outputs='textbox', verbose=True)

io.launch()