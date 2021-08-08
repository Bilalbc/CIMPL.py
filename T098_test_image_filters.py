# T098 P6 Task 2 Submission - Test Image Filters - 26/03/20


from T098_image_filters import *
from test_grayscale import check_equal

img = load_image(choose_file())

original_img = load_image("images/p2-original.jpg")

image_Red = load_image("images/red_image.png")
image_Green = load_image("images/green_image.png")
image_Blue = load_image("images/blue_image.png")


# Red Channel test Filter - Author: Pietro Alvarez, 10115082
def test_red_filter() -> None:
    """ Test function for the red filter. Returns TEST PASSED if the channel
    tested has a red filter applied, Returns TEST FAILED if the channel has
    the red filter applied improperly.

    >>> test_red_filter(img)

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    """

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(55, 55, 55))
    set_color(original, 1, 0, create_color(110, 110, 110))
    set_color(original, 2, 0, create_color(165, 165, 165))
    set_color(original, 3, 0, create_color(0, 0, 0))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(55, 0, 0))
    set_color(expected, 1, 0, create_color(110, 0, 0))
    set_color(expected, 2, 0, create_color(165, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    red_image = red_channel(original)

    for x, y, col in red_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(red_image, x, y))


# Green Channel test Filter - Author: Nathan Chen 101142799
def test_green_filter() -> None:
    """ Test function for the green filter.

    >>> test_green_filter(img)

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    """

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(55, 55, 55))
    set_color(original, 1, 0, create_color(110, 110, 110))
    set_color(original, 2, 0, create_color(165, 165, 165))
    set_color(original, 3, 0, create_color(0, 0, 0))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 55, 0))
    set_color(expected, 1, 0, create_color(0, 110, 0))
    set_color(expected, 2, 0, create_color(0, 165, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    green_image = red_channel(original)

    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(green_image, x, y))


# Blue Channel test Filter - Author: Chris Vernon, 101144282
def test_blue_filter() -> None:
    """
    test function for the blue filter, Returns "/test passed"/ if the channel
    tested has a blue filter applied, and returns test failed if the red filer
    is applied improperly

    >>> test_blue_filter(img)

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------

    """

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(55, 55, 55))
    set_color(original, 1, 0, create_color(110, 110, 110))
    set_color(original, 2, 0, create_color(165, 165, 165))
    set_color(original, 3, 0, create_color(0, 0, 0))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 0, 55))
    set_color(expected, 1, 0, create_color(0, 0, 110))
    set_color(expected, 2, 0, create_color(0, 0, 165))
    set_color(expected, 3, 0, create_color(0, 0, 0))

    blue_image = red_channel(original)

    for x, y, col in blue_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(blue_image, x, y))


# test_Combine Filter - Author: Bilal Chaudhry 101141634
def test_combine() -> None:
    """
    Function used to test the combined image function.
    compares the rgb value of the combined images to their respective color image
    Test is passed if all of the pixels are the same color, and fails otherwise.

    >>> test_combine(red_image, green_image, blue_image)

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    """

    original_red = create_image(3, 1)
    set_color(original_red, 0, 0, create_color(0, 0, 0))
    set_color(original_red, 1, 0, create_color(127, 0, 0))
    set_color(original_red, 2, 0, create_color(255, 0, 0))

    original_green = create_image(3, 1)
    set_color(original_green, 0, 0, create_color(0, 0, 0))
    set_color(original_green, 1, 0, create_color(0, 127, 0))
    set_color(original_green, 2, 0, create_color(0, 255, 0))

    original_blue = create_image(3, 1)
    set_color(original_blue, 0, 0, create_color(0, 0, 0))
    set_color(original_blue, 1, 0, create_color(0, 0, 127))
    set_color(original_blue, 2, 0, create_color(0, 0, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(127, 127, 127))
    set_color(expected, 2, 0, create_color(255, 255, 255))

    combined_image = combine(original_red, original_green, original_blue)

    for x, y, col in combined_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(combined_image, x, y))


# test_posterize Filter - Author: Bilal Chaudhry 101141634
def test_posterize() -> None:
    """
    Function used to test the posterize function. creates a 6x1 image and which
    is used as input into posterize function. new image is compared to expected
    result and passes test if all pixels are the same. If not, fails test

    >>> test_posterize()

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    """

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(55, 55, 55))
    set_color(original, 1, 0, create_color(110, 110, 110))
    set_color(original, 2, 0, create_color(165, 165, 165))
    set_color(original, 3, 0, create_color(220, 220, 220))

    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(31, 31, 31))
    set_color(expected, 1, 0, create_color(95, 95, 95))
    set_color(expected, 2, 0, create_color(159, 159, 159))
    set_color(expected, 3, 0, create_color(223, 223, 223))

    posterized = posterize(original)

    for x, y, col in posterized:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# test sepia Filter - Author Bilal Chaudhry 101141634
