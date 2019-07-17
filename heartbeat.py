import numpy as np
import matplotlib.pyplot as plt
import time

import cv2


fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    x.append(i)    
    y.append(frame.mean())

    ax.plot(x, y, color='b')
    fig.canvas.draw()
    print(frame.mean())
    i += 1
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
