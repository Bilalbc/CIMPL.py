from Cimpl import *

def _adjust_component( col_value:int)->int:
    if 0 <= col_value <=63:
        col_value = 31
    if 63 < col_value <= 127:
        col_value = 95
    if 127 < col_value <= 191:
        col_value = 159
    if 191 < col_value <= 255:
        col_value = 223
    return col_value
            
def posterize( image:Image)-> Image:
    ''' 
    
    '''
    
    new_image = copy(image)
    
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_colour = create_color(r, g, b)
        set_color (new_image, x, y, new_colour)
    return new_image


FILENAME = "images/miss_sullivan.jpg"
original_image = load_image(FILENAME)

show( original_image )
new_image = posterize(original_image)
show( new_image )
