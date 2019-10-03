import cv2
import numpy as np
import math
import cv2
from darkflow.net.build import TFNet
import time
from control import yAxis,Brake,reCentre,left,right,walk                               #importing control ,this will help to move car

options = {                                                      
    'model': 'cfg/yolov2.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.2,
    'gpu': 1.0
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 540)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            label = result['label']
            if(label=='person'):                                                       
                Brake()
                ptlx = result['topleft']['x'] 
                ptly = result['topleft']['y']
                pbrx = result['bottomright']['x']
                pbry = result['bottomright']['y']
                pcx = int((ptlx + pbrx)/2)                                              # calculating center of person
                pcy = int((ptly + pbry)/2)
                frame = cv2.rectangle(frame, (ptlx, ptly), (pbrx,pbry), color, 1)

            if(label=='cell phone'):
                
                ctlx = result['topleft']['x'] 
                ctly = result['topleft']['y']                      
                cbrx = result['bottomright']['x']				        # calculating center of cellphone 
                cbry = result['bottomright']['y']
                ccx = int((ctlx + cbrx)/2)
                ccy = int((ctly + cbry)/2)
                frame = cv2.rectangle(frame, (ctlx, ctly), (cbrx,cbry), color, 2)       # making rectangle aroung object 
                frame = cv2.line(frame, (pcx,pcy), (ccx, ccy), (0,255,0), 3)            # joning line from center to center of person and object
                if(ccy<pcy):                                                           
                    left()
                    walk()
                    
                if(ccy>pcy):
                    walk()
                    right()
                else:
                    reCentre()
            cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()