def colorize (text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    try: 
        if not isinstance (text, str):
            raise TypeError ("Text must be instance for it")
        if color  not in colors:
            raise ValueError ("Color not in the tuple")
    except Exception as err:
        print(err)
    else:
        print("Evrything ok")
colorize (1,"blue")
colorize('red', 'green')
colorize("hello", 'red')

