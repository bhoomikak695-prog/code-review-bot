def test():
    global x
    x = None

    if x == None:
        print("x is none")

    try:
        result = 10 / 0
    except:
        print("error occurred")