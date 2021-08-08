#Bilal Chauhdry 101141634 T098 - Test function for detect_edges function 
#22/03/20

from Cimpl import choose_file, create_color, create_image, get_color,\
                  set_color, Image
from test_grayscale import check_equal
from T098_P5_filter_edge import detect_edges

def test_detect_edges() -> None:
    """
    function designed to test the detect_edge filter. Creates temporary 1x3 
    original and expected images. processes the original image through the filter
    and compares the values with hard coded expected value to determine the 
    accuracy of the function
    
    >>>test_detect_edges()
    """
    
    original = create_image(1, 3)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(10, 10, 10))
    set_color(original, 0, 2,  create_color(100, 100, 100))
    
    expected = create_image(1, 3)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 0, 1,  create_color(0, 0, 0))
    set_color(expected, 0, 2,  create_color(255, 255, 255))
    
    edge = detect_edges(original,15)
    
    for x, y, col in edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y)) 
    
    
test_detect_edges()
    
    