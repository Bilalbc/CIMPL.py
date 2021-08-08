#Bilal Chaudhry 101141634 - 16-03-20 - Test Posterize function

#assumptions:
#Cimpl.py, test_grayscale, T098_P4_posterize all in same file directory 
#image stored in 'images' folder in the same directory as this program 
from Cimpl import set_color, load_image, create_image, get_color, create_color
from test_grayscale import check_equal
from T098_P4_posterize import posterize

FILENAME = "images/miss_sullivan.jpg"
original_image = load_image(FILENAME)



#Author: Bilal Chaudhry 101141634 03/14/2020
def test_posterize() -> None:
    """
    Function used to test the posterize function. creates a 6x1 image and which 
    is used as input into posterize function. new image is comapred to expected
    result and passess test if all pixels are the same. If not, fails test
    
    >>>test_posterize()
    """
    
    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(55, 55, 55))
    set_color(original, 1, 0,  create_color(110, 110, 110))
    set_color(original, 2, 0,  create_color(165, 165, 165))
    set_color(original, 3, 0,  create_color(220, 220, 220))
    
    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(95, 95, 95))
    set_color(expected, 2, 0,  create_color(159, 159, 159))
    set_color(expected, 3, 0,  create_color(223, 223, 223))
    
    posterized = posterize(original)
    
    for x, y, col in posterized:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y)) 
        
test_posterize()
