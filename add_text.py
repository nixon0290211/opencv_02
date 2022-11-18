import os
import sys
import cv2

cur_dir = os.path.dirname(sys.argv[0])  # 現在のディレクトリを取得
file_path = os.path.join(cur_dir, 'image/konjikido_01.jpg')

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # 画像の読み込み(path) 階層が違うと読み込めないので注意

cv2.imshow("Image", img)  # 読み込んだ画像を表示

cv2.waitKey(5000) # 1秒待つ

cv2.imwrite(os.path.join(cur_dir, "write.jpg"), img)  # ファイル名 write.jpg で img を保存
