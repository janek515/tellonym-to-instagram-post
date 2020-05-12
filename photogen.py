from PIL import Image
from PIL import ImageDraw
from drive import main
from drive import upload
from text_wrap import text_wrap
import os


class PhotoGen:

    def __init__(self, i):
        self.no = open('no.txt', 'r').read()
        self.name = i[0] + '_' + self.no + '.jpg'
        self.mime = i[1]
        self.font = i[3]
        self.baseImg = Image.open('bg.jpg')
        self.draw = ImageDraw.Draw(self.baseImg)
        self.w, self.h = self.baseImg.size
        self.bgColor = i[4]
        self.fontColor = i[6]
        # You can vary the size of the rect by changing the fraction of blank area over the image size
        self.width, self.height = (0.168, 0.36)
        self.padding = i[5]
        self.rectXY = [(self.width * self.w, self.height * self.h),
                       (self.w - self.width * self.w, self.h - self.height * self.h)]
        self.text = text_wrap(i[2], self.font, (self.w - self.width * self.w) - self.width * self.w - 20)
        print(self.text)
        open('no.txt', 'w').write(str(int(self.no) + 1).zfill(5))

    def gen(self):
        self.draw.rectangle(self.rectXY, self.bgColor)
        self.draw.multiline_text((self.width * self.w + self.padding, self.height * self.h + self.padding), self.text,
                                 self.fontColor, font=self.font)
        self.baseImg.save(self.name, quality=90)
        main()
        upload(self.name, self.mime)
        folderid = open('drive.txt', 'r').read
        if folderid != 'False':
            os.remove(self.name)
