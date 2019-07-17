import numpy as np
import matplotlib.pyplot as plt
import time
import cv2	#必要なモジュールをimport

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0     #iの値を初期化
x, y = [], [] #グラフx軸とy軸を用意する
cap = cv2.VideoCapture(0)   #webcameraのインスタンスを作成


while(True):
    
    ret, frame = cap.read()  # Capture frame-by-frame
    x.append(i)     #x軸の値がi
    y.append(frame.mean())  #y軸の値がwebcameraで読み取る画像の平均値

    ax.plot(x, y, color='b') #グラフをプロットする。
    fig.canvas.draw()
    print(frame.mean())    #webcameraで読み取る画像の平均値を出力する
    i += 1
    cv2.imshow('frame',frame)  #webcameraで読み取る画像を表示する
    if cv2.waitKey(1) == 27:  #ESCボタンを押したらループから抜けて、プログラム終了
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
