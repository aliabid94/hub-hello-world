from hello import hello 
import gradio
import time

print("TESTING")

io = gradio.Interface(fn=hello, inputs='text', outputs='text', verbose=True, title='Hello World', 
    description='Hello World Descriptiooon', thumbnail='https://github.com/gradio-app/gradio_static/blob/master/static/img/logo.png?raw=true', analytics_enabled=False)

for i in range(80):
    print(i)
    time.sleep(0.2)
 
io.launch(debug=True)
