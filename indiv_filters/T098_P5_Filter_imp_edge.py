#Bilal Chaudhry 101141634 T098 - Milestone P5 detect_images_better filter
#22/03/20

from Cimpl import *

file = choose_file()
original_image = load_image(file)


def detect_images_better(img: Image, thresh: float) -> Image:
    """
    a function used to apply a filter to make an image look like a pencil sketch.
    takes an image and a threshold as paramenters and returns filtered image.
    the function compares a pixel to the pixel below and to the right of it. if 
    the absolute difference in the average RGB values for either pixel 
    comparison is greater than the threshold value, set the priginal pixel color
    to black. Otherwise, set the color to white
    
    >>>detect_edges(image, 15)
    
    """
    new_img = copy(img)
    
    width = (get_width(new_img)-1)
    height = (get_height(new_img)-1)
    
    BLACK = create_color(0,0,0)
    WHITE = create_color(255,255,255)
    
    for x,y,(r,g,b) in new_img:
        if(y == height or x == width):
            set_color(new_img,x,y,WHITE)
        
        else:
            brightness = _avg((r,g,b))
            brightnessx = _avg(get_color(new_img, x+1, y))            
            brightnessy = _avg(get_color(new_img, x, y+1))

            contrastx = abs(brightness - brightnessx)            
            contrasty = abs(brightness - brightnessy)
            
            if(contrastx > thresh or contrasty > thresh):
                set_color(new_img, x, y, BLACK)
            else:
                set_color(new_img, x, y, WHITE)
    
    return new_img
            
                      
def _avg(RGB:tuple) -> float:
    """
    Helper function used to calculate the avg RGB value of a pixel
    
    >>>_avg((255,255,255))
    255
    """
    r,g,b = RGB
    return (r+g+b)//3

