def hello(inp):
  if inp == "fail":
    raise ValueError("whoops") 
  return inp.replace("hello", "HELLOO").replace("Hello", "HELLOO")
  
