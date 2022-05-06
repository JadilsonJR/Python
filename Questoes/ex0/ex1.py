
def say_hello(name):
    # You can print to STDOUT for debugging like you normally would:
    
    if name:
       resp= "Hello, "+ name+"!"
    else:
       resp="Hello there!"
    return  str(resp)