from pynput.keyboard import Controller

class PressRelease:
    def __init__(self,key):
        Controller().press(key)
        Controller().release(key)

if __name__ == '__main__':
    PressRelease('/')