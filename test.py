def divide(a, b):
    result = a/b
    return result

def process(data):
    if data == None:
        return
    for i in range(len(data)):
        print(data[i])
    try:
        result = divide(data[0], data[1])
    except:
        pass

global counter
counter = 0

process([10, 0, 5])