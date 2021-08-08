#ECOR 1051 - Winter Semester - Milestone 1 - Combined Code
#Program that adjusts the R, G and B values to create a Red, Green and Blue filter
#as well as combines different channels to recreate the original image.

from Cimpl import *

# Assumption: There are images stored in an 'images' folder in the same directory 
# as the program file.

original_img = load_image("images/p2-original.jpg")

image_Red = load_image("images/red_image.png")
image_Green = load_image("images/green_image.png")
image_Blue = load_image("images/blue_image.png")


#-------------------------------------------------------------------------------
#Red Channel Filter - Author: Pietro Alvarez, 10115082
def red_channel(image:Image)->Image:
    '''Returns a new picture with a filter applying a colour of red on every
    pixel in the image, and removing the green and blue components of each pixel
    in the picture.
    
    >>> red_filter(dog)
    # the same picture of a dog will be returned just in the color red
    '''
    
    print("Creating Red Image...")
    new_image = copy(image) 

    for pixel in original_img:
        x, y, (r, g, b) = pixel
        new_colour = create_color( r,0,0) 
        # Mix up the colours ad hoc 
        set_color (new_image, x, y, new_colour)
        
    return new_image

def test_red_filter(new_image: Image):
    ''' Test function for the red filter. Returns TEST PASSED if the channel
    tested has a red filter applied, Returns TEST FAILED if the channel has 
    the red filter applied improperly.
    
    >>> test_red_filter()
    '''

    print("Testing Red Image...")    
    image = copy(new_image)
    wrong = 0
    
    for x,y, (r,g,b) in original_img:
        R, G, B = get_color(image, x, y)
        if G != 0 or B!= 0:
            wrong += 1
            print( 'FAIL : PIXEL @(', x, ',', y, '), g=', G, ', b=', B, '.')
            
    if wrong > 0:
        print("TEST FAILED")
    elif wrong == 0:
        print("TEST PASSED")
        
#-------------------------------------------------------------------------------
#Green Channel Filter - Author: Nathan Chen 101142799
def green_channel(image: Image) -> Image:
    ''' function that takes an image as an input at green scales it by setting r 
    and b color values to zero. Returns the green scaled image
    
    >>>green_channel(original_image)
    '''

    print("Creating Green Image...")    
    new_image = copy(image)
    
    for x, y, (r, g, b) in new_image:
        green = create_color(r-r, g, b-b)
        set_color(new_image, x, y, green)
    return new_image


def test_green_filter(new_image:Image):
    ''' Test function for the green filter.
    
    >>> test_green_filter()
    '''
    
    print("Testing Green Image...")  
    wrong = 0 
    image = copy(new_image)
    
    for x,y, (r,g,b) in image:
        R, G, B = get_color(image, x, y)
        if R != 0 or B!= 0:
            print ( 'FAIL : PIXEL @(', x, ',', y, '), r=', R, ', b=', B, '.')
           
            wrong += 1
  
    if wrong == 0:
        print ("TEST PASSED")
    else:
        print("TEST FAILED")
              
#-------------------------------------------------------------------------------
#Blue Channel Filter - Author: Chris Vernon, 101144282
def blue_channel(image: Image) -> Image:
    """
    returns a given image that contains only the blue shade for each of the 
    pixel's component (ex. the function will return the original "p2-original.jpg"
    image, however this time, it will only contain the blue pixels)
    """

    print("Creating Blue Image...")    
    new_image = copy(image) #def terms "new_image" and "load_image"
    for x, y, (r,g,b) in new_image:
        blue = create_color(r-r, g-g, b) #eliminate the red and green pixels
        set_color(new_image, x,y, blue)
    return new_image


def test_blue_filter(new_image: Image):
    """
    test function for the blue filter, Returns "/test passed"/ if the channel 
    tested has a blue filter applied, and returns test failed if the red filer
    is applied improperly
    """
    
    print("Testing Blue Image...")  
    image = copy(new_image)
   
    wrong = 0
   
    for x, y, (r,g,b) in image:
        R, G, B = get_color(image, x, y)
        if ((R,G,B) != (0,0,B)):
            wrong += 1
            print( 'FAIL : PIXEL @(', x, ',', y, '), g=', G, ', b=', B, ',')
           
    if wrong > 0:
        print("TEST FAILED")
    elif wrong == 0:
        print("TEST PASSED")
        
#-------------------------------------------------------------------------------
#Combine Filter - Author: Bilal Chaudhry 101141634
def combine(fileR:Image, fileG:Image, fileB:Image) -> Image:
    """
    function used to combine the r, g and b values from different images.
    returns the new image.
    
    >>>combine(red_image, green_image, blue_image)
    """
    
    print("Combining Images...")  
    new_image = copy(fileR) 
    
    for x,y,(r,g,b) in new_image:
        r1,new_g,b = get_color(image_Green, x, y)
        r1,g,new_b = get_color(image_Blue, x, y)
        new_color = create_color(r,new_g,new_b)
        set_color(new_image, x,y, new_color)
    
    return new_image

def test_combine(combine_image: Image):
    """
    Function used to test the combined image function.
    compares the rgb value of the combined images to their respective color image
    Test is passed if all of the pixels are the same color, and fails otherwise.
    
    >>>test_combine(red_image, green_image, blue_image)
    """
    
    print("Testing Combine Image...")  
    new_image = copy(combine_image)
    dif = 0
    same = 0
    for x,y, (r,g,b) in new_image:
        
        ex_r, g1, b1 = get_color(image_Red,x,y)
        r1, ex_g, b1 = get_color(image_Green,x,y)
        r1, g1, ex_b = get_color(image_Blue,x,y)
        
        if((ex_r, ex_g, ex_b) != (r,g,b)):
            dif += 1
            print("FAIL: pos",x,",",y, "Expected RGB:",ex_r,ex_g,ex_b,"Actual:",r,g,b)
            
    if (dif == 0):
        print("TEST PASSED")
    else:
        print("TEST FAILED")
        

        
#-------------------------------------------------------------------------------
#Class body to run and test functions 

print("Original Image...")       

print("----------------------------------------")
show(original_img)
#Testing red channel filter
red_image = red_channel(original_img)

show(red_image)                
test_red_filter(red_image)  

print("----------------------------------------")

#Testing green channel filter
green_image = green_channel(original_img)

show(green_image)
test_green_filter(green_image)

print("----------------------------------------")

#Testing blue channel filter
blue_image = blue_channel(original_img)

show(blue_image)
test_blue_filter(blue_image)

print("----------------------------------------")


#Testing Combined Image 
combined_image = combine(red_image,green_image,blue_image)

show(combined_image)
test_combine(combined_image)


        
    
    
    
    
