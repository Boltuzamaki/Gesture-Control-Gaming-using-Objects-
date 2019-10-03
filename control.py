from KeyboardInput import W,S,D,A,PressKey,ReleaseKey

def reCentre():
   ReleaseKey(W)
   ReleaseKey(S)
   ReleaseKey(A)
   ReleaseKey(D)

def Brake():
   PressKey(S)
   ReleaseKey(W)
   ReleaseKey(S)
   ReleaseKey(D)
    
def left():
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)

def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)

def walk():
    PressKey(W)
    ReleaseKey(S)

