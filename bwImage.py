from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageOps,ImageEnhance
from os import path

Tk().withdraw() ##Only need the file select below
filename=askopenfilename(title="Select the image")  ##gets the path to the image
splitPathToWrite=path.split(filename)
pathToWrite=path.join(splitPathToWrite[0],(f"BNW{splitPathToWrite[1]}"))    ##Sets the name of the saved image
try:
    img=Image.open(filename)    ##Opens the image file
    enhancer=ImageEnhance.Contrast(img)
    img=enhancer.enhance(2)
    bwfilter=ImageEnhance.Color(img)
    img=bwfilter.enhance(0)
    img=ImageOps.posterize(img,1)
    brightness=ImageEnhance.Brightness(img)
    img=brightness.enhance(2)
    img.save(pathToWrite)
    img.show()
except:
    input(f"Something went wrong with converting {filename}, sorry!\nPress any key to exit...")
