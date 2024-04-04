def z7_1():
    from PIL import Image
    picture = Image.open("Barm.jpg")
    picture.show()
    print(f"Размер: {picture.size}")
    print(f"Формат: {picture.format}")
    print(f"Цветовая модель: {picture.mode}")

def z7_2():
    from PIL import Image
    picture = Image.open("Barm.jpg")
    picture.show()
    pic_reduced = picture.reduce(3)
    pic_reduced.save("Barm_reduced.jpg")
    pic_reduced.show()
    pic_1 = pic_reduced.transpose(Image.FLIP_LEFT_RIGHT)
    pic_1.show()
    pic_1.save("Barm_mirror.jpg")
    pic_2 = pic_reduced.transpose(Image.FLIP_TOP_BOTTOM)
    pic_2.show()
    pic_2.save("Barm_180.jpg")

def z7_3():
    from PIL import Image, ImageFilter
    pictures = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for i in pictures:
        pic = Image.open(i)
        pic_new = pic.filter(ImageFilter.FIND_EDGES)
        pic_new.show()
        pic_new.save("filters/" + str("1" + i))

def z7_4():
    from PIL import Image, ImageFilter
    picture = Image.open("Barm.jpg")
    wm = Image.open("watermark.png")

    picture.paste(wm, mask=wm)
    picture.show()

def z8_1():
    from PIL import Image
    picture = Image.open("открытка.jpg")
    x1, y1 = 0, 350
    x2, y2 = 1340, 1900
    pic_cropped = picture.crop((x1, y1, x2, y2))
    pic_cropped.show()
    pic_cropped.save("открытка_обрез.jpg")

def z8_2():
    from PIL import Image
    cards = {
        "день рождения": "открытка.jpg",
        "новый год": "нг.jpg",
        "8 марта": "8марта.jpg",
        "23 февраля": "23.jpg"
    }
    a = input("К какому празднику Вам нужна открытка?: ")
    if a.lower() in cards:
        card_name = cards[a.lower()]
        card_im = Image.open(card_name)
        card_im.show()
    else:
        print("Не найдено открытки к данному празднику")

def z8_3():
    from PIL import Image, ImageDraw, ImageFont
    import random
    cards = {
        "день рождения": "открытка.jpg",
        "новый год": "нг.jpg",
        "8 марта": "8марта.jpg",
        "23 февраля": "23.jpg"
    }
    a = input("К какому празднику Вам нужна открытка?: ")
    if a.lower() in cards:
        card_name = cards[a.lower()]
        card_im = Image.open(card_name)
    else:
        print("Не найдено открытки к данному празднику")
    w, h = card_im.size
    name = input("Кого вы хотите поздравить?: ")
    b = random.randint(0, 256)
    c = random.randint(0, 256)
    d = random.randint(0, 256)
    y = [0, 1800]
    y1 = random.choice(y)
    v = ["arial.ttf", "ariblk.ttf"]
    v1 = random.choice(v)
    font = ImageFont.truetype(f"{v1}", 80)
    txt = ImageDraw.Draw(card_im)
    name_text = f"{name}, поздравляю!"
    _, _, w1, h1 = txt.textbbox((0, y1), name_text, font=font)
    txt.text(((w - w1)/2, y1), name_text, (b, c, d), font=font)
    card_im.show()
    card_im.save("card1.png")

z8_3()

