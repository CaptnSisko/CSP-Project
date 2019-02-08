# Photo Editor
# Written by Trevor and CJ

import os,PIL
from PIL import ImageEnhance, ImageOps, Image

directory = os.getcwd()

image_list = [] # Initialize aggregaotrs
file_list = []

directory_list = os.listdir(directory) # Get list of files
for entry in directory_list:
    absolute_filename = os.path.join(directory, entry)
    try:
        image = PIL.Image.open(absolute_filename)
        file_list += [entry]
        image_list += [image]
    except IOError:
        pass # do nothing with errors tying to open non-images

def save(image): # Function to save the image with an inputted file name
    name = raw_input('What would you like to name the new file? ') + '.png'
    new_directory = os.path.join(os.getcwd(), 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  

    new_image_filename = os.path.join(new_directory, name)
    image.save(new_image_filename)
    
def brighten(image): # function to brighten images with an inputted brightness coefficient
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(float(input('What factor would you like to multiply the brightness by? ')))

def invert(image): # Inverts the inputted image
    return ImageOps.invert(image)

def resize(image): # Resizes the inputted image
    width = int(input('How many pixels wide? '))
    height = int(input('How many pixels tall? '))
    return image.resize((width, height), Image.ANTIALIAS)

def paste(image): # Pastes a different inputted image on the inputted image
    for f in file_list: print str(file_list.index(f) + 1) + ') ' + f
    second_image = resize(image_list[int(input('Choose photo to paste by id: '))-1])
    x = int(input('What\'s the x location of the top left corner of the image you want to paste? '))
    y = int(input('What\'s the y location of the top left corner of the image you want to paste? '))
    image.paste(second_image, box=(x, y))
    return image

def blend(image): # Blends two images
    for f in file_list: print str(file_list.index(f) + 1) + ') ' + f
    second_image = image_list[int(input('Choose photo to paste by id: '))-1]
    image = image.convert('RGBA')
    second_image = second_image.convert('RGBA').resize(image.size, Image.ANTIALIAS)
    return Image.blend(image, second_image, alpha=0.5)

while 'y' in raw_input('Would you like to edit an image? '): # Main loop
    for f in file_list: print str(file_list.index(f) + 1) + ') ' + f  # list files
    image = image_list[int(input('Choose photo to edit by id: '))-1]
    while 'y' in raw_input('Would you like to perform an operation on the image? '): # Operation loop allows you to run as many operations as you want
        print '1) Brighten'
        print '2) Invert'
        print '3) Resize'
        print '4) Paste'
        print '5) Blend'
        selection = int(input('Selection: '))
        if selection == 1: image = brighten(image)
        elif selection == 2: image = invert(image)
        elif selection == 3: image = resize(image)
        elif selection == 4: image = paste(image)
        elif selection == 5: image = blend(image)
        else: print 'Invalid selection!'
    save(image) # saves the image
        