def test_sepia() -> None:
    """
    Tests the sepia function by comparing a 3 by 1 image to an expected
    image of the same dimensions. compares the pixels of the hard coded expected
    image to the pixels in the original image. returns each successful 
    and unsuccessful pixel
    
    It accomplishes this by comparing the
    pixels of the expected image to the original image and returns each
    successful pixel.

    >>> test_sepia()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    """

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(40, 100, 40))
    set_color(original, 1, 0, create_color(100, 100, 100))
    set_color(original, 2, 0, create_color(250, 100, 250))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(66, 60, 54))
    set_color(expected, 1, 0, create_color(114, 100, 85))
    set_color(expected, 2, 0, create_color(216, 200, 186))

    sepia_image = sepia(original)

    for x, y, col in sepia_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# test_two_tone Filter - Author: Pietro Alvarez, 10115082
def test_two_tone(color_1: str, color_2: str) -> None:
    """ Returns "TEST PASSED" or "TEST FAILED" dependant on if the tested
    function works (two_tone) properly at the indicated brightness levels.

    >>> test_two_tone( "red", "blue")

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    """

    r1, g1, b1 = get_RGB(color_1)
    r2, g2, b2 = get_RGB(color_2)

    original = create_image(4, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(127, 127, 127))
    set_color(original, 2, 0, create_color(128, 128, 128))
    set_color(original, 3, 0, create_color(255, 255, 255))

    new = create_image(4, 1)
    set_color(new, 0, 0, create_color(r1, g1, b1))
    set_color(new, 1, 0, create_color(r1, g1, b1))
    set_color(new, 2, 0, create_color(r2, g2, b2))
    set_color(new, 3, 0, create_color(r2, g2, b2))

    Two_tone = two_tone(original, color_1, color_2)

    for x, y, col in Two_tone:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(Two_tone, x, y))


# test_three_tone - Author: Pietro Alvarez, 10115082
def test_three_tone(color_1: str, color_2: str, color_3: str) -> None:
    """ Returns 'TEST PASSED' or 'TEST FAILED' dependant on if the tested
    function (three_tone) has worked with the inputted arguments of colour.

    >>> test_three_tone( "red", "white", "blue")

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------
    """

    r1, g1, b1 = get_RGB(color_1)
    r2, g2, b2 = get_RGB(color_2)
    r3, g3, b3 = get_RGB(color_3)

    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(84, 84, 84))
    set_color(original, 2, 0, create_color(85, 85, 85))
    set_color(original, 3, 0, create_color(170, 170, 170))
    set_color(original, 4, 0, create_color(171, 171, 171))
    set_color(original, 5, 0, create_color(255, 255, 255))

    new = create_image(6, 1)
    set_color(new, 0, 0, create_color(r1, g1, b1))
    set_color(new, 1, 0, create_color(r1, g1, b1))
    set_color(new, 2, 0, create_color(r2, g2, b2))
    set_color(new, 3, 0, create_color(r2, g2, b2))
    set_color(new, 4, 0, create_color(r3, g3, b3))
    set_color(new, 5, 0, create_color(r3, g3, b3))

    Three_tone = three_tone(original, color_1, color_2, color_3)

    for x, y, col in Three_tone:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(Three_tone, x, y))


# extreme_contrast test Filter - Author: Nathan Chen, 101142799
def test_extreme_contrast() -> None:
    """A test function for extreme contrast.

    >>> test_extreme_contrast()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    """

    original = create_image(5, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(128, 0, 0))
    set_color(original, 2, 0, create_color(0, 128, 0))
    set_color(original, 3, 0, create_color(0, 0, 128))
    set_color(original, 4, 0, create_color(128, 128, 128))

    expected = create_image(5, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(255, 255, 255))

    extreme_image = extreme_contrast(original)
    for x, y, col in extreme_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# test_detect_edges Filter - Author: Bilal Chaudhry 101141634
def test_detect_edges() -> None:
    """
    function designed to test the detect_edge filter. Creates temporary 1x3
    original and expected images. processes the original image through the filter
    and compares the values with hard coded expected value to determine the
    accuracy of the function

    >>> test_detect_edges()

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    """

    original = create_image(1, 3)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(10, 10, 10))
    set_color(original, 0, 2, create_color(100, 100, 100))

    expected = create_image(1, 3)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 0, 2, create_color(255, 255, 255))

    edge = detect_edges(original, 15)

    for x, y, col in edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# test_imp_edge_filter - Author: Nathan Chen 101142799
