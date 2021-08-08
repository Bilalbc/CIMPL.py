# T098 P6 Task 2 Submission - Image Filters - 26/03/20

from Cimpl import *


# Red Channel Filter - Author: Pietro Alvarez, 10115082
def red_channel(image: Image) -> Image:
    """Returns a new picture with a filter applying a colour of red on every
    pixel in the image, and removing the green and blue components of each pixel
    in the picture.

    >>> red_channel(img)
    # the same picture of a dog will be returned just in the color red
    """

    print("Creating Red Image...")
    new_image = copy(image)

    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(r, 0, 0)
        set_color(new_image, x, y, new_colour)

    return new_image


# Green Channel Filter - Author: Nathan Chen 101142799
def green_channel(image: Image) -> Image:
    """ function that takes an image as an input at green scales it by setting r
    and b color values to zero. Returns the green scaled image

    >>> green_channel(img)
    """

    print("Creating Green Image...")
    new_image = copy(image)

    for x, y, (r, g, b) in new_image:
        green = create_color(r - r, g, b - b)
        set_color(new_image, x, y, green)
    return new_image


# Blue Channel Filter - Author: Chris Vernon, 101144282
def blue_channel(image: Image) -> Image:
    """
    returns a given image that contains only the blue shade for each of the
    pixel's component (ex. the function will return the original "p2-original.jpg"
    image, however this time, it will only contain the blue pixels)

    >>> blue_channel(img)
    """

    print("Creating Blue Image...")
    new_image = copy(image)  # def terms "new_image" and "load_image"
    for x, y, (r, g, b) in new_image:
        blue = create_color(r - r, g - g, b)  # eliminate the red and green pixels
        set_color(new_image, x, y, blue)
    return new_image


# Combine Filter - Author: Bilal Chaudhry 101141634
def combine(fileR: Image, fileG: Image, fileB: Image) -> Image:
    """
    function used to combine the r, g and b values from different images.
    returns the new image.

    >>> combine(red_image, green_image, blue_image)
    """

    print("Combining Images...")
    new_image = copy(fileR)
    image_Green = copy(fileG)
    image_Blue = copy(fileB)

    for x, y, (r, g, b) in new_image:
        r1, new_g, b = get_color(image_Green, x, y)
        r1, g, new_b = get_color(image_Blue, x, y)
        new_color = create_color(r, new_g, new_b)
        set_color(new_image, x, y, new_color)

    return new_image


# two_tone Filter - Author: Bilal Chaudhry 101141634
def two_tone(image: Image, color_1: str, color_2: str) -> Image:
    """
    function used to convert an image into a new two color tone image. takes two
    strings representing primary and secondary colors to be used in the two-tone
    image.

    >>> two_tone(img, "black", "white")
    """
    r1, g1, b1 = get_RGB(color_1)
    r2, g2, b2 = get_RGB(color_2)

    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        avg = sum((r, g, b)) // 3

        if avg < 128:
            new_color = create_color(r1, g1, b1)
        else:
            new_color = create_color(r2, g2, b2)

        set_color(new_image, x, y, new_color)

    return new_image


# three_tone Filter - Author: Bilal Chaudhry 101141634
def three_tone(image: Image, color_1: str, color_2: str, color_3: str) -> Image:
    """
    function used to convert an image into a new three color tone image. takes
    three strings as input, which represent primary, secondary and tertiary
    colors to be used in the three-tone image.

    >>> three_tone(img, "black", "white", "red")
    """
    r1, g1, b1 = get_RGB(color_1)
    r2, g2, b2 = get_RGB(color_2)
    r3, g3, b3 = get_RGB(color_3)

    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        avg = sum((r, g, b)) // 3
        if avg < 85:
            new_color = create_color(r1, g1, b1)
        elif avg < 170:
            new_color = create_color(r2, g2, b2)
        else:
            new_color = create_color(r3, g3, b3)

        set_color(new_image, x, y, new_color)

    return new_image


