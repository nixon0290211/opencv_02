import os
import sys
import cv2
from PIL import


cur_dir = os.path.dirname(sys.argv[0])  # 現在のディレクトリを取得
file_path = os.path.join(cur_dir, "image/konjikido_01.jpg")

img = cv2.imread(file_path)  # 画像の読み込み(path) 階層が違うと読み込めないので注意

# テキストを追加
cv2.putText(
    img,
    text="平泉　最高",  # 表示したい文字(日本語は別途フォントの用意が必要)
    org=(100, 250),  # テキストの左下の座標
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,  # フォント
    fontScale=8,  # フォントサイズ
    color=(255, 255, 0),  # 色のタプル(R, G, B)
    thickness=5,
)


cv2.imshow("Image", img)  # 読み込んだ画像を表示

cv2.waitKey(3000)  # 1秒待つ
