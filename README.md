# image_processing

- プログラムの概要(Program outline)


  - 内臓Webカメラを使って画像の輝度値の平均値を計算し，プロットする.(Calculate and plot the mean value of the brightness values of the image using the built-in webcam)
  
- プログラムの説明(explaination of the python code)
  - 1～5行目:必要なモジュールをimport　(line 1 to 5 : import module)
  - 10行目：iの値を初期化(line 10:initialize value of i)
  - 12行目:webcameraのインスタンスを作成   (line 12 : Configure VideoCapture class instance for using camera)
  - 17行目：Capture frame-by-frame
  - 18行目：x軸の値がi(line 18:set i as value of x axis)
  - 19行目：y軸の値がwebcameraで読み取る画像の平均値
  - 21行目：グラフをプロットする。(plot graph of x and y)
  - 23行目：webcameraで読み取る画像の平均値を出力する(printout the mean value of the brightness values of the image )
  - 25行目：webcameraで読み取る画像を表示する(Display the image read by webcamera)
  - 26行目：ESCボタンを押したらループから抜けて、プログラム終了(press ESC button to finish the program)
- 使い方(How to use)
  - $ python3.7 image_mean_analysis.py　で実行(compile and execute "image_mean_analysis.py")
  - web cameraが起動し，輝度値を測定する．(The web camera will start and measures the brightness value.)
  - 輝度値はリアルタイムでグラフにプロットされる．(The values will be plotted on the graph in real time.)
  - ESCボタンを押したらプログラム終了(press ESC button to end the program)

- 実行結果(Execution result)
  - GIFによる実行結果
    - ![demo]()

- 参考文献(references)
  - https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
  - https://www.youtube.com/watch?v=GIywmJbGH-8
