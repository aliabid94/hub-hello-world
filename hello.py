def hello(inp):
  if inp == "fail":
    raise ValueError("whoops") 
  print("yay")
  return inp.replace("hello", "HELLO").replace("Hello", "HELLO")
  
