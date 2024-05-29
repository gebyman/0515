from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
image = Image.new('RGB', (600, 800), 'white')
draw = ImageDraw.Draw(image)

# Define title and items
title = "湯寶冰 菜單"
items = [
    ("芒果冰湯包", "甜美多汁的芒果，搭配特製冰湯包外皮", "NT$ 120"),
    ("草莓冰湯包", "新鮮香甜的草莓，包裹在冰湯包外皮中", "NT$ 130"),
    ("橙子冰湯包", "清爽酸甜的橙子，融合冰湯包的獨特口感", "NT$ 110"),
    ("綜合水果冰湯包", "精選當季水果，滿足您對多種口味的渴望", "NT$ 150"),
    ("套餐組合", "任選三款冰湯包，享受優惠價", "NT$ 320"),
]

add_ons = [
    ("蜜紅豆", "NT$ 20"),
    ("煉乳", "NT$ 20"),
    ("椰果", "NT$ 20"),
]

drinks = [
    ("蜂蜜檸檬茶", "NT$ 60"),
    ("鮮榨橙汁", "NT$ 70"),
    ("手工冬瓜茶", "NT$ 50"),
]

info = [
    ("地址", "XX市XX區XX路XX號"),
    ("營業時間", "每日 10:00 - 22:00"),
    ("聯絡電話", "0123-456-789"),
]

# Load a font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)

# Draw title
draw.text((200, 20), title, fill='black', font=font)

# Draw items
y = 80
for item in items:
    draw.text((50, y), item[0], fill='black', font=font_small)
    draw.text((50, y + 30), item[1], fill='grey', font=font_small)
    draw.text((500, y + 30), item[2], fill='black', font=font_small)
    y += 70

# Draw add-ons
y += 30
draw.text((50, y), "加料選擇", fill='black', font=font_small)
y += 40
for add_on in add_ons:
    draw.text((50, y), add_on[0], fill='black', font=font_small)
    draw.text((500, y), add_on[1], fill='black', font=font_small)
    y += 30

# Draw drinks
y += 30
draw.text((50, y), "飲品推薦", fill='black', font=font_small)
y += 40
for drink in drinks:
    draw.text((50, y), drink[0], fill='black', font=font_small)
    draw.text((500, y), drink[1], fill='black', font=font_small)
    y += 30

# Draw info
y += 50
for line in info:
    draw.text((50, y), f"{line[0]}: {line[1]}", fill='black', font=font_small)
    y += 30

# Save the image
image_path = "/mnt/data/menu.png"
image.save(image_path)
image.show()

image_path