# extreme_contrast Filter - Author: Chris Vernon, 101144282
def extreme_contrast(image) -> Image:
    """
    Takes any image and returns that image with a green filter placed over it

    >>> extreme_contrast(img)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in new_image:
        if 0 <= r <= 127:
            pixel1 = 0
        else:
            pixel1 = 255
        if 0 <= g <= 127:
            pixel2 = 0
        else:
            pixel2 = 255
        if 0 <= b <= 127:
            pixel3 = 0
        else:
            pixel3 = 255
        new_colour = create_color(pixel1, pixel2, pixel3)  # create new color
        set_color(new_image, x, y, new_colour)
    return new_image


# Sepia Filter - Author: Nathan Chen 101142799
def sepia(image: Image) -> Image:
    """
    function that takes an image from the user and returns the image with an 
    applied sepia filter functions by first converting image to grayscale and
    then slightly tints each RGB component yellow by a small percentage

    >>> sepia(img)
    """
    new_image = _grayscale(image)

    for x, y, (r, g, b) in new_image:
        if (r, g, b) < (63, 63, 63):
            new_color = create_color(r * 1.1, g, b * 0.9)
        elif (r, g, b) < (191, 191, 191):
            new_color = create_color(r * 1.15, g, b * 0.85)
        elif (r, g, b) >= (191, 191, 191):
            new_color = create_color(r * 1.08, g, b * 0.93)

        set_color(new_image, x, y, new_color)

    return new_image


# posterize Filter - Author: Pietro Alvarez, 10115082
def posterize(image: Image) -> Image:
    """ Returns a Posterized image, after a normal image is used as the argument.

    >>> posterize(image)
    """

    new_image = copy(image)

    for pixel in new_image:
        x, y, (r, g, b) = pixel
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_colour = create_color(r, g, b)
        set_color(new_image, x, y, new_colour)
    return new_image


# detect_edges Filter - Author: Nathan Chen 101142799
def detect_edges(image: Image, threshold: float) -> Image:
    """
    Returns an image that seems like it was drawn with pencil.
    This is done by changing the colour of the pixels by comparing its brightness
    and contrast.

    >>> detect_edges(image, 15)
    """

    image_1 = copy(image)
    H = get_height(image_1) - 1

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, (r, g, b) in image_1:
        if y == H:
            set_color(image_1, x, y, white)
        else:
            brightness1 = (r + g + b) // 3
            r1, b1, g1 = get_color(image_1, x, y + 1)
            brightness2 = (r1 + g1 + b1) // 3
            contrast = abs(brightness1 - brightness2)

            if contrast > threshold:
                set_color(image_1, x, y, black)
            else:
                set_color(image_1, x, y, white)

    return image_1


# detect_images_better Filter - Author: Bilal Chaudhry 101141634
def detect_edges_better(image: Image, thresh: float) -> Image:
    """
    a function used to apply a filter to make an image look like a pencil sketch.
    takes an image and a threshold as parameters and returns filtered image.
    the function compares a pixel to the pixel below and to the right of it. if
    the absolute difference in the average RGB values for either pixel
    comparison is greater than the threshold value, set the original pixel color
    to black. Otherwise, set the color to white

    >>>detect_edges(img, 15)

    """
    new_img = copy(image)

    width = (get_width(new_img) - 1)
    height = (get_height(new_img) - 1)

    BLACK = create_color(0, 0, 0)
    WHITE = create_color(255, 255, 255)

    for x, y, (r, g, b) in new_img:
        if y == height or x == width:
            set_color(new_img, x, y, WHITE)

        else:
            brightness = _avg((r, g, b))
            brightnessx = _avg(get_color(new_img, x + 1, y))
            brightnessy = _avg(get_color(new_img, x, y + 1))

            contrastx = abs(brightness - brightnessx)
            contrasty = abs(brightness - brightnessy)

            if contrastx > thresh or contrasty > thresh:
                set_color(new_img, x, y, BLACK)
            else:
                set_color(new_img, x, y, WHITE)

    return new_img


# flip_vertical Filter - Author: Pietro Alvarez, 10115082
def flip_vertical(image: Image) -> Image:
    """ Returns an image flipped vertically, from an original image inputted in
    for the argument, inside the parameter given.

    >>> flip_vertical(img)
    """
    new_image = copy(image)
    width = get_width(new_image)
    height = get_height(new_image)
    for y in range(height):  # iterates through each row of pixels in the image.
        for x in range(width // 2):
            r, g, b = get_color(image, x, y)
            left_color = create_color(r, g, b)
            (red, green, blue) = get_color(image, (width - 1 - x), y, )
            color_right = create_color(red, green, blue)
            set_color(new_image, (width - 1 - x), y, left_color)
            set_color(new_image, x, y, color_right)
    return new_image


# flip_horizontal Filter - Author: Chris Vernon, 101144282
def flip_horizontal(original_image: Image) -> Image:
    """
    Returns an image flipped horizontally, from an original image chosen by the 
    user, used as a parameter

    >>> flip_horizontal(img)
    """
    new_image = copy(original_image)
    img_width = get_width(new_image)
    img_height = get_height(new_image)
    img_center = img_height // 2

    for x in range(img_width):
        for y in range(img_center):
            r, g, b = get_color(new_image, x, y)
            r2, g2, b2 = get_color(new_image, x, img_height - y - 1)
            set_color(new_image, x, y, create_color(r2, g2, b2))
            set_color(new_image, x, img_height - y - 1, create_color(r, g, b))

    return new_image


def _avg(RGB: tuple) -> float:
    """
    Helper function used to calculate the avg RGB value of a pixel

    >>>_avg((255,255,255))
    255
    """
    r, g, b = RGB
    return (r + g + b) // 3


def _adjust_component(col_value: int) -> int:
    """Returns a value of colour for each component in each pixel in a picture,
    (red, green, blue).

    >>> _adjust_component(250)
    223
    """
    if 0 <= col_value <= 63:
        col_value = 31
    if 63 < col_value <= 127:
        col_value = 95
    if 127 < col_value <= 191:
        col_value = 159
    if 191 < col_value <= 255:
        col_value = 223
    return col_value


def _grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = _grayscale(image)
    >>> show(gray_image)
    """
    image_1 = copy(image)
    for x, y, (r, g, b) in image_1:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(image_1, x, y, gray)
    return image_1


def get_RGB(color: str) -> tuple:
    """
    function designed to return the RGB values of specific colors required for
    the two-tone and three-tone filters

    >>>get_RGB("black")
    (0,0,0)
    """

    if color == "black":
        RGB = (0, 0, 0)
    elif color == "white":
        RGB = (255, 255, 255)
    elif color == "red":
        RGB = (255, 0, 0)
    elif color == "lime":
        RGB = (0, 255, 0)
    elif color == "blue":
        RGB = (0, 0, 255)
    elif color == "yellow":
        RGB = (255, 255, 0)
    elif color == "cyan":
        RGB = (0, 255, 255)
    elif color == "magenta":
        RGB = (255, 0, 255)
    elif color == "gray":
        RGB = (128, 128, 128)

    return RGB