def test_imp_edge() -> None:
    """A test function for edge filter.
    The function compares a made up image which is edited through
    the filer_imp_edge and the an its expected outcome.

    >>> test_extreme_contrast()

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(2, 2) PASSED
    ------
    """

    original = create_image(3, 3)
    set_color(original, 0, 0, create_color(255, 0, 0))
    set_color(original, 1, 0, create_color(155, 0, 0))
    set_color(original, 2, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(255, 0, 0))
    set_color(original, 1, 1, create_color(100, 0, 0))
    set_color(original, 2, 1, create_color(0, 0, 0))
    set_color(original, 0, 2, create_color(255, 0, 0))
    set_color(original, 1, 2, create_color(155, 0, 0))
    set_color(original, 2, 2, create_color(0, 0, 0))

    expected = create_image(3, 3)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(255, 255, 255))
    set_color(expected, 0, 2, create_color(255, 255, 255))
    set_color(expected, 1, 2, create_color(255, 255, 255))
    set_color(expected, 2, 2, create_color(255, 255, 255))

    edge_image = detect_edges_better(original, 15)
    for x, y, col in edge_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# test_horizontal test Filter - Author: Pietro Alvarez, 10115082
def test_flip_horizontal() -> None:
    """ Returns TEST PASSED or TEST FAILED at the indicated (x,y) value, with
    the values of the r, g, b components.

    >>> test_horizontal()

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(0, 3) PASSED
    ------
    Checking pixel @(0, 4) PASSED
    ------
    ------
    """

    original = create_image(1, 5)
    set_color(original, 0, 0, (create_color(0, 0, 0)))
    set_color(original, 0, 1, (create_color(10, 10, 10)))
    set_color(original, 0, 2, (create_color(122, 122, 122)))
    set_color(original, 0, 3, (create_color(180, 180, 180)))
    set_color(original, 0, 4, (create_color(255, 255, 255)))

    expected = create_image(1, 5)
    set_color(expected, 0, 0, (create_color(255, 255, 255)))
    set_color(expected, 0, 1, (create_color(180, 180, 180)))
    set_color(expected, 0, 2, (create_color(122, 122, 122)))
    set_color(expected, 0, 3, (create_color(10, 10, 10)))
    set_color(expected, 0, 4, (create_color(0, 0, 0)))

    horizontal_flip = flip_horizontal(original)

    for x, y, col in horizontal_flip:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(horizontal_flip, x, y))


# test_vertical_flip Filter - Author: Chris Vernon, 101144282
def test_flip_vertical() -> None:
    """
    Tests the flip_vertical function.

    >>> test_vertical_flip()

    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    """
    # Create a image with a resolution of 4x2 (8 pixels in total)
    original = create_image(4, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 0))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 3, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(0, 0, 0))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(255, 255, 255))
    set_color(original, 3, 1, create_color(255, 255, 255))

    # Expected image after passing into the flip_vertical function.
    expected = create_image(4, 2)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 2, 1, create_color(0, 0, 0))
    set_color(expected, 3, 1, create_color(0, 0, 0))

    flipped_image = flip_vertical(original)

    # Checks each pixel and prints 'PASSED' or 'FAILED' based on expected
    # image values and image passed into flip_vertical
    for x, y, col in flipped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


# show(original_img)

print("-------------- Red Image Test --------------")
# show(red_channel(original_img))
test_red_filter()

print("-------------- Green Image Test --------------")
# show(green_channel(original_img))
test_green_filter()

print("-------------- Blue Image Test --------------")
# show(blue_channel(original_img))
test_blue_filter()

print("-------------- Combine Image Test --------------")
# show(combine(image_Red, image_Green, image_Blue))
test_combine()

print("-------------- Posterize Image Test --------------")
# show(posterize(img))
test_posterize()

print("-------------- Sepia Image Test --------------")
# show(posterize(img))
test_sepia()

print("-------------- Extreme Contrast Image Test --------------")
# show(extreme_contrast(img))
test_extreme_contrast()

print("-------------- Two Tone Image Test --------------")
# show(two_tone(img, "white", "black"))
test_two_tone("white", "black")

print("-------------- Three Tone Image Test --------------")
# show(three_tone(img, "white", "black", "red"))
test_three_tone("white", "black", "red")

print("-------------- Detect Edges Image Test --------------")
# show(detect_edges(img, 15))
test_detect_edges()

print("-------------- Improved Detect Edges Image Test --------------")
# show(detect_edges_better(img, 15))
test_imp_edge()

print("-------------- Horizontal Flip Image Test --------------")
# show(flip_horizontal(img))
test_flip_horizontal()

print("-------------- Vertical Flip Image Test --------------")
# show(flip_vertical(img))
test_flip_vertical()
