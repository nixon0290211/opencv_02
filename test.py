from PIL import Image, ImageFont, ImageDraw

image_path = "image/konjikido_01.jpg"
text = "平泉 最高"


def main(text, image_path):
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc"
    font_size = 100  # 文字の大きさ
    font = ImageFont.truetype(font_path, font_size)  # フォントの指定
    font_color = (255, 255, 255)  # 文字の色

    im = Image.open(image_path)
    image = im.resize((800, 300))

    (text_w, text_h), (offset_x, offset_y) = font.font.getsize(text)
    start_X_point = image.size[0] / 2 - text_w / 2
    start_Y_point = image.size[1] / 2 - text_h / 2

    draw = ImageDraw.Draw(image)
    draw.text((start_X_point, start_Y_point), text, fill=font_color, font=font)
    image.save("image/after_image.jpg")
    image.show()  # 読み込んだ画像を表示
    # print(font.font.getsize(text))


if __name__ == "__main__":
    main(text, image_path)
