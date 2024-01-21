import sounddevice as sd
import numpy as np

threshold = 20
clap = False

def clap_detect(indata,frames,time,status):
    global clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm>threshold:
        print("ooga Booga ?")
        clap = True

def listern_claps():
    with sd.InputStream(callback=clap_detect):
        return sd.sleep(1000)



while True:
    listern_claps()
    if clap==True:
        break


    else:
        pass