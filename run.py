from tellonym import Tellonym as Te
import time as tm
from photogen import PhotoGen as Pg
from PIL import ImageFont


'''
    
    Needed variables:
    
    username: str
        your tellonym username
        
    password: str
        your tellonym password
        
    interval: int/float
        how often you want the script to check for new tells (in minutes)
        
    font: freeTypeFont
        the font you want the script to use
    
    rectColor: tuple[R, G, B]
        specifies the color of the rect on which the text is shown
        
    padding: int
        padding of the text inside the rect
        
    fontColor: tuple[R, G, B]
        specifies the color of the font

'''
username = 'username'
password = 'password'
interval = 10
font = ImageFont.truetype("Lato.ttf", 24, encoding='utf-8')
rectColor = (47, 49, 51)
padding = 10
fontColor = (255, 255, 255)


client = Te.Tellonym(username, password)

lastTellID = open('lastID.txt', 'r').read()

tellsToSend = []
IDs = []

while 1:
    tellsToSend = []
    IDs = []
    for x in client.get_tells():
        if str(x.id) == lastTellID:
            break
        tellsToSend.append(x.tell)
        IDs.append(x.id)
        print(x.id)
    try:
        lastTellID = IDs[0]
        open('lastID.txt', 'w').write(str(lastTellID))
    except IndexError:
        print('sraka')
    for x in tellsToSend:
        phot = Pg(['tell', 'image/jpeg', x, font, rectColor, padding, fontColor])
        phot.gen()
    tm.sleep(interval * 60)


