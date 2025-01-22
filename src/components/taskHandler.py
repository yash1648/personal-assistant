import pyjokes

def joke():
    funny=pyjokes.get_joke()
    print(funny)
    return funny

