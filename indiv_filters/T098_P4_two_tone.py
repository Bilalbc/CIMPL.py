#Two-Tone Filter
#Bilal Chaudhry 101141634 - 15/03/2020

#assumptions:
#Cimpl.py stored in same file directory as this program 
#image saved in 'images' folder in same file directory
from Cimpl import *

image = load_image("images/p2-original.jpg")


#Author: Bilal Chaudhry 101141634 03/14/2020
def two_tone(image: Image, color_1:str, color_2:str) -> Image:
    """
    function used to convert an image into a new two color tone image. takes two 
    strings representing primary and secondary colors to be used in the two-tone
    image.
    
    >>>two_tone("images/p2-original.jpg", "black", "white")
    """
    r1,g1,b1 = get_RGB(color_1)
    r2,g2,b2 = get_RGB(color_2)    
    
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        avg = sum((r,g,b))//3
        
        if(avg<128):
            new_color = create_color(r1,g1,b1)
        else:
            new_color = create_color(r2,g2,b2)
    
        set_color(new_image, x, y, new_color)
        
    return new_image
    
    
def get_RGB(color: str) -> tuple:
    """
    function designed to return the RGB values of specific colors required for 
    the two-tone and three-tone filters 
    
    >>>get_RGB("black")
    (0,0,0)
    """
    if color == "black": RGB = (0,0,0)
    elif color == "white": RGB = (255,255,255)
    elif color == "red": RGB =(255,0,0)
    elif color == "lime": RGB = (0,255,0)
    elif color == "blue": RGB = (0,0,255)
    elif color == "yellow": RGB = (255,255,0)
    elif color == "cyan": RGB = (0,255,255)
    elif color == "magenta": RGB = (255, 0, 255)
    elif color == "gray": RGB = (128,128,128)
    
    return RGB
    

show(two_tone(image, "black","white"))