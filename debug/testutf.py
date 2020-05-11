from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tellonym import Tellonym as Te

username = 'vapewwa'
password = 'cipkadupka12$'

client = Te.Tellonym(username, password)


tellsToSend = []

for x in client.get_tells():
    tellsToSend.append(x.tell)

for x in tellsToSend:
    text = x

baseImg = Image.open('bg.jpg')
draw = ImageDraw.Draw(baseImg)
font = ImageFont.truetype("Roboto.ttf", 24, encoding='utf-8')

draw.multiline_text((0, 0), text, (255, 255, 255), font=font, language='pl')

baseImg.save('twojastara.jpg')