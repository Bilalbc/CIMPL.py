#Nathan Chen
#101142799
#Group T098
#Milestone 2 
#sepia filter

from Cimpl import *

file = choose_file()
image = load_image(file)

def detect_edges(image: Image, threshold: float) -> Image: 
    """
    Returns an image 
    
    
    """
    image_1 = copy(image)
    W = get_width(image_1) -1
    H = get_height(image_1) -1
    
    black = create_color(0, 0, 0)
    white = create_color(255,255,255)
    
    for x, y, (r, g, b) in image_1:
        if y == H:
            set_color(image_1, x, y, white)
        
        else: 
            brightness1 = (r + g + b)//3
            r1, b1, g1 = get_color(image_1, x, y+1)
            brightness2 = (r1 + g1 + b1)//3
            contrast = abs (brightness1 - brightness2)
        
            if contrast > threshold:
                set_color(image_1, x, y, black)
                
            else: set_color(image_1, x, y, white)
            
    return image_1

show(detect_edges(image, 15))
        
        
        
        
        
            
            