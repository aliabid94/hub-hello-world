import gradio
import time
import torch

print("TESTING")

def hello(inp):
  if inp == "fail":
    raise ValueError("whoops") 
  elif inp == "gpu":
    return torch.cuda.device_count()
  return inp.replace("hello", "HELLOO").replace("Hello", "HELLOO")

io = gradio.Interface(fn=hello, inputs='text', outputs='text', verbose=True, title='Hello World', 
    description='Hello World Descriptiooon', thumbnail='https://github.com/gradio-app/gradio_static/blob/master/static/img/logo.png?raw=true', analytics_enabled=False)

for i in range(80):
    print(i)
    time.sleep(0.1)

io.launch(debug=True)
