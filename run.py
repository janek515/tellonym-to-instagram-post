#  Copyright (c) 2020. Jan Ochwat.NesTeam

from tellonym import Tellonym as Te
import time as tm
from photogen import PhotoGen as Pg
from PIL import ImageFont


class TellonymPost:

    def __init__(self, creds, interval=10, fontcol=(255, 255, 255), rectcol=(47, 49, 51), padding=10, d=False):
        """
    
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


            :type creds: tuple

        """
        self.username, self.password = creds
        self.interval = interval
        self.font = ImageFont.truetype("Lato.ttf", 36, encoding='utf-8')
        self.rectColor = rectcol
        self.padding = padding
        self.fontColor = fontcol
        self.d = d
        self.client = Te.Tellonym(self.username, self.password, self.d)
        print('Logged in succesfully.')
        self.lastTellID = open('lastID.txt', 'r').read()
        self.tellsToSend = []
        self.IDs = []

    def run(self):
        while 1:
            self.tellsToSend = []
            self.IDs = []
            for x in self.client.get_tells():
                if str(x.id) == self.lastTellID:
                    break
                self.tellsToSend.append(x.tell)
                self.IDs.append(x.id)
                # print(x.id)
            try:
                self.lastTellID = self.IDs[0]
                open('lastID.txt', 'w').write(str(self.lastTellID))
            except IndexError:
                print('No new tells found.')
            print('Generating and Sending ' + str(len(self.tellsToSend)) + ' new tells.')
            for x in self.tellsToSend:
                phot = Pg(['tell', 'image/jpeg', x, self.font, self.rectColor, self.padding, self.fontColor, self.d])
                phot.gen()
            if self.d:
                break
            else:
                tm.sleep(self.interval * 60)
