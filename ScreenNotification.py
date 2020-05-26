# Author: Abdul Campos

import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class ScreenNotification:

    # Display text of size text_size at location x and scrolls across the screen
    def displaySentence(self):
        while self.x > -self.text_size:
            # Draw a black filled box to clear the image.
            self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

            #Draw the text
            self.draw.text((self.x, 0), self.text, font=self.font, fill=255)

            # Display image.
            self.display.image(self.image)
            self.display.show()
            time.sleep(0.01)
            self.x-=10

    #Display the text statically
    def staticText(self):

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        #Draw the text

        self.draw.text((self.x, 0), self.text, font=self.font, fill=255)

        # Display image.
        self.display.image(self.image)
        self.display.show()

    def setText(self, text):
        self.text = text

    #Clear screen with black box
    def clearScreen(self):
        #Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Display image.
        self.display.image(self.image)
        self.display.show()

    #Constructor for the Notification class, takes the text from the constructor
    #and creates the interfaces needed to use the screen
    def __init__(self, text=""):
        # Create the I2C interface.
        self.i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c)

        # Clear display.
        self.display.fill(0)
        self.display.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.display.width
        self.height = self.display.height
        self.image = Image.new("1", (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0

        self.text = text

        # Load default font.
        self.font = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf',28)

        # Alternatively load a TTF font.  Make sure the .ttf font file is in the
        # same directory as the python script!
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        # font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

        # Calculate text size to display image again when it goes off screen
        self.text_size = self.draw.textsize(self.text,self.font)[0]+10